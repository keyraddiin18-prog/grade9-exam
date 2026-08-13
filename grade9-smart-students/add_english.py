import sqlite3

DB_NAME = "exam.db"

# ============================================================
# ENGLISH QUESTIONS — GRADE 9
# 50 QUESTIONS
# ============================================================

questions = [

# ------------------------------------------------------------
# PART I — COMMUNICATIVE ACTIVITIES
# ------------------------------------------------------------

{
    "question": """Abel: Why were you late for the flag ceremony?
Bontu: ___________________________.""",
    "a": "I will come early tomorrow",
    "b": "I helped my mother before coming",
    "c": "The ceremony is very important",
    "d": "I like flag ceremonies",
    "answer": "B"
},

{
    "question": """Muhe: I have had a headache since yesterday.
Robsen: ___________________________.""",
    "a": "Headache is very common in Ethiopia",
    "b": "I have a headache too",
    "c": "You should see a health worker",
    "d": "Yesterday was very busy",
    "answer": "C"
},

{
    "question": """Rosa: Can you help me with this math problem?
Bilen: ___________________________.""",
    "a": "Yes, let’s solve it together",
    "b": "Math is very difficult",
    "c": "I finished my homework",
    "d": "The problem is wrong",
    "answer": "A"
},

{
    "question": """Kume: Why should we keep our school compound clean?
Biftu: ___________________________.""",
    "a": "Because cleaning is boring",
    "b": "To avoid coming late",
    "c": "It helps protect our health and environment",
    "d": "Teachers like it",
    "answer": "C"
},

{
    "question": """Lata: Some students are cheating during the exam.
Kemal: ___________________________.""",
    "a": "I will join them",
    "b": "It is not my problem",
    "c": "We should inform the teacher",
    "d": "Exams are difficult",
    "answer": "C"
},

# ------------------------------------------------------------
# PART II — READING COMPREHENSION
# ------------------------------------------------------------

{
    "question": """READING PASSAGE:

The Grand Ethiopian Renaissance Dam (GERD) is a large-scale hydroelectric project constructed on the Blue Nile River in Ethiopia’s Benishangul-Gumuz Region. Launched in 2011, the project was designed to address Ethiopia’s rapidly growing demand for electricity and to support long-term national development. After more than a decade of construction and phased reservoir filling, the dam was officially completed and inaugurated in September 2025 by Prime Minister Abiy Ahmed, marking a historic milestone as Africa’s largest hydroelectric power station.

The GERD is equipped with 13 turbines and has an installed generation capacity of approximately 5,150 megawatts (MW), with a reservoir capable of storing up to 74 billion cubic meters of water. Remarkably, the project was largely financed through domestic resources, reflecting Ethiopia’s commitment to self-reliance despite regional disagreements over Nile water utilization. As a result, the dam has come to symbolize national unity, determination, and collective ambition.

Economically, the GERD is expected to transform Ethiopia’s energy sector by significantly expanding access to clean and renewable electricity. The increased power supply will meet domestic demand, support industrial growth, and accelerate urban development. Moreover, surplus electricity exports to neighboring countries are anticipated to generate foreign exchange earnings and strengthen regional economic cooperation.

Beyond its economic significance, the GERD has had a profound psychological and social impact on Ethiopians. In a country often associated with challenges, the dam stands as a powerful demonstration of what can be achieved through perseverance and cooperation. It has reinforced a renewed sense of national pride and optimism, particularly among young people, by embodying the vision of a self-sufficient and forward-looking Ethiopia capable of shaping its own future.

Question: Where is the Grand Ethiopian Renaissance Dam located?""",
    "a": "On the White Nile in Sudan",
    "b": "On the Blue Nile in Benishangul-Gumuz",
    "c": "On the Awash River in Oromia",
    "d": "On the Tekeze River in Tigray",
    "answer": "B"
},

{
    "question": """According to the passage about the GERD, when was the dam officially inaugurated?""",
    "a": "2011",
    "b": "2020",
    "c": "September 2025",
    "d": "August 2023",
    "answer": "C"
},

{
    "question": """According to the passage, what was the primary reason for constructing the GERD?""",
    "a": "To control flooding in neighboring countries",
    "b": "To meet Ethiopia’s growing energy needs",
    "c": "To improve irrigation systems",
    "d": "To attract foreign tourism",
    "answer": "B"
},

{
    "question": """What does the GERD mainly symbolize for Ethiopians?""",
    "a": "Political dominance",
    "b": "External dependence",
    "c": "National unity and self-reliance",
    "d": "Environmental exploitation",
    "answer": "C"
},

{
    "question": """How can the GERD practically support Ethiopia’s industrial growth?""",
    "a": "By reducing agricultural land",
    "b": "By increasing access to reliable electricity",
    "c": "By limiting regional cooperation",
    "d": "By discouraging urbanization",
    "answer": "B"
},

{
    "question": """Why is the GERD described as a symbol of self-reliance?""",
    "a": "Because it depends on foreign loans",
    "b": "Because it was mainly financed by domestic resources",
    "c": "Because it reduced Ethiopia’s population growth",
    "d": "Because it ended all regional disagreements",
    "answer": "B"
},

{
    "question": """How does the passage show Ethiopia’s progress through the GERD?""",
    "a": "By focusing only on environmental issues",
    "b": "By ignoring historical challenges",
    "c": "By presenting the dam as evidence of progress and capability",
    "d": "By emphasizing military strength",
    "answer": "C"
},

{
    "question": """Which title best summarizes the passage?""",
    "a": "Water Conflicts in the Nile Basin",
    "b": "GERD: A Symbol of Power and Progress",
    "c": "Foreign Aid and Ethiopian
