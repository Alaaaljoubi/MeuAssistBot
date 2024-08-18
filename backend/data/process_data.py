import sys
import os
import pandas as pd
import random
from faker import Faker

fake = Faker()

# Add the path to the app module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Load the Excel file
excel_file = './university_data.xlsx'

# Read the sheets
department_df = pd.read_excel(excel_file, sheet_name='Department Information')
course_df = pd.read_excel(excel_file, sheet_name='Course Information')
student_df = pd.read_excel(excel_file, sheet_name='Student Information')
employee_df = pd.read_excel(excel_file, sheet_name='Employee Information')
performance_df = pd.read_excel(excel_file, sheet_name='Student Performance')

# Generate labeled data for training
questions = []
labels = []

# Add questions related to student performance
for _, row in performance_df.iterrows():
    questions.append(f"What is the performance of student {row['Student ID']} in course {row['Course ID']}?")
    labels.append("performance")
    questions.append(f"How did student {row['Student ID']} perform in course {row['Course ID']}?")
    labels.append("performance")
    questions.append(f"Describe the performance of student {row['Student ID']} in course {row['Course ID']}.")
    labels.append("performance")

# Add questions related to department information
for _, row in department_df.iterrows():
    questions.append(f"Tell me about the department {row['Department Name']}.")
    labels.append("department")
    questions.append(f"Provide information about the {row['Department Name']} department.")
    labels.append("department")
    questions.append(f"Give me the details of the {row['Department Name']} department.")
    labels.append("department")

# Add questions related to employee information
for _, row in employee_df.iterrows():
    questions.append(f"Who is the employee with ID {row['Employee ID']}?")
    labels.append("employee")
    questions.append(f"List the details of employee with ID {row['Employee ID']}.")
    labels.append("employee")
    questions.append(f"Provide information about employee with ID {row['Employee ID']}.")
    labels.append("employee")

# Add questions related to student counseling
for _, row in student_df.iterrows():
    questions.append(f"What are the counseling sessions for student {row['Student ID']}?")
    labels.append("counseling")
    questions.append(f"Detail the counseling notes for student {row['Student ID']}.")
    labels.append("counseling")
    questions.append(f"Provide counseling session information for student {row['Student ID']}.")
    labels.append("counseling")

# Create a DataFrame for the labeled data
labeled_data = pd.DataFrame({
    'question': questions,
    'label': labels
})

# Save the labeled data to CSV
labeled_data.to_csv('./labeled_data.csv', index=False)

print("Labeled data generated and saved to './data/labeled_data.csv'")

# The rest of the process_data.py script for loading data into the database
def process_data():
    from app import app
    from models import db
    
    with app.app_context():
        department_df.to_sql('department_information', db.engine, if_exists='replace', index=False)
        course_df.to_sql('course_information', db.engine, if_exists='replace', index=False)
        student_df.to_sql('student_information', db.engine, if_exists='replace', index=False)
        employee_df.to_sql('employee_information', db.engine, if_exists='replace', index=False)
        performance_df.to_sql('student_performance', db.engine, if_exists='replace', index=False)
        print("Data processed and saved to the database")

if __name__ == '__main__':
    process_data()
    print("Data processed successfully")
