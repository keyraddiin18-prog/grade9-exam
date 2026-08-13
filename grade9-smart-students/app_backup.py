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
        registration_number = request.form.get("registration_number", "").strip()

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


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

