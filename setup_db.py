import sqlite3

conn = sqlite3.connect("exam.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    registration_number TEXT UNIQUE NOT NULL,
    full_name TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database table created successfully!")

