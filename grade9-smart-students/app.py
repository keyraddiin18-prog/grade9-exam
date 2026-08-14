from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)

# =========================================================
# APP CONFIGURATION
# =========================================================

app.secret_key = "grade9-smart-students-2026"

DATABASE = "exam.db"


# =========================================================
# DATABASE CONNECTION
# =========================================================

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():
    return redirect(url_for("login"))


    return redirect(url_for("login"))
# LOGIN
# =========================================================
    return redirect(url_for("login"))
@app.route("/login", methods=["GET", "POST"])
def login():
    return redirect(url_for("login"))
    if request.method == "POST":

    return redirect(url_for("login"))
            "full_name",
            ""
    return redirect(url_for("login"))

        registration_number = request.form.get(
    return redirect(url_for("login"))
            ""
        ).strip()
    return redirect(url_for("login"))
        conn = get_db()

    return redirect(url_for("login"))
            """
            SELECT *
    return redirect(url_for("login"))
            WHERE full_name = ?
            AND registration_number = ?
    return redirect(url_for("login"))
            (
                full_name,
    return redirect(url_for("login"))
            )
        ).fetchone()
    return redirect(url_for("login"))
        conn.close()

    return redirect(url_for("login"))

            session["student_id"] = student["id"]
    return redirect(url_for("login"))
            session["student_name"] = (
                student["full_name"]
    return redirect(url_for("login"))

            session["registration_number"] = (
    return redirect(url_for("login"))
            )

    return redirect(url_for("login"))
                url_for("student_dashboard")
            )
    return redirect(url_for("login"))
        return render_template(
            "login.html",
    return redirect(url_for("login"))
        )

    return redirect(url_for("login"))


    return redirect(url_for("login"))
# STUDENT DASHBOARD
# =========================================================
    return redirect(url_for("login"))
@app.route("/student")
def student_dashboard():
    return redirect(url_for("login"))
    if "student_id" not in session:
        return redirect(
    return redirect(url_for("login"))
        )

    return redirect(url_for("login"))
        "student.html",
        student_name=session["student_name"],
    return redirect(url_for("login"))
            "registration_number"
        ]
    return redirect(url_for("login"))


    return redirect(url_for("login"))
# SUBJECTS
# =========================================================
    return redirect(url_for("login"))
@app.route("/subjects")
def subjects():
    return redirect(url_for("login"))
    if "student_id" not in session:
        return redirect(
    return redirect(url_for("login"))
        )

    return redirect(url_for("login"))

    subjects_data = conn.execute(
    return redirect(url_for("login"))
        SELECT *
        FROM subjects
    return redirect(url_for("login"))
        """
    ).fetchall()
    return redirect(url_for("login"))
    conn.close()

    return redirect(url_for("login"))
        "subjects.html",
        subjects=subjects_data,
    return redirect(url_for("login"))
    )

    return redirect(url_for("login"))
# =========================================================
# SUBJECT / EXAM
    return redirect(url_for("login"))

