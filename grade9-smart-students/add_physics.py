import sqlite3

conn = sqlite3.connect("exam.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL,
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
)
""")

cursor.execute("SELECT id FROM subjects WHERE name = 'Physics'")
subject = cursor.fetchone()

if not subject:
    print("❌ Physics subject not found!")
    conn.close()
    exit()

physics_id = subject[0]

questions = [
    (
        "The Greek word 'phusis' for nature is appropriate in describing the field of physics. Which is the best answer?",
        "Physics studies life and living organisms.",
        "Physics studies the laws and principles of our universe.",
        "Physics studies social behavior.",
        "Physics studies only changes in living organisms.",
        "B"
    ),
    (
        "A moving car suddenly comes to a rest after applying brakes. Which branch of physics explains this?",
        "Mechanics",
        "Acoustics",
        "Electromagnetism",
        "Nuclear physics",
        "A"
    ),
    (
        "Which of the following is NOT one of the branches of physics?",
        "Thermodynamics",
        "Optics",
        "Classical physics",
        "Evolution",
        "D"
    ),
    (
        "Which of the following is not a historical contributor in physics?",
        "Willebrod Snell",
        "Daniel Bernoulli",
        "Thomas Young",
        "Charles Darwin",
        "D"
    ),
    (
        "Which branch of Physics is most important when studying the nature and behavior of light?",
        "Quantum Mechanics",
        "Nuclear Physics",
        "Optics",
        "Thermodynamics",
        "C"
    ),
    (
        "Galileo's famous experiment at the leaning tower of Pisa demonstrated that:",
        "What goes up must come down.",
        "All objects fall to Earth at the same rate, regardless of their mass.",
        "Heavier objects fall faster.",
        "Gravity does not act on falling objects.",
        "B"
    ),
    (
        "Which branch of Physics is most important when studying how air conditioners cool your house?",
        "Mechanics",
        "Optics",
        "Thermodynamics",
        "Electromagnetism",
        "C"
    ),
    (
        "Which branch of Physics is most important when studying how glasses help people see?",
        "Mechanics",
        "Optics",
        "Thermodynamics",
        "Electromagnetism",
        "B"
    ),
    (
        "Which branch of Physics is most important when determining how much voltage is produced by a wind turbine?",
        "Mechanics",
        "Waves and Wave mechanics",
        "Relativity",
        "Electromagnetism",
        "D"
    ),
    (
        "Which branch of Physics studies the motion of everyday objects like a car or bowling ball?",
        "Mechanics",
        "Optics",
        "Thermodynamics",
        "Electromagnetism",
        "A"
    ),
    (
        "Which branch of Physics is most important when discussing the motion of sub-atomic particles?",
        "Quantum Mechanics",
        "Waves and Wave mechanics",
        "Relativity",
        "Electromagnetism",
        "A"
    ),
    (
        "Which branch of Physics is most important when studying the results of a car crash?",
        "Mechanics",
        "Waves and Wave mechanics",
        "Relativity",
        "Electromagnetism",
        "A"
    ),
    (
        "Which branch of Physics studies highly ionized gases?",
        "Mechanics",
        "Acoustics",
        "Plasma Physics",
        "Atomic and Nuclear Physics",
        "C"
    ),
    (
        "Which branch of Physics studies the production and properties of sound?",
        "Optics",
        "Mechanics",
        "Acoustics",
        "Quantum Physics",
        "C"
    ),
    (
        "Which branch of Physics studies heat and other forms of energy and their conversion?",
        "Plasma Physics",
        "Quantum Physics",
        "Atomic and Nuclear Physics",
        "Thermodynamics",
        "D"
    ),
    (
        "Which branch of Physics is concerned with forces between electrically charged particles?",
        "Quantum Physics",
        "Electromagnetism",
        "Mechanics",
        "Acoustics",
        "B"
    ),
    (
        "Which branch of Physics deals with the structure of the atomic nucleus and nuclear reactions?",
        "Plasma Physics",
        "Atomic and Nuclear Physics",
        "Thermodynamics",
        "Relativity Physics",
        "B"
    ),
    (
        "The branch of Physics known as Mechanics deals with:",
        "Motors and generators",
        "Forces and the behavior of objects",
        "Heat, temperature and energy",
        "Electricity and magnetism",
        "B"
    ),
    (
        "Which outstanding contribution in Physics is associated with Newton?",
        "Universal gravitational law",
        "Laws of Motion",
        "Discovery of Calculus",
        "All of the above",
        "D"
    )
]

cursor.executemany("""
INSERT INTO questions
(subject_id, question, option_a, option_b, option_c, option_d, correct_answer)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", [
    (physics_id, q, a, b, c, d, answer)
    for q, a, b, c, d, answer in questions
])

conn.commit()

print(f"✅ {len(questions)} Physics questions added successfully!")

conn.close()
