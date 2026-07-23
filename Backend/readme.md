# 🖥️ Backend

This folder contains the backend implementation of the **Attendance Management System** developed using **Python**, **Flask**, and **MySQL**. The backend is responsible for handling business logic, database operations, authentication, and communication between the frontend and the database.

---

## 📂 Files

| File | Description |
|------|-------------|
| `app.py` | Main Flask application that initializes the server, registers blueprints, manages routes, and handles user authentication. |
| `database.py` | Establishes the connection with the MySQL database. |
| `api_students.py` | Provides API endpoints for student-related operations such as adding and retrieving student records. |
| `api_subjects.py` | Provides API endpoints for subject management. |
| `api_attendance.py` | Handles attendance-related operations, including marking, viewing, and storing attendance records. |
| `test_db.py` | Tests the database connection to ensure proper connectivity with MySQL. |

---

## ⚙️ Technologies Used

- Python 3
- Flask
- MySQL
- MySQL Connector for Python
- ReportLab (PDF Generation)

---

## 🚀 Features

- User Authentication (Admin Login)
- Student Management
- Subject Management
- Attendance Management
- Bulk Attendance
- Attendance Percentage Calculation
- PDF Report Generation
- MySQL Database Integration
- RESTful API Design using Flask Blueprints

---

## 🔄 Backend Workflow

```text
Client Request
       │
       ▼
Flask Routes (app.py)
       │
       ▼
Blueprint APIs
(Student / Subject / Attendance)
       │
       ▼
Database Connection (database.py)
       │
       ▼
MySQL Database
       │
       ▼
Response Returned to Frontend
```

---

## 📌 API Modules

### 👨‍🎓 Student API
- Add Student
- View Students
- Retrieve Student Details

### 📚 Subject API
- Add Subject
- View Subjects

### ✅ Attendance API
- Mark Attendance
- Bulk Attendance
- View Attendance
- Calculate Attendance Percentage
- Generate Attendance Reports

---

## 🔐 Authentication

The backend includes an admin authentication system using Flask sessions. Protected routes require users to log in before accessing attendance management features.

---

## 🗄️ Database

The backend communicates with a MySQL database to store and retrieve:

- Student Information
- Subject Details
- Attendance Records
- Admin Credentials

---

## ▶️ Running the Backend

Start the Flask server:

```bash
python app.py
```

By default, the application runs at:

```
http://127.0.0.1:5000
```

---

## 📖 Learning Outcomes

This backend demonstrates:

- Flask Application Development
- REST API Development
- CRUD Operations
- Blueprint Architecture
- Session-Based Authentication
- MySQL Integration
- Database Connectivity
- Backend-Frontend Communication
