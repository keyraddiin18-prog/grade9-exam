import sqlite3

students = [
    "Sharaddiin Mahammad",
    "Kalid Abdii",
    "Anas Xaha",
    "Ramadan",
    "Ibsaa Mayyuu",
    "Leello Umar",
    "Anas Mahammad",
    "Mahammad Ramadan",
    "Seyfaddiin Mahammad",
    "Common"
]

conn = sqlite3.connect("exam.db")

for i, name in enumerate(students, start=1):
    registration_number = f"G9-{i:03d}"

    conn.execute(
        """
        INSERT OR IGNORE INTO students
        (registration_number, full_name)
        VALUES (?, ?)
        """,
        (registration_number, name)
    )

conn.commit()
conn.close()

print("10 students added successfully!")
