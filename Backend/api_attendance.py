from flask import Blueprint, request, redirect, render_template
from database import get_db_connection
from datetime import date

attendance_api = Blueprint(
    "attendance_api",
    __name__,
    url_prefix="/attendance"
)

# ---------------- ADD ATTENDANCE ----------------
@attendance_api.route("/add", methods=["POST"])
def add_attendance():
    student_id = request.form.get("student_id")
    subject_id = request.form.get("subject_id")
    status = request.form.get("status")
    attendance_date = date.today()

    conn = get_db_connection()
    cursor = conn.cursor()

    # prevent duplicate for same day
    cursor.execute("""
        SELECT 1 FROM attendance
        WHERE student_id=%s AND subject_id=%s AND attendance_date=%s
    """, (student_id, subject_id, attendance_date))

    if cursor.fetchone():
        cursor.close()
        conn.close()
        return "Attendance already marked for today"

    cursor.execute("""
        INSERT INTO attendance (student_id, subject_id, status, attendance_date)
        VALUES (%s, %s, %s, %s)
    """, (student_id, subject_id, status, attendance_date))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect("/attendance/list")


# ---------------- VIEW ATTENDANCE ----------------
@attendance_api.route("/list", methods=["GET"])
def attendance_list():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT 
            s.name,
            sub.subject_name,
            a.status,
            a.attendance_date
        FROM attendance a
        JOIN students s ON a.student_id = s.student_id
        JOIN subjects sub ON a.subject_id = sub.subject_id
        ORDER BY a.attendance_date DESC
    """)

    attendance = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("view_attendance.html", attendance=attendance)
