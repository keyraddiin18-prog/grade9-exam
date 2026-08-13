from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "grade9-smart-students-2026"

DATABASE = "exam.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        registration_number = request.form.get(
            "registration_number", ""
        ).strip()

        conn = get_db()

        student = conn.execute(
            """
            SELECT * FROM students
            WHERE full_name = ? AND registration_number = ?
            """,
            (full_name, registration_number)
        ).fetchone()

        conn.close()

        if student:
            session["student_id"] = student["id"]
            session["student_name"] = student["full_name"]
            session["registration_number"] = student["registration_number"]

            return redirect(url_for("student_dashboard"))

        return render_template(
            "login.html",
            error="Student name or registration number is incorrect."
        )

    return render_template("login.html")


@app.route("/student")
def student_dashboard():
    if "student_id" not in session:
        return redirect(url_for("login"))

    return render_template(
        "student.html",
        student_name=session["student_name"],
        registration_number=session["registration_number"]
    )


@app.route("/subjects")
def subjects():
    if "student_id" not in session:
        return redirect(url_for("login"))

    conn = get_db()

    subjects = conn.execute(
        """
        SELECT s.*, COUNT(q.id) AS question_count
        FROM subjects s
        LEFT JOIN questions q ON s.id = q.subject_id
        GROUP BY s.id
        ORDER BY s.id
        """
    ).fetchall()

    conn.close()

    return render_template(
        "subjects.html",
        subjects=subjects,
        student_name=session["student_name"]
    )


@app.route("/subject/<int:subject_id>", methods=["GET", "POST"])
def subject_detail(subject_id):

    if "student_id" not in session:
        return redirect(url_for("login"))

    conn = get_db()

    subject = conn.execute(
        "SELECT * FROM subjects WHERE id = ?",
        (subject_id,)
    ).fetchone()

    questions = conn.execute(
        """
        SELECT *
        FROM questions
        WHERE subject_id = ?
        ORDER BY id
        """
        ,
        (subject_id,)
    ).fetchall()

    if not subject:
        conn.close()
        return "Subject not found", 404

    # =========================
    # EXAM SUBMISSION
    # =========================
    if request.method == "POST":

        total_questions = len(questions)
        score = 0

        for q in questions:
            question_id = str(q["id"])

            student_answer = request.form.get(
                f"question_{question_id}"
            )

            correct_answer = q["correct_answer"]

            if student_answer and student_answer.upper() == correct_answer.upper():
                score += 1

        # Calculate percentage
        if total_questions > 0:
            percentage = (score / total_questions) * 100
        else:
            percentage = 0

        # Qualification: 55% or above
        if percentage >= 55:
            status = "Qualified"
        else:
            status = "Not Qualified"

        conn.close()

        return render_template(
            "result.html",
            subject=subject,
            score=score,
            total_questions=total_questions,
            percentage=round(percentage, 2),
            status=status,
            student_name=session["student_name"],
            registration_number=session["registration_number"]
        )

    conn.close()

    return render_template(
        "subject.html",
        subject=subject,
        questions=questions,
        student_name=session["student_name"]
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