@app.route(
    return redirect(url_for("login"))
    methods=["GET", "POST"]
)
    return redirect(url_for("login"))

    if "student_id" not in session:
    return redirect(url_for("login"))
            url_for("login")
        )
    return redirect(url_for("login"))
    conn = get_db()

    return redirect(url_for("login"))
    subject = conn.execute(
        """
    return redirect(url_for("login"))
        FROM subjects
        WHERE id = ?
    return redirect(url_for("login"))
        (subject_id,)
    ).fetchone()
    return redirect(url_for("login"))
    # Subject not found
    if not subject:
    return redirect(url_for("login"))
        conn.close()

    return redirect(url_for("login"))

    # Get questions
    return redirect(url_for("login"))
        """
        SELECT *
    return redirect(url_for("login"))
        WHERE subject_id = ?
        ORDER BY id
    return redirect(url_for("login"))
        (subject_id,)
    ).fetchall()
    return redirect(url_for("login"))

    # =====================================================
    return redirect(url_for("login"))
    # =====================================================

    return redirect(url_for("login"))

        total_questions = len(questions)
    return redirect(url_for("login"))
        score = 0

    return redirect(url_for("login"))

            question_id = str(
    return redirect(url_for("login"))
            )

    return redirect(url_for("login"))
                f"question_{question_id}"
            )
    return redirect(url_for("login"))
            correct_answer = question[
                "correct_answer"
    return redirect(url_for("login"))

            if (
    return redirect(url_for("login"))
                and
                student_answer.upper()
    return redirect(url_for("login"))
                correct_answer.upper()
            ):
    return redirect(url_for("login"))


    return redirect(url_for("login"))
        # PERCENTAGE
        # =================================================
    return redirect(url_for("login"))
        if total_questions > 0:

    return redirect(url_for("login"))
                score / total_questions
            ) * 100
    return redirect(url_for("login"))
        else:

    return redirect(url_for("login"))


    return redirect(url_for("login"))
        # QUALIFICATION
        # =================================================
    return redirect(url_for("login"))
        if percentage >= 55:

    return redirect(url_for("login"))

        else:
    return redirect(url_for("login"))
            status = "Not Qualified"

    return redirect(url_for("login"))
        # =================================================
        # CREATE RESULTS TABLE
    return redirect(url_for("login"))

        conn.execute(
    return redirect(url_for("login"))
            CREATE TABLE IF NOT EXISTS results (

    return redirect(url_for("login"))

                student_id INTEGER,
    return redirect(url_for("login"))
                subject_id INTEGER,

    return redirect(url_for("login"))

                total_questions INTEGER,
    return redirect(url_for("login"))
                percentage REAL,

    return redirect(url_for("login"))
            )
            """
    return redirect(url_for("login"))


    return redirect(url_for("login"))
        # SAVE RESULT
        # =================================================
    return redirect(url_for("login"))
        conn.execute(
            """
    return redirect(url_for("login"))
            (
                student_id,
    return redirect(url_for("login"))
                score,
                total_questions,
    return redirect(url_for("login"))
                status
            )
    return redirect(url_for("login"))
            """,
            (
    return redirect(url_for("login"))
                subject_id,
                score,
    return redirect(url_for("login"))
                percentage,
                status
    return redirect(url_for("login"))
        )

    return redirect(url_for("login"))

        conn.close()
    return redirect(url_for("login"))

        # =================================================
    return redirect(url_for("login"))
        # =================================================

    return redirect(url_for("login"))
            "result.html",

    return redirect(url_for("login"))

            score=score,
    return redirect(url_for("login"))
            total_questions=total_questions,

    return redirect(url_for("login"))
                percentage,
                2
    return redirect(url_for("login"))

            status=status,
    return redirect(url_for("login"))
            student_name=session[
                "student_name"
    return redirect(url_for("login"))

            registration_number=session[
    return redirect(url_for("login"))
            ]
        )
    return redirect(url_for("login"))

    # Close database for GET
    return redirect(url_for("login"))


    return redirect(url_for("login"))
    # EXAM PAGE
    # =====================================================
    return redirect(url_for("login"))
    return render_template(
        "subject.html",
    return redirect(url_for("login"))
        subject=subject,

    return redirect(url_for("login"))

        student_name=session[
    return redirect(url_for("login"))
        ]
    )
    return redirect(url_for("login"))

# =========================================================
    return redirect(url_for("login"))
# =========================================================

    return redirect(url_for("login"))
def results():

    return redirect(url_for("login"))
        return redirect(
            url_for("login")
    return redirect(url_for("login"))

    conn = get_db()
    return redirect(url_for("login"))

    # =====================================================
    return redirect(url_for("login"))
    # =====================================================

    return redirect(url_for("login"))
        """
        CREATE TABLE IF NOT EXISTS results (
    return redirect(url_for("login"))
            id INTEGER PRIMARY KEY AUTOINCREMENT,

    return redirect(url_for("login"))

            subject_id INTEGER,
    return redirect(url_for("login"))
            score INTEGER,

    return redirect(url_for("login"))

            percentage REAL,
    return redirect(url_for("login"))
            status TEXT
        )
    return redirect(url_for("login"))
    )

    return redirect(url_for("login"))


    return redirect(url_for("login"))
    # GET STUDENT RESULTS
    # =====================================================
    return redirect(url_for("login"))
    student_results = conn.execute(
        """
    return redirect(url_for("login"))
            results.*,
            subjects.name AS subject_name
    return redirect(url_for("login"))
        FROM results

    return redirect(url_for("login"))
        ON results.subject_id = subjects.id

    return redirect(url_for("login"))

        ORDER BY results.id DESC
    return redirect(url_for("login"))
        (
            session["student_id"],
    return redirect(url_for("login"))
    ).fetchall()

    return redirect(url_for("login"))


    return redirect(url_for("login"))
        "results.html",

    return redirect(url_for("login"))

        student_name=session[
    return redirect(url_for("login"))
        ],

    return redirect(url_for("login"))
            "registration_number"
        ]
    return redirect(url_for("login"))


    return redirect(url_for("login"))
# NOTES — SUBJECT LIST
# =========================================================
    return redirect(url_for("login"))
@app.route("/notes")
def notes():
    return redirect(url_for("login"))
    if "student_id" not in session:
        return redirect(
    return redirect(url_for("login"))
        )

    return redirect(url_for("login"))
        "notes.html",

    return redirect(url_for("login"))
            "student_name"
        ],
    return redirect(url_for("login"))
        registration_number=session[
            "registration_number"
    return redirect(url_for("login"))
    )

    return redirect(url_for("login"))
# =========================================================
# BIOLOGY NOTES
    return redirect(url_for("login"))

@app.route("/notes/biology")
    return redirect(url_for("login"))

    if "student_id" not in session:
    return redirect(url_for("login"))
            url_for("login")
        )
    return redirect(url_for("login"))
    return render_template(
        "biology.html",
    return redirect(url_for("login"))
        student_name=session[
            "student_name"
    return redirect(url_for("login"))

        registration_number=session[
    return redirect(url_for("login"))
        ]
    )
    return redirect(url_for("login"))

# =========================================================
    return redirect(url_for("login"))
# =========================================================

    return redirect(url_for("login"))
def biology_unit1():

    return redirect(url_for("login"))
        return redirect(
            url_for("login")
    return redirect(url_for("login"))

    return render_template(
    return redirect(url_for("login"))

        student_name=session[
    return redirect(url_for("login"))
        ],

    return redirect(url_for("login"))
            "registration_number"
        ]
    return redirect(url_for("login"))


    return redirect(url_for("login"))
# MATHEMATICS NOTES
# =========================================================
    return redirect(url_for("login"))
@app.route("/notes/mathematics")
def mathematics_notes():
    return redirect(url_for("login"))
    if "student_id" not in session:
        return redirect(
    return redirect(url_for("login"))
        )

    return redirect(url_for("login"))
        "mathematics.html",

    return redirect(url_for("login"))
            "student_name"
        ],
    return redirect(url_for("login"))
        registration_number=session[
            "registration_number"
    return redirect(url_for("login"))
    )

    return redirect(url_for("login"))
# =========================================================
# MATHEMATICS UNIT 1
    return redirect(url_for("login"))

@app.route("/notes/mathematics/unit1")
    return redirect(url_for("login"))

    if "student_id" not in session:
    return redirect(url_for("login"))
            url_for("login")
        )
    return redirect(url_for("login"))
    return render_template(
        "mathematics_unit1.html",
    return redirect(url_for("login"))
        student_name=session[
            "student_name"
    return redirect(url_for("login"))

        registration_number=session[
    return redirect(url_for("login"))
        ]
    )
    return redirect(url_for("login"))

# =========================================================
    return redirect(url_for("login"))
# =========================================================

    return redirect(url_for("login"))
def ranking():

    return redirect(url_for("login"))
        return redirect(
            url_for("login")
    return redirect(url_for("login"))

    conn = get_db()
    return redirect(url_for("login"))

    # =====================================================
    return redirect(url_for("login"))
    # =====================================================

    return redirect(url_for("login"))
        """
        CREATE TABLE IF NOT EXISTS results (
    return redirect(url_for("login"))
            id INTEGER PRIMARY KEY AUTOINCREMENT,

    return redirect(url_for("login"))

            subject_id INTEGER,
    return redirect(url_for("login"))
            score INTEGER,

    return redirect(url_for("login"))

            percentage REAL,
    return redirect(url_for("login"))
            status TEXT
        )
    return redirect(url_for("login"))
    )

    return redirect(url_for("login"))


    return redirect(url_for("login"))
    # RANKING DATA
    # =====================================================
    return redirect(url_for("login"))
    ranking_data = conn.execute(
        """
    return redirect(url_for("login"))

            students.full_name,
    return redirect(url_for("login"))
            students.registration_number,

    return redirect(url_for("login"))
            AS total_score,

    return redirect(url_for("login"))
            AS total_questions,

    return redirect(url_for("login"))
                SUM(results.score)
                * 100.0
    return redirect(url_for("login"))
                NULLIF(
                    SUM(results.total_questions),
    return redirect(url_for("login"))
                ),
                2
    return redirect(url_for("login"))
            AS percentage

    return redirect(url_for("login"))

        JOIN students
    return redirect(url_for("login"))

        GROUP BY students.id
    return redirect(url_for("login"))
        ORDER BY percentage DESC
        """
    return redirect(url_for("login"))

    conn.close()
    return redirect(url_for("login"))

    return render_template(
    return redirect(url_for("login"))

        ranking=ranking_data,
    return redirect(url_for("login"))
        student_name=session[
            "student_name"
    return redirect(url_for("login"))
    )

    return redirect(url_for("login"))
# =========================================================
# LOGOUT
    return redirect(url_for("login"))

@app.route("/logout")
    return redirect(url_for("login"))

    session.clear()
    return redirect(url_for("login"))
    return redirect(
        url_for("login")
    return redirect(url_for("login"))


    return redirect(url_for("login"))
# RUN SERVER
# =========================================================
    return redirect(url_for("login"))
if __name__ == "__main__":

    return redirect(url_for("login"))
        host="0.0.0.0",
        port=5000,
    return redirect(url_for("login"))
    )
