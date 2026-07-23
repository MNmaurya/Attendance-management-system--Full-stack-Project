# 📂 Templates

This folder contains all the HTML templates used by the Flask application. These templates are rendered dynamically using Flask's Jinja2 template engine.

## 📄 Files

| File | Description |
|------|-------------|
| `base.html` | Base layout template containing the common structure (header, footer, navigation, etc.) shared across all pages. |
| `home.html` | Home page/dashboard of the Attendance Management System. |
| `login.html` | User login page for authentication. |
| `add_student.html` | Form to add new student records. |
| `add_subject.html` | Form to add new subjects. |
| `mark_attendance.html` | Interface for marking attendance for students. |
| `bulk_attendance.html` | Page for marking attendance for multiple students simultaneously. |
| `view_students.html` | Displays the list of registered students. |
| `view_subjects.html` | Displays the list of available subjects. |
| `view_attendance.html` | Shows attendance records of students. |
| `attendance_percentage.html` | Displays attendance percentage for individual students. |

## ⚙️ Template Engine


Example:

```html
{% extends "base.html" %}

{% block content %}
<h2>Welcome to Attendance Management System</h2>
{% endblock %}
```

## 📌 Purpose

These templates provide the user interface for the Attendance Management System and interact with the Flask backend to display and manage data stored in the MySQL database.

## 🛠 Technologies Used

- HTML5
- CSS3
- Bootstrap 5
