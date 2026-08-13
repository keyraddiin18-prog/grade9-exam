import sqlite3

DATABASE = "exam.db"


questions = [
    {
        "question": "Which one of the following sets is not a subset of {1, {2}, {1, 2}}?",
        "a": "{1}",
        "b": "{2}",
        "c": "{1, {2}}",
        "d": "{{1, 2}}",
        "answer": "B"
    },
    {
        "question": "If A = {0, {3}, 5, -4}, then which one of the following is true?",
        "a": "3 ∈ A",
        "b": "{5} ∈ A",
        "c": "5 ∈ A",
        "d": "{0, -4} ∈ A",
        "answer": "C"
    },
    {
        "question": "Which of the following is true?",
        "a": "0 ∈ ∅",
        "b": "{3, 4} ⊂ {3, 4, 5}",
        "c": "{1, 2, 3} ⊂ {1, 2, 3, 4}",
        "d": "7 ∈ {7}",
        "answer": "C"
    },
    {
        "question": "Which one of the following sets is not finite?",
        "a": "A = {x : x is an even integer lying between 2 and 10}",
        "b": "B = {x : x is a letter of the English alphabet}",
        "c": "C = {x : x is a student of St. Gabriel Secondary School}",
        "d": "D = {x : x is an integer less than 10}",
        "answer": "D"
    },
    {
        "question": "Let A = {1, {2,3}, 3} and B = {{1}, {3,2}, 3}. Then B − A is equal to:",
        "a": "{{3,2}}",
        "b": "{{1}}",
        "c": "{{1}, {3,2}}",
        "d": "{1}",
        "answer": "C"
    },
    {
        "question": "If A and B are two sets such that n(A) = 12, n(B) = 15 and n(A ∩ B) = 4, then n(A ∪ B) is equal to:",
        "a": "8",
        "b": "11",
        "c": "23",
        "d": "19",
        "answer": "C"
    },
    {
        "question": "The number of subsets of the set {x : x is an even integer and -1 < x < 3} is:",
        "a": "4",
        "b": "2",
        "c": "32",
        "d": "8",
        "answer": "A"
    },
    {
        "question": "In a given universal set U, let A and B be sets. The simplified form of (A ∪ B) ∩ (A′ ∪ B′)′ is:",
        "a": "∅",
        "b": "U",
        "c": "A ∪ B",
        "d": "A ∩ B",
        "answer": "D"
    },
    {
        "question": "If M = {x : −2 < x < 2}, where x is an integer, then M is:",
        "a": "{−1, 0, 1}",
        "b": "{x : −1 < x < 1, where x is a real number}",
        "c": "{x : x < 3, where x is a natural number}",
        "d": "{2, 3, 4}",
        "answer": "A"
    },
    {
        "question": "For two finite sets A and B, where A ⊂ B with n(A) = p and n(B) = q such that p < q, which relation is true?",
        "a": "n(A ∪ B) = p",
        "b": "n(A ∪ B) = q",
        "c": "n(A ∪ B) = p + q",
        "d": "n(A ∪ B) < q",
        "answer": "B"
    },
    {
        "question": "Let H = {∅, {{0,1}}}. Which of the following represents the power set of H?",
        "a": "{∅, {∅}, {{{0,1}}}, {∅, {{0,1}}}}",
        "b": "{∅, {{0,1}}, {∅, {0,1}}}",
        "c": "{∅, {0}, {1}, {0,1}}",
        "d": "{∅, {∅}, {0}, {1}, {0,1}}",
        "answer": "A"
    },
    {
        "question": "Given three sets X, Y, and Z, which statement is NOT true?",
        "a": "If X ∩ Y ≠ ∅ and X ∩ Z = ∅, then X ∩ Y ∩ Z = ∅",
        "b": "If X ∩ Y = Y, then Y ⊂ X",
        "c": "If X ∩ Y = ∅, then Y − X = Y",
        "d": "If X ∩ Y = ∅, then X − Y = X",
        "answer": "B"
    },
    {
        "question": "The number of proper subsets of a set with 7 elements is:",
        "a": "127",
        "b": "128",
        "c": "14",
        "d": "28",
        "answer": "A"
    },
    {
        "question": "If A = {x : x ∈ N and 1 ≤ x ≤ 20} and B = {x : x ∈ N, 1 ≤ x ≤ 20 and x is odd}, then A − B is:",
        "a": "{2,3,4,5,7,11,13,19}",
        "b": "∅",
        "c": "{2,4,6,...,20}",
        "d": "{2,4,6,...,18}",
        "answer": "C"
    },
    {
        "question": "Consider W = {1,1.1,1.2,1.3,...,1.9,2}, X = {0,1,2,3,...,9,10}, Y = {3/10,29/10,28/10,...,21/10,2/10}, and Z = {x : x ∈ N and x ≤ 10}. Which statement is true?",
        "a": "X = Z",
        "b": "X ~ Z",
        "c": "W = X",
        "d": "W ~ Y",
        "answer": "A"
    },
    {
        "question": "If E and F are two unequal sets and U is the corresponding universal set, which statement is true?",
        "a": "E ∩ ∅ = U",
        "b": "If E ⊂ F, then (E ∩ F) ∪ F = E",
        "c": "If E ⊂ F, then E ∪ F = E",
        "d": "E ∩ U = E",
        "answer": "D"
    },
    {
        "question": "Which one of the following pairs represents equal sets?",
        "a": "{x : x ∈ Z and (x²−4)(3−x)=0} and {x : x ∈ N and (4−x²)(x−3)=0}",
        "b": "{x : x is an even natural number} and {x : x is an odd natural number}",
        "c": "{6,12} and {3,9}",
        "d": "{x : x ∈ Z and 2 < x ≤ 3} and {x : x ∈ Z and 3 < x < 4}",
        "answer": "D"
    },
    {
        "question": "If A = {−1,0,1} and B = {−1,1}, then the Cartesian product A × B is:",
        "a": "{(−1,−1),(0,−1),(0,1),(1,1),(−1,1),(1,−1)}",
        "b": "{(−1,−1),(0,−1),(0,1),(1,1),(−1,1)}",
        "c": "{(−1,−1),(0,1),(1,1)}",
        "d": "{(−1,−1),(0,−1),(0,1),(1,1)}",
        "answer": "A"
    },
    {
        "question": "Which one of the following sets is equal to {x : x = 2n + 1, n ∈ Z}?",
        "a": "{...,−5,−3,−2,2,3,5,7,11,13,...}",
        "b": "R \\ {x : x = 2n, n ∈ Z}",
        "c": "{...,−6,−4,−2,0,2,4,6,...}",
        "d": "{...,−5,−3,−1,1,3,5,7,9,...}",
        "answer": "D"
    },
    {
        "question": "If B = {−2,−1,0,1,2} and A = {x+y : x ∈ B and y ∈ B}, then the list of all elements of A is:",
        "a": "{−4,−3,−2,−1,0,1,2,3,4}",
        "b": "{−2,−1,0,1,2}",
        "c": "{−3,−1,0,1,3}",
        "d": "{−3,−2,−1,0,1,2,3}",
        "answer": "A"
    },
    {
        "question": "Given three sets A, B, C and a universal set U, which one of the following is true?",
        "a": "A ∩ B ∩ C = A ∩ B ∩ C",
        "b": "A ∩ B ⊂ A",
        "c": "A ∩ B ∩ C′ = A ∩ B′ ∩ C′",
        "d": "A ∩ U = U",
        "answer": "B"
    },
    {
        "question": "Let set M contain 25 elements. Which of the following sets is equivalent to M?",
        "a": "{x : x is a natural number and x < 25}",
        "b": "{x : x is a natural number and x < 26}",
        "c": "{x : x is a natural number and x = 25}",
        "d": "{x : x is a natural number and x > 25}",
        "answer": "B"
    },
    {
        "question": "In a certain Ethiopian High School, 100 students are studying English, 85 students are studying French, and 35 students are studying both languages. How many students are studying at least one of the two foreign languages?",
        "a": "220",
        "b": "15",
        "c": "150",
        "d": "185",
        "answer": "C"
    }
]


conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# Find Mathematics subject
cursor.execute(
    "SELECT id FROM subjects WHERE name = ?",
    ("Mathematics",)
)

subject = cursor.fetchone()

if subject is None:
    print("❌ Mathematics subject not found!")
    print("Run setup_db.py first.")
    conn.close()
    exit()

subject_id = subject[0]

# Remove old Mathematics questions
cursor.execute(
    "DELETE FROM questions WHERE subject_id = ?",
    (subject_id,)
)

# Add new Mathematics questions
for q in questions:
    cursor.execute(
        """
        INSERT INTO questions
        (subject_id, question, option_a, option_b, option_c, option_d, correct_answer)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            subject_id,
            q["question"],
            q["a"],
            q["b"],
            q["c"],
            q["d"],
            q["answer"]
        )
    )

conn.commit()
conn.close()

print(f"✅ {len(questions)} Mathematics questions added successfully!")
