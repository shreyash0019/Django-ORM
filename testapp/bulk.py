import random
from django.utils import timezone
from testapp.models import Student, Score, Game, Attendance

subjects = ['Math', 'Science', 'English', 'History', 'Geography']
games = ['Football', 'Basketball', 'Cricket', 'Chess', 'Volleyball']

students = []

for i in range(1, 501):  # Generating 500 records
    student = Student(
        name=f'Student_{i}',
        age=random.randint(10, 18),   # Unique age for all
        student_class=f'Class_{random.randint(1, 12)}',
        roll_number=i,  # Unique roll numbers
        city=random.choice(['Mumbai', 'Delhi', 'Bangalore', 'Pune', 'Chennai'])
    )
    students.append(student)

# Bulk insert into the database
Student.objects.bulk_create(students)
