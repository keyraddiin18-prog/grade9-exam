import sqlite3

DB_NAME = "exam.db"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    registration_number TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Subjects table
cursor.execute("""
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)
""")

# Add students
students = [
    ("Sharaddiin Mahammad", "G9-001"),
    ("Kalid Abdii", "G9-002"),
    ("Ramadan Jamaal", "G9-003"),
    ("Ibsaa Mayyuu", "G9-004"),
    ("Ansara Mayyuu", "G9-005"),
    ("Anas Xaha", "G9-006"),
    ("Nurse Turkii", "G9-007"),
    ("Furqaa Mahammad", "G9-008"),
    ("Milkoo Umar", "G9-009"),
    ("Caalaa Mahammad", "G9-010"),
    ("Zahir Mahammad", "G9-011")
]

cursor.executemany("""
INSERT OR IGNORE INTO students
(full_name, registration_number)
VALUES (?, ?)
""", students)

# Add subjects
subjects = [
    "Mathematics",
    "Physics",
    "Biology",
    "Chemistry",
    "Afaan Oromoo",
    "English"
]

cursor.executemany("""
INSERT OR IGNORE INTO subjects (name)
VALUES (?)
""", [(subject,) for subject in subjects])

conn.commit()
conn.close()

print("✅ Students and subjects added successfully!")
