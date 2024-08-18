from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class StudentPerformance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(50), nullable=False)
    course_id = db.Column(db.String(50), nullable=False)
    marks = db.Column(db.Float, nullable=False)

class DepartmentInformation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    doe = db.Column(db.String(50), nullable=False)

class EmployeeInformation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(100), nullable=False)
    doj = db.Column(db.String(100), nullable=False)
    department_id = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(50), nullable=False)

class StudentInformation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    department_id = db.Column(db.String(50), nullable=False)
    financial_status = db.Column(db.String(100), nullable=False)

class CourseInformation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    department_id = db.Column(db.String(50), nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    prerequisite_course_id = db.Column(db.String(50), nullable=True)

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
