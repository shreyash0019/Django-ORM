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

## Models Structure

The project defines a `Student` model with attributes such as ID, Name, Age, City, Roll Number, and Class. These fields are used to perform various ORM operations.

## Operations Performed

### 1. Create Operation

The create operation involves adding a new student record with details like ID, name, age, city, roll number, and class.

### 2. Retrieve Data

The retrieve operation allows fetching all student records or filtering them based on specific conditions, such as filtering by city.

### 3. Update Operation

The update operation enables modifying an existing record. For instance, updating the class of a student after mistakenly entering incorrect data.

### 4. Delete Operation

The delete operation is used to remove a specific student record from the database.

### 5. Bulk Data Insertion

Bulk data insertion allows adding multiple student records at once, which is useful when handling large datasets.

## Data Export to CSV

The project includes functionality to export student data to a CSV file. This allows easy data analysis and reporting.

## How to Run the Project

1. Ensure all prerequisites are installed.
2. Run the Django server to perform CRUD operations.

