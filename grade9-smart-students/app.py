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


# =========================================================
# LOGIN
# =========================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        full_name = request.form.get(
            "full_name",
            ""
        ).strip()

        registration_number = request.form.get(
            "registration_number",
            ""
        ).strip()

        conn = get_db()

        student = conn.execute(
            """
            SELECT *
            FROM students
            WHERE full_name = ?
            AND registration_number = ?
            """,
            (
                full_name,
                registration_number
            )
        ).fetchone()

        conn.close()

        if student:

            session["student_id"] = student["id"]

            session["student_name"] = (
                student["full_name"]
            )

            session["registration_number"] = (
                student["registration_number"]
            )

            return redirect(
                url_for("student_dashboard")
            )

        return render_template(
            "login.html",
            error="Student name or registration number is incorrect."
        )

    return render_template("login.html")


# =========================================================
# STUDENT DASHBOARD
# =========================================================

@app.route("/student")
def student_dashboard():

    if "student_id" not in session:
        return redirect(
            url_for("login")
        )

    return render_template(
        "student.html",
        student_name=session["student_name"],
        registration_number=session[
            "registration_number"
        ]
    )


# =========================================================
# SUBJECTS
# =========================================================

@app.route("/subjects")
def subjects():

    if "student_id" not in session:
        return redirect(
            url_for("login")
        )

    conn = get_db()

    subjects_data = conn.execute(
        """
        SELECT *
        FROM subjects
        ORDER BY id
        """
    ).fetchall()

    conn.close()

    return render_template(
        "subjects.html",
        subjects=subjects_data,
        student_name=session["student_name"]
    )


# =========================================================
# SUBJECT / EXAM
# =========================================================

@app.route(
    "/subject/<int:subject_id>",
    methods=["GET", "POST"]
)
def subject_detail(subject_id):

    if "student_id" not in session:
        return redirect(
            url_for("login")
        )

    conn = get_db()

    # Get subject
    subject = conn.execute(
        """
        SELECT *
        FROM subjects
        WHERE id = ?
        """,
        (subject_id,)
    ).fetchone()

    # Subject not found
    if not subject:

        conn.close()

        return "Subject not found", 404

    # Get questions
    questions = conn.execute(
        """
        SELECT *
        FROM questions
        WHERE subject_id = ?
        ORDER BY id
        """,
        (subject_id,)
    ).fetchall()


    # =====================================================
    # SUBMIT EXAM
    # =====================================================

    if request.method == "POST":

        total_questions = len(questions)

        score = 0

        for question in questions:

            question_id = str(
                question["id"]
            )

            student_answer = request.form.get(
                f"question_{question_id}"
            )

            correct_answer = question[
                "correct_answer"
            ]

            if (
                student_answer
                and
                student_answer.upper()
                ==
                correct_answer.upper()
            ):
                score += 1


        # =================================================
        # PERCENTAGE
        # =================================================

        if total_questions > 0:

            percentage = (
                score / total_questions
            ) * 100

        else:

            percentage = 0


        # =================================================
        # QUALIFICATION
        # =================================================

        if percentage >= 55:

            status = "Qualified"

        else:

            status = "Not Qualified"


        # =================================================
        # CREATE RESULTS TABLE
        # =================================================

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS results (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                student_id INTEGER,

                subject_id INTEGER,

                score INTEGER,

                total_questions INTEGER,

                percentage REAL,

                status TEXT
            )
            """
        )


        # =================================================
        # SAVE RESULT
        # =================================================

        conn.execute(
            """
            INSERT INTO results
            (
                student_id,
                subject_id,
                score,
                total_questions,
                percentage,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                session["student_id"],
                subject_id,
                score,
                total_questions,
                percentage,
                status
            )
        )

        conn.commit()

        conn.close()


        # =================================================
        # RESULT PAGE
        # =================================================

        return render_template(
            "result.html",

            subject=subject,

            score=score,

            total_questions=total_questions,

            percentage=round(
                percentage,
                2
            ),

            status=status,

            student_name=session[
                "student_name"
            ],

            registration_number=session[
                "registration_number"
            ]
        )


    # Close database for GET
    conn.close()


    # =====================================================
    # EXAM PAGE
    # =====================================================

    return render_template(
        "subject.html",

        subject=subject,

        questions=questions,

        student_name=session[
            "student_name"
        ]
    )


