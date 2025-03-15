from django.shortcuts import render

from django.http import JsonResponse
from .models import Student

def orm_query(request):
    # Insert Data
    Student.objects.create(name="django", age=25, city="London")

    # Fetch All Data
    students = Student.objects.all().values()

    return JsonResponse(list(students), safe=False)
