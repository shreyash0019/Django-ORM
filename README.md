# Django ORM Operations

This project demonstrates various CRUD (Create, Read, Update, Delete) operations using Django ORM.

## Project Structure

```
Django-ORM/
│
├── orm/
│   └── settings.py
│
├── testapp/
│   └── models.py
│
├── manage.py
│
└── project.csv
```

## Prerequisites

- Python Installed
- Django Installed
- MySQL Database Setup

## Models.py

```python
from django.db import models

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    roll_number = models.IntegerField()
    student_class = models.CharField(max_length=50)
```

## Operations Performed

### 1. Create Operation

```python
Student.objects.create(id=101, name='Aon', age=10, city='Pune', roll_number=502, student_class='Class_2')
```

### 2. Retrieve Data

```python
Student.objects.all()
Student.objects.filter(city='Pune')
```

### 3. Update Operation

```python
student = Student.objects.get(id=101)
student.student_class = 'Class_2'
student.save()
```

### 4. Delete Operation

```python
student = Student.objects.get(id=101)
student.delete()
```

### 5. Bulk Data Insertion

```python
students = [
    Student(id=102, name='John', age=15, city='Mumbai', roll_number=503, student_class='Class_3'),
    Student(id=103, name='Emma', age=14, city='Delhi', roll_number=504, student_class='Class_4')
]
Student.objects.bulk_create(students)
```

## Export to CSV

```python
import csv

with open('project.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'Name', 'Age', 'City', 'Roll Number', 'Class'])
    for student in Student.objects.all():
        writer.writerow([student.id, student.name, student.age, student.city, student.roll_number, student.student_class])
```

## How to Run

```bash
python manage.py runserver
```

## Conclusion

This project demonstrates the fundamental CRUD operations in Django ORM and how to export data to CSV.

