from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    student_class = models.CharField(max_length=50, default='')
    roll_number = models.IntegerField(unique=True, default=0)
    city = models.CharField(max_length=100)

class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()
    exam_date = models.DateField()

class Game(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    game_name = models.CharField(max_length=100)
    game_type = models.CharField(max_length=100)
    score = models.IntegerField()

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])
