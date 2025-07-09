# Student Profile Management System (Python Tkinter + MySQL)

This is a desktop application built using Python's Tkinter library for the graphical user interface and MySQL as the backend database. The system allows users to perform basic CRUD operations on student profiles.

## Features

- Add new student records
- View all student profiles in a table
- Update existing student details
- Delete student records
- Clear input fields
- Simple and intuitive GUI

## Fields Managed

- Student ID (Auto-incremented)
- Name
- Email
- Phone
- Course

## Technologies Used

- Python 3.x
- Tkinter (GUI)
- MySQL
- mysql-connector-python (JDBC for MySQL)

## Database Setup

Run the following SQL commands in your MySQL server:

```sql
CREATE DATABASE IF NOT EXISTS StudentManagement;

USE StudentManagement;

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    course VARCHAR(50)
);
