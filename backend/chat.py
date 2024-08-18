from transformers import BertTokenizer, BertForSequenceClassification
import torch
from models.database import StudentPerformance, DepartmentInformation, EmployeeInformation, StudentInformation

class NLPModel:
    def __init__(self, model_path='backend/models/my_model'):  # Update model path
        self.tokenizer = BertTokenizer.from_pretrained(model_path)
        self.model = BertForSequenceClassification.from_pretrained(model_path)

    def classify(self, text):
        inputs = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
        outputs = self.model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()
        return predicted_class

nlp_model = NLPModel()

CLASS_MAP = {
    0: "performance",
    1: "department",
    2: "employee",
    3: "counseling"
}

def get_classification(message):
    predicted_class = nlp_model.classify(message)
    return CLASS_MAP[predicted_class]

def handle_chat(message):
    message = message.lower()
    response = "I can help you with information about student performances, departments, employees, and counseling sessions. Ask me about one of these topics!"
    
    classification = get_classification(message)
    
    if classification == "performance":
        performances = StudentPerformance.query.all()
        response = "Here are the student performances:\n"
        response += "\n".join([f"Student {performance.student_id}: {performance.marks}" for performance in performances])
    elif classification == "department":
        departments = DepartmentInformation.query.all()
        response = "Here are the departments:\n"
        response += "\n".join([f"{dept.name} established on {dept.doe}" for dept in departments])
    elif classification == "employee":
        employees = EmployeeInformation.query.all()
        response = "Here are the employees:\n"
        response += "\n".join([f"{emp.employee_id}, Name: {emp.name}, DOB: {emp.dob}, DOJ: {emp.doj}, Dept ID: {emp.department_id}, Position: {emp.position}" for emp in employees])
    elif classification == "counseling":
        counselings = StudentInformation.query.all()
        response = "Here are the counseling sessions:\n"
        response += "\n".join([f"{counsel.student_id}: {counsel.counseling_notes}" for counsel in counselings])
    
    return response
