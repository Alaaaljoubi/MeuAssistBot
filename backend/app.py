from flask import Flask, request, jsonify, session
from flask_cors import CORS
from fuzzywuzzy import fuzz
import json
import os
from functools import wraps

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Replace with a strong secret key

# Enable CORS with session support
CORS(app, supports_credentials=True)

# Path to the JSON file
DATA_FILE = '/Users/anasalsayed/Documents/PROJECTS/MeuAssistBot/backend/data/Questions.json'

# Load the questions and answers from the JSON file
def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Save data back to the JSON file
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Initial load of the data
kbs_data = load_data()

# Dummy admin credentials
ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "password123"

# Helper function to check if user is logged in
def is_logged_in():
    return session.get('logged_in', False)

@app.route('/admin/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
        session['logged_in'] = True
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

# Logout route
@app.route('/admin/logout', methods=['POST'])
def logout():
    session.pop('logged_in', None)
    return jsonify({'message': 'Logout successful'}), 200

# Decorator to protect admin routes
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_logged_in():
            return jsonify({'message': 'Please log in first'}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route('/kbs', methods=['POST'])
def answer_question():
    user_question = request.json.get('question', '').lower().strip()

    # Preprocessing step: handling common typos or issues
    if user_question.startswith('ريد'):
        user_question = 'أ' + user_question

    # Initialize variables to store the best match
    best_match = None
    highest_score = 0

    # Search for the best answer using fuzzy matching
    for category, qa_pairs in kbs_data.items():
        for qa in qa_pairs:
            score = fuzz.ratio(user_question, qa['question'].lower())
            if score > highest_score:
                highest_score = score
                best_match = qa['answer']

    # Set a threshold to consider a match (e.g., 60% similarity)
    if highest_score >= 60:
        return jsonify({'answer': best_match})

    return jsonify({'answer': "Sorry, I couldn't find the answer to that question."})

# Admin endpoint to add a new question and answer
@app.route('/admin/add', methods=['POST'])
@login_required
def add_qa():
    new_qa = request.json
    category = new_qa.get('category', 'general')
    if category not in kbs_data:
        kbs_data[category] = []

    kbs_data[category].append({
        'question': new_qa['question'],
        'answer': new_qa['answer']
    })
    save_data(kbs_data)
    return jsonify({'message': 'Question added successfully'}), 201

# Admin endpoint to update an existing question and answer
@app.route('/admin/update', methods=['PUT'])
@login_required
def update_qa():
    updated_qa = request.json
    category = updated_qa.get('category', 'general')
    if category in kbs_data:
        for qa in kbs_data[category]:
            if qa['question'] == updated_qa['old_question']:
                qa['question'] = updated_qa['new_question']
                qa['answer'] = updated_qa['new_answer']
                save_data(kbs_data)
                return jsonify({'message': 'Question updated successfully'}), 200

    return jsonify({'message': 'Question not found'}), 404

# Admin endpoint to delete a question and answer
@app.route('/admin/delete', methods=['DELETE'])
@login_required
def delete_qa():
    category = request.json.get('category', 'general')
    question_to_delete = request.json.get('question')
    if category in kbs_data:
        kbs_data[category] = [qa for qa in kbs_data[category] if qa['question'] != question_to_delete]
        save_data(kbs_data)
        return jsonify({'message': 'Question deleted successfully'}), 200

    return jsonify({'message': 'Question not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
