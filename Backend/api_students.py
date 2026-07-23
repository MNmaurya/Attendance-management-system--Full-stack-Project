from flask import Blueprint, request
from database import get_db_connection
import mysql.connector

students_api = Blueprint("students_api", __name__)

@students_api.route("/students/add", methods=["POST"])
def add_student():
    name = request.form.get("name")
    roll_no = request.form.get("roll_no")
    student_class = request.form.get("class")

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO students (name, roll_no, class) VALUES (%s, %s, %s)",
            (name, roll_no, student_class)
        )
        conn.commit()
        return "✅ Student Added Successfully"

    except mysql.connector.IntegrityError:
        return "⚠️ Roll number already exists! Try different one."

    finally:
        cursor.close()
        conn.close()