# =========================================================
# MY RESULTS
# =========================================================

@app.route("/results")
def results():

    if "student_id" not in session:
        return redirect(
            url_for("login")
        )

    conn = get_db()


    # =====================================================
    # CREATE RESULTS TABLE
    # =====================================================

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS results (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            student_id INTEGER,

            subject_id INTEGER,

            score INTEGER,

            total_questions INTEGER,

            percentage REAL,

            status TEXT
        )
        """
    )

    conn.commit()


    # =====================================================
    # GET STUDENT RESULTS
    # =====================================================

    student_results = conn.execute(
        """
        SELECT
            results.*,
            subjects.name AS subject_name

        FROM results

        LEFT JOIN subjects
        ON results.subject_id = subjects.id

        WHERE results.student_id = ?

        ORDER BY results.id DESC
        """,
        (
            session["student_id"],
        )
    ).fetchall()

    conn.close()


    return render_template(
        "results.html",

        results=student_results,

        student_name=session[
            "student_name"
        ],

        registration_number=session[
            "registration_number"
        ]
    )


# =========================================================
# NOTES — SUBJECT LIST
# =========================================================

@app.route("/notes")
def notes():

    if "student_id" not in session:
        return redirect(
            url_for("login")
        )

    return render_template(
        "notes.html",

        student_name=session[
            "student_name"
        ],

        registration_number=session[
            "registration_number"
        ]
    )


# =========================================================
# BIOLOGY NOTES
# =========================================================

@app.route("/notes/biology")
def biology_notes():

    if "student_id" not in session:
        return redirect(
            url_for("login")
        )

    return render_template(
        "biology.html",

        student_name=session[
            "student_name"
        ],

        registration_number=session[
            "registration_number"
        ]
    )


# =========================================================
# BIOLOGY UNIT 1
# =========================================================

@app.route("/notes/biology/unit1")
def biology_unit1():

    if "student_id" not in session:
        return redirect(
            url_for("login")
        )

    return render_template(
        "biology_unit1.html",

        student_name=session[
            "student_name"
        ],

        registration_number=session[
            "registration_number"
        ]
    )


# =========================================================
# MATHEMATICS NOTES
# =========================================================

@app.route("/notes/mathematics")
def mathematics_notes():

    if "student_id" not in session:
        return redirect(
            url_for("login")
        )

    return render_template(
        "mathematics.html",

        student_name=session[
            "student_name"
        ],

        registration_number=session[
            "registration_number"
        ]
    )


# =========================================================
# MATHEMATICS UNIT 1
# =========================================================

@app.route("/notes/mathematics/unit1")
def mathematics_unit1():

    if "student_id" not in session:
        return redirect(
            url_for("login")
        )

    return render_template(
        "mathematics_unit1.html",

        student_name=session[
            "student_name"
        ],

        registration_number=session[
            "registration_number"
        ]
    )


# =========================================================
# RANKING / PROGRESS
# =========================================================

@app.route("/ranking")
def ranking():

    if "student_id" not in session:
        return redirect(
            url_for("login")
        )

    conn = get_db()


    # =====================================================
    # CREATE RESULTS TABLE
    # =====================================================

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS results (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            student_id INTEGER,

            subject_id INTEGER,

            score INTEGER,

            total_questions INTEGER,

            percentage REAL,

            status TEXT
        )
        """
    )

    conn.commit()


    # =====================================================
    # RANKING DATA
    # =====================================================

    ranking_data = conn.execute(
        """
        SELECT

            students.full_name,

            students.registration_number,

            SUM(results.score)
            AS total_score,

            SUM(results.total_questions)
            AS total_questions,

            ROUND(
                SUM(results.score)
                * 100.0
                /
                NULLIF(
                    SUM(results.total_questions),
                    0
                ),
                2
            )
            AS percentage

        FROM results

        JOIN students
        ON results.student_id = students.id

        GROUP BY students.id

        ORDER BY percentage DESC
        """
    ).fetchall()

    conn.close()


    return render_template(
        "ranking.html",

        ranking=ranking_data,

        student_name=session[
            "student_name"
        ]
    )


# =========================================================
# LOGOUT
# =========================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("login")
    )


# =========================================================
# RUN SERVER
# =========================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
