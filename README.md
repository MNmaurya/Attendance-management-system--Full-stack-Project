# 🎓 Attendance Management System
A Full-Stack Attendance Management System developed using **Python Flask**, **MySQL**, **HTML**, **CSS**, and **Bootstrap**. The application helps educational institutions efficiently manage students, subjects, attendance records, and attendance reports through a user-friendly web interface.

---

## 📌 Features

### 👨‍🎓 Student Management
- Add new students
- View student records
- Store student details securely in MySQL
  
### 📚 Subject Management
- Add subjects
- View subject list
- Manage subject information

### ✅ Attendance Management
- Mark attendance
- Bulk attendance support
- View attendance records
- Attendance stored in MySQL database

### 📊 Attendance Analytics
- Automatic attendance percentage calculation
- Individual student attendance tracking

### 💾 Database Integration
- MySQL database connectivity using Flask
- CRUD operations
- Organized database structure

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend Programming |
| Flask | Web Framework |
| MySQL | Database |
| HTML5 | Frontend Structure |
| CSS3 | Styling |
| Bootstrap | Responsive UI |
| ReportLab | PDF Generation |

---

# 📁 Project Structure

```text
Attendance-Management-System/
│
├── app.py
├── database.py
├── api_students.py
├── api_subjects.py
├── api_attendance.py
├── templates/
├── database/
├── screenshots/
└── README.md
```

---

## Create Database

Open MySQL and create a database.

```sql
CREATE DATABASE attendance_management;
```

Import the provided SQL file.

```
database/attendance.sql
```

---

## 5️⃣ Configure Database

Update the database credentials in

```
database.py
```

---

## 6️⃣ Run the Application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

# 📸 Screenshots

## Login Page
<img width="950" height="463" alt="image" src="https://github.com/user-attachments/assets/2202207e-916f-4194-a1e3-9fa2739abaac" />

---

## Dashboard

<img width="955" height="420" alt="image" src="https://github.com/user-attachments/assets/b5029795-f901-4f17-9e95-81048339ed75" />


---

## Add Student

<img width="952" height="418" alt="image" src="https://github.com/user-attachments/assets/8d9fe492-107f-4442-a291-a1a72f2de8b6" />


---

## Mark Attendance

<img width="955" height="422" alt="image" src="https://github.com/user-attachments/assets/9732db16-7727-4ac5-b413-4b3c3ea0f732" />

<img width="955" height="418" alt="image" src="https://github.com/user-attachments/assets/d7fefb70-ef5f-4c80-9b90-0cdb41b2cb8a" />

<img width="950" height="436" alt="image" src="https://github.com/user-attachments/assets/2fc02220-eb0d-4379-a757-d0d45ff32e71" />

---

## Attendance Percentage

![Uploading image.png…]()

---


# ✨ Future Enhancements

- Student profile photos
- Email notifications
- QR Code attendance
- Face Recognition attendance
- Role-based authentication
- Attendance graphs and analytics
- Export reports in Excel
- Search and filter functionality

---

# 🎯 Learning Outcomes

Through this project, I learned:

- Flask Web Development
- REST API Design
- CRUD Operations
- MySQL Database Integration
- Responsive Web Design
- PDF Report Generation
- Backend-Frontend Integration
- Project Structuring

---

# 👩‍💻 Author

**Muskan Maurya**

B.Tech Artificial Intelligence & Machine Learning

Delhi Skill and Entrepreneurship University (DSEU)

---

## ⭐ If you found this project useful, consider giving it a Star!
