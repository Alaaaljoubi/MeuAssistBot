import pandas as pd
import random
from faker import Faker

fake = Faker()

# Generating Department Information
department_names = [
    'Computer Science', 'Mechanical Engineering', 'Civil Engineering', 'Electrical Engineering', 'Business Administration',
    'Chemical Engineering', 'Physics', 'Mathematics', 'Biology', 'Economics'
]
departments = []
for i in range(1, 11):
    departments.append([f'DEP{i}', department_names[i-1], fake.date_this_century()])

department_df = pd.DataFrame(departments, columns=['Department ID', 'Department Name', 'Date of Establishment'])

# Generating Course Information
course_names = [
    'Algorithms', 'Thermodynamics', 'Fluid Mechanics', 'Circuit Theory', 'Management Principles', 
    'Data Structures', 'Machine Learning', 'Project Management', 'Database Systems', 'Digital Signal Processing',
    'Organic Chemistry', 'Physical Chemistry', 'Quantum Mechanics', 'Linear Algebra', 'Calculus',
    'Microbiology', 'Genetics', 'Macroeconomics', 'Microeconomics', 'Financial Accounting'
]
courses = []
for i in range(1, 101):
    course_name = random.choice(course_names)
    department_id = random.choice(department_df['Department ID'])
    credits = random.randint(2, 5)
    prerequisite_course_id = f'COURSE{random.randint(1, i-1)}' if i > 1 else None
    courses.append([f'COURSE{i}', course_name, department_id, credits, prerequisite_course_id])

course_df = pd.DataFrame(courses, columns=['Course ID', 'Course Name', 'Department ID', 'Credits', 'Prerequisite Course ID'])

# Generating Student Information
students = []
for i in range(1, 5001):
    financial_status = f"${random.randint(0, 5000)} Outstanding"
    students.append([f'STUD{i}', fake.name(), random.randint(18, 25), random.choice(['M', 'F']), random.choice(department_df['Department ID']), financial_status])

student_df = pd.DataFrame(students, columns=['Student ID', 'Name', 'Age', 'Gender', 'Department ID', 'Financial Status'])

# Generating Employee Information
positions = ['Professor', 'Assistant Professor', 'Lecturer', 'Lab Technician', 'Administrator']
employees = []
for i in range(1, 501):
    employees.append([f'EMP{i}', fake.name(), fake.date_of_birth(minimum_age=25, maximum_age=65), fake.date_this_century(), random.choice(department_df['Department ID']), random.choice(positions)])

employee_df = pd.DataFrame(employees, columns=['Employee ID', 'Name', 'Date of Birth', 'Date of Joining', 'Department ID', 'Position'])

# Generating Student Performance Information
performances = []
for _ in range(50000):
    student_id = random.choice(student_df['Student ID'])
    course_id = random.choice(course_df['Course ID'])
    marks = random.uniform(0, 100)
    performances.append([student_id, course_id, marks])

performance_df = pd.DataFrame(performances, columns=['Student ID', 'Course ID', 'Marks'])

# Saving to Excel
with pd.ExcelWriter('university_data.xlsx') as writer:
    department_df.to_excel(writer, sheet_name='Department Information', index=False)
    course_df.to_excel(writer, sheet_name='Course Information', index=False)
    student_df.to_excel(writer, sheet_name='Student Information', index=False)
    employee_df.to_excel(writer, sheet_name='Employee Information', index=False)
    performance_df.to_excel(writer, sheet_name='Student Performance', index=False)

print("Data generated and saved to 'university_data.xlsx'")
