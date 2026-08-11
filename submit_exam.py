import sqlite3
from exam_data import ANSWER_KEY

PASS_MARK = 64


def calculate_score(subject, answers):
    correct_answers = ANSWER_KEY[subject]
    score = 0

    for i, correct in enumerate(correct_answers):
        if i < len(answers) and answers[i].upper() == correct.upper():
            score += 1

    return score


def save_result(registration_number, full_name, scores):
    total = sum(scores.values())
    percentage = (total / 80) * 100
    status = "Qualified" if total >= PASS_MARK else "Not Qualified"

    conn = sqlite3.connect("exam.db")

    conn.execute(
        """
        INSERT INTO results
        (registration_number, full_name,
         mathematics, science, afaan_oromoo, english,
         total, percentage, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            registration_number,
            full_name,
            scores["mathematics"],
            scores["science"],
            scores["afaan_oromoo"],
            scores["english"],
            total,
            percentage,
            status
        )
    )

    conn.commit()
    conn.close()

    return {
        "registration_number": registration_number,
        "full_name": full_name,
        "mathematics": scores["mathematics"],
        "science": scores["science"],
        "afaan_oromoo": scores["afaan_oromoo"],
        "english": scores["english"],
        "total": total,
        "percentage": percentage,
        "status": status
    }


if __name__ == "__main__":
    print("Exam scoring system is ready!")
