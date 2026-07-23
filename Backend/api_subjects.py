from flask import Blueprint, request, jsonify, redirect 
from database import get_db_connection

subjects_api = Blueprint("subjects_api", __name__, url_prefix="/subjects")

# -------- ADD SUBJECT --------
@subjects_api.route("/add", methods=["POST"])
def add_subject():
    subject_name = request.form.get("subject_name")

    if not subject_name:
        return "Subject name required", 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO subjects (subject_name) VALUES (%s)",
        (subject_name,)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return redirect("/view_subjects")

# -------- GET SUBJECTS --------
@subjects_api.route("/", methods=["GET"])
def get_subjects():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM subjects")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)
