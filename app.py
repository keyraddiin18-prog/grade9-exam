from flask import Flask, send_file, request, jsonify
import sqlite3

app = Flask(__name__)

DB_NAME = "exam.db"


def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return send_file("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "No data received"
        }), 400

    registration_number = data.get("registration_number", "").strip()
    full_name = data.get("full_name", "").strip()

    mathematics = int(data.get("mathematics", 0))
    science = int(data.get("science", 0))
    afaan_oromoo = int(data.get("afaan_oromoo", 0))
    english = int(data.get("english", 0))

    if not registration_number or not full_name:
        return jsonify({
            "success": False,
            "message": "Full name and registration number are required."
        }), 400

    total = (
        mathematics
        + science
        + afaan_oromoo
        + english
    )

    percentage = (total / 80) * 100

    status = "Qualified" if total >= 64 else "Not Qualified"

    conn = get_db()

    # Check whether this student already submitted
    existing = conn.execute(
        "SELECT id FROM results WHERE registration_number = ?",
        (registration_number,)
    ).fetchone()

    if existing:
        conn.execute(
            """
            UPDATE results
            SET full_name = ?,
                mathematics = ?,
                science = ?,
                afaan_oromoo = ?,
                english = ?,
                total = ?,
                percentage = ?,
                status = ?
            WHERE registration_number = ?
            """,
            (
                full_name,
                mathematics,
                science,
                afaan_oromoo,
                english,
                total,
                percentage,
                status,
                registration_number
            )
        )
    else:
        conn.execute(
            """
            INSERT INTO results
            (
                registration_number,
                full_name,
                mathematics,
                science,
                afaan_oromoo,
                english,
                total,
                percentage,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                registration_number,
                full_name,
                mathematics,
                science,
                afaan_oromoo,
                english,
                total,
                percentage,
                status
            )
        )

    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "registration_number": registration_number,
        "full_name": full_name,
        "mathematics": mathematics,
        "science": science,
        "afaan_oromoo": afaan_oromoo,
        "english": english,
        "total": total,
        "percentage": round(percentage, 2),
        "status": status
    })


@app.route("/results")
def results():
    conn = get_db()

    rows = conn.execute(
        """
        SELECT
            registration_number,
            full_name,
            mathematics,
            science,
            afaan_oromoo,
            english,
            total,
            percentage,
            status
        FROM results
        ORDER BY total DESC
        """
    ).fetchall()

    conn.close()

    return jsonify([dict(row) for row in rows])


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
