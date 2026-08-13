# add_chemistry.py
# Add Grade 9 Chemistry questions to exam.db

import sqlite3

DB_NAME = "exam.db"

# ---------------------------------------------------------
# CHEMISTRY QUESTIONS
# Format:
# (question, option_a, option_b, option_c, option_d, answer)
# ---------------------------------------------------------

questions = [
    (
        "Which sentence is not true about matter?",
        "Anything that can be weighed and takes up space is considered matter",
        "Size, shape, and color are properties of matter",
        "Light from the Sun is matter",
        "Everything we see and touch is matter",
        "C"
    ),
    (
        "Which of the following is not correctly matched?",
        "Inorganic chemistry - Study all the elements and their compounds with the exception of carbon and its compounds",
        "Organic chemistry - Chemistry of carbon compounds except carbides, cyanides, carbon dioxide, carbon monoxide, carbonates and hydrogen carbonates",
        "Physical chemistry - Study physical properties of materials, such as their thermal, electrical and magnetic behavior",
        "Analytical chemistry - Focuses on the investigation of chemical reactions occurring within biological systems",
        "D"
    ),
    (
        "Chemicals that kill insects and other pests that harm crops and affect the yield are called:",
        "Fertilizers",
        "Pesticides",
        "Weedicides",
        "Preservatives",
        "B"
    ),
    (
        "Chemistry plays the following important roles in agriculture EXCEPT:",
        "Chemistry has helped to increase crop production through fertilizers",
        "Pest control",
        "Plastic pipes for improved irrigation",
        "The use of pesticides increases the effect of pests on crops by ten percent",
        "D"
    ),
    (
        "The sanitizers we use for Covid-19 belong to the group:",
        "Disinfectants",
        "Analgesics",
        "Anesthetics",
        "Antibiotics",
        "A"
    ),
    (
        "Which of the following is used to control infection and cure diseases?",
        "Tranquillizers",
        "Antiseptics",
        "Antibiotics",
        "Anesthetics",
        "C"
    ),
    (
        "Which pair of industry and chemical products is not correctly matched?",
        "Ziway Caustic Soda factory - Sodium hydroxide",
        "Chorra Gas and Chemical products - Plastic, chemicals, petroleum products",
        "Nefas Silk Paints factory - Detergent products and Leather chemical inputs",
        "Adami Tulu Pesticide Processing Plant - Formulates malathion, endosulfan, diazinon, fenitrothion and dimethoate",
        "C"
    ),
    (
        "The length of the carbon-oxygen bond in carbon dioxide is 116.3 pm. What is the distance in centimeters?",
        "1.163 × 10^-7 cm",
        "1.163 × 10^-10 cm",
        "1.163 × 10^-8 cm",
        "1.163 × 10^-11 cm",
        "A"
    ),
    (
        "Which instrument is NOT used to measure the volume of a liquid?",
        "Measuring cylinder",
        "Burette",
        "Meter stick",
        "Pipette",
        "C"
    ),
    (
        "The average temperature in Addis Ababa during summer is about 25°C. What is the equivalent temperature in Fahrenheit?",
        "13°F",
        "77°F",
        "45.9°F",
        "18.11°F",
        "B"
    ),
    (
        "What is the symbol of the SI unit of amount of substance?",
        "mol",
        "cd",
        "A",
        "s",
        "A"
    ),
    (
        "Which statement is incorrect about heat and temperature?",
        "Temperature is a measure of the average kinetic energy of particles in a system",
        "The instrument used for measuring temperature is a thermometer",
        "Heat always flows spontaneously from a colder body to a hotter body",
        "Temperature tells us in what direction heat flows",
        "C"
    ),
    (
        "Which of the following statements is not correct?",
        "Volume has no units",
        "Every measurement has a unit tied to it",
        "Physical quantities are properties that can be measured",
        "Every Kelvin temperature is 273.15 units above the corresponding Celsius temperature",
        "A"
    ),
    (
        "Pick the fundamental physical quantity from the following:",
        "Volume",
        "Density",
        "Length",
        "Pressure",
        "C"
    ),
    (
        "Which statement is incorrect about the given physical quantities?",
        "Density of an object is its mass per unit volume",
        "Volume is the amount of space occupied by a solid, liquid or gas",
        "A mole of any substance represents 6.023 × 10^23 particles of that substance",
        "Pressure is work per unit area over which the energy is exerted",
        "D"
    ),
    (
        "Which of the following is NOT a systematic uncertainty?",
        "Reaction time",
        "Inaccurate meter stick",
        "Miscalibrated balance",
        "Unpredictable fluctuations in experimental condition",
        "D"
    ),
    (
        "Which one of the following is incorrect about uncertainty in measurements?",
        "Systematic uncertainty produces values that are either entirely higher or smaller than the actual value",
        "Systematic uncertainty always affects a result in a particular direction",
        "Random uncertainties are variations in measurements that occur without a predictable pattern",
        "Random uncertainty can be eliminated easily",
        "D"
    ),
    (
        "Which of the following statements is correct?",
        "Precision refers to the closeness of a single measurement to its true value",
        "Accuracy refers to the closeness of the set of values obtained from identical measurements",
        "It is possible to have precise measurements which are not accurate",
        "Accuracy and precision are the same thing",
        "C"
    ),
    (
        "The numbers 2.7450 and 2.73514, when rounded off to three significant figures respectively, give:",
        "2.75 and 2.74",
        "2.74 and 2.73",
        "2.75 and 2.73",
        "2.74 and 2.74",
        "A"
    ),
    (
        "The sum of 436.32, 227.2 and 0.301 in appropriate significant figures is:",
        "663.821",
        "664",
        "663.8",
        "663.82",
        "C"
    ),
    (
        "A temperature reading of 75.6°C has an absolute uncertainty of 0.2°C. Calculate the percent uncertainty.",
        "0.3%",
        "0.1%",
        "0.4%",
        "0.5%",
        "A"
    ),
    (
        "Which example illustrates a number correctly rounded to three significant figures?",
        "4.05438 grams to 4.054 grams",
        "0.03954 grams to 0.040 grams",
        "20.0332 grams to 20.0 grams",
        "103.692 grams to 103.7 grams",
        "B"
    ),
    (
        "In the four representative dart patterns, which statement is incorrect?",
        "A set of measurements that is neither precise nor accurate - (a)",
        "An accurate but imprecise set of measurements - (b)",
        "A set of measurements that is both precise and accurate - (d)",
        "An accurate but not precise set of measurements - (c)",
        "D"
    ),
    (
        "A sample has an accepted value of 8.72 g. Student A records 8.72, 8.74 and 8.70 g; B records 8.50, 8.77 and 8.83 g; C records 8.50, 8.48 and 8.51 g; D records 8.41, 8.72 and 8.55 g. Which statement is NOT true?",
        "Student A was the most accurate",
        "Student C was the most precise",
        "Student C gave the least accurate data",
        "Student B was the most precise",
        "D"
    ),
    (
        "The area of a rectangle with length 5.6 cm and width 9.24 cm is:",
        "50 cm²",
        "51.7 cm²",
        "51.74 cm²",
        "52 cm²",
        "B"
    ),
    (
        "Which of the following is incorrect?",
        "0.00000075 has 2 significant figures",
        "37.300 has 3 significant figures",
        "33.00000 has 7 significant figures",
        "7,004 has 4 significant figures",
        "B"
    ),

    # Question 27 was omitted because the calculation/formula was missing
    # from the supplied text.

    (
        "Some alpha-rays are deflected through acute and obtuse angles due to the presence of ______ in the center of the atom.",
        "Positive charge",
        "Negative charge",
        "Neutral charge",
        "Neutron",
        "A"
    ),
    (
        "What is 100 decimeters expressed in centimeters?",
        "100 cm",
        "10 cm",
        "1000 cm",
        "10,000 cm",
        "C"
    ),
    (
        "Which distance measurement below is the longest?",
        "795 µm",
        "45,000 nm",
        "84.3 cm",
        "1,100 mm",
        "D"
    ),
    (
        "The speed of X-rays is 300,000 m/s. The scientific notation with the correct 3 significant figures is:",
        "3.000 × 10^5 m/s",
        "3.00 × 10^5 m/s",
        "3.0000 × 10^5 m/s",
        "300 × 10^4 m/s",
        "B"
    ),
    (
        "Which of the following does NOT allow you to give an exact number when you measure it?",
        "The number of pages in a Grade 9 Chemistry textbook",
        "The number of microseconds in a week",
        "The surface area of a coin",
        "The number of grams in one kilogram",
        "C"
    ),
    (
        "The major skill that is NOT developed in a laboratory environment is:",
        "Skills in the operation of standard chemical instrumentation",
        "Skills in the safe handling of chemical materials",
        "Skills required for conducting standard laboratory procedures",
        "Skills of sucking solutions into a pipette by mouth",
        "D"
    ),
    (
        "Which statement is NOT correct about the scientific method?",
        "Observation and formulation of a question is the first step",
        "A hypothesis may be expressed as a cause-and-effect statement",
        "After a hypothesis is made, there is no need to test it",
        "If analyzed data are consistent with the hypothesis, it may be accepted",
        "C"
    ),
    (
        "Which is the major point of atomic idea according to Greek philosophers?",
        "All matter is composed of atoms",
        "There is no void, which is an empty space between atoms",
        "Atoms are completely liquid",
        "Atoms are heterogeneous, with no internal structure",
        "A"
    ),
    (
        "Which one of the following is false?",
        "Laws are generalized observations about relationships in the natural world",
        "Scientific laws are statements based on repeated experiments or observations",
        "Chemical laws are laws of nature relevant to chemistry",
        "Antoine Lavoisier discovered the law of conservation of energy",
        "D"
    ),
    (
        "The number of electrons present in the valence shell of an atom with atomic number 20 is:",
        "1",
        "2",
        "3",
        "4",
        "B"
    ),
    (
        "Every chemical compound contains fixed and constant proportions by mass of its constituent elements. This is:",
        "The law of conservation of energy",
        "Scientific laws",
        "The Law of definite proportions",
        "The law of conservation of mass",
        "C"
    ),
    (
        "Which is false about Dalton's atomic theory?",
        "Elements are made of small particles called atoms",
        "Atoms can neither be created nor destroyed",
        "All atoms of the same element are different and have the same mass and size",
        "Atoms of different elements have different masses and sizes",
        "C"
    ),
    (
        "What is the similarity between Dalton's and Modern atomic theories?",
        "Atom is the smallest unit of matter that takes part in a chemical reaction",
        "Matter consists of small indivisible particles called atoms",
        "Atoms of the same element are alike in all respects",
        "Atoms of different elements are different in all respects",
        "A"
    ),
    (
        "Anode rays or canal rays:",
        "Were found in a stream of neutral particles in contrast to cathode rays",
        "Are neutrons",
        "Travel in straight lines",
        "Are deflected in electric and magnetic fields in the same way as cathode rays",
        "C"
    ),
    (
        "The second experiment using a light paddlewheel between the cathode and anode to study the particulate nature of cathode rays was performed by:",
        "Rutherford",
        "James Chadwick",
        "Bohr",
        "J. J. Thomson",
        "D"
    ),
    (
        "Millikan's oil drop experiment determined:",
        "Balancing of water drops",
        "Uniformly distributed positive charge",
        "The charge of an electron",
        "Electrons embedded in positive matter",
        "C"
    ),
    (
        "Which one of the following is false?",
        "Rutherford discovered the nucleus",
        "Goldstein discovered electrons in the discharge tube experiment",
        "The proton is located at the center of the atom",
        "The electron is located in the extranuclear part",
        "B"
    ),
    (
        "Bohr's atomic model explains:",
        "Specified paths of electrons around the nucleus",
        "A variable amount of energy in every orbit",
        "Decrease in orbital energy with increasing distance from the nucleus",
        "No change in electron energy when moving from one orbit to another",
        "A"
    ),
    (
        "Which statement is false?",
        "According to Thomson's atomic model, electrons revolve around the nucleus",
        "In a discharge tube, anode rays originate when electrons collide with gas",
        "Alpha-ray scattering experiment proved that positive particles are present in the extranuclear part of an atom",
        "The energy of an electron in the first orbit is less than that in the other orbits",
        "A"
    ),
    (
        "Silicon has mass number 28 and atomic number 14. What are its proton and neutron numbers?",
        "28 and 14",
        "28 and 28",
        "14 and 28",
        "14 and 14",
        "D"
    ),
    (
        "Rutherford's alpha-particle scattering experiment eventually led to the conclusion that:",
        "Mass and energy are related",
        "The point of impact with matter can be precisely determined",
        "Neutrons are buried deep in the nucleus",
        "Electrons are distributed in a large space around the nucleus",
        "D"
    ),
    (
        "Which concept was NOT considered in Rutherford's atomic model?",
        "The electrical neutrality of an atom",
        "The quantization of energy",
        "Electrons revolve around the nucleus at very high speeds",
        "The existence of nuclear forces of attraction on electrons",
        "B"
    ),
    (
        "An element has two isotopes with mass numbers 16 and 18. Its average atomic mass is 16.5. The percentage abundance of the isotopes 16 and 18 respectively is:",
        "25%, 75%",
        "50%, 50%",
        "75%, 25%",
        "33.33%, 66.67%",
        "C"
    ),
    (
        "When alpha particles are sent through a thin metal foil, only one out of ten thousand is rebounded. This observation led to the conclusion that:",
        "Positive charge is concentrated at the center of the atom",
        "More electrons are revolving around the nucleus",
        "Unit positive charge is only present in an atom",
        "A massive sphere with negative charge and unit positive charge is at the center",
        "A"
    ),
    (
        "In which pair of shells is the energy difference between two adjacent orbits minimum?",
        "L, M",
        "M, N",
        "N, O",
        "K, L",
        "C"
    ),
    (
        "Some elements have fractional atomic masses. The reason could be:",
        "The existence of isobars",
        "Nuclear reactions",
        "The existence of isotopes",
        "The presence of neutrons in the nucleus",
        "C"
    ),
    (
        "Which one of the following is false?",
        "Atoms are the tiniest particles of matter that take part in chemical reactions",
        "Atoms of the same element are the same",
        "Atoms are composed of electrons and a nucleus",
        "The nucleus consists of a positively charged proton and a negatively charged neutron",
        "D"
    ),
    (
        "Which is true about the fundamental particles of an atom?",
        "The masses of protons and neutrons are fairly similar, although the neutron is slightly heavier than the proton",
        "Electrons have a charge of -1 and protons also have a charge of -1",
        "Neutrons are neither attracted to nor repelled by charged objects",
        "The mass of an atom depends only on the mass of protons and electrons",
        "A"
    ),
    (
        "Calculate the average atomic mass of copper: Cu-63, 69.15% and Cu-65, 30.85%.",
        "43.56",
        "20.05",
        "63.61",
        "83.61",
        "C"
    ),
    (
        "How many main energy levels does calcium (Ca) have?",
        "One",
        "Two",
        "Three",
        "Four",
        "D"
    ),
    (
        "Write the electronic configuration of potassium (K), atomic number = 19.",
        "2, 8, 9",
        "2, 8, 8, 1",
        "2, 7, 9, 1",
        "2, 7, 8, 2",
        "B"
    ),
    (
        "In an element that has isotopes, which subatomic particles are different while others remain unchanged?",
        "Neutrons are different while electrons and protons remain unchanged",
        "Neutrons are the same while electrons and protons remain unchanged",
        "Neutrons are different while electrons and protons also change",
        "Neutrons are the same while electrons and protons change",
        "A"
    ),
    (
        "What is the main energy level of an electron?",
        "The shell or orbital in which the electron is located relative to the atom's mass number",
        "The shell or energy level in which the electron is located relative to the atom's nucleus",
        "The shell in which the proton is located relative to the atom's mass number",
        "The shell in which the neutron is located relative to the atom's nucleus",
        "B"
    ),
]


def get_subject_id(conn):
    """Find the Mathematics/Physics-style subject table and Chemistry subject ID."""
    cur = conn.cursor()

    # First try the expected subjects table.
    cur.execute(
        "SELECT id FROM subjects WHERE LOWER(name)=LOWER(?) LIMIT 1",
        ("Chemistry",)
    )
    row = cur.fetchone()

    if row:
        return row[0]

    # If Chemistry does not exist, create it.
    cur.execute(
        "INSERT INTO subjects (name) VALUES (?)",
        ("Chemistry",)
    )
    conn.commit()
    return cur.lastrowid


def get_question_columns(conn):
    """
    Detect the question table structure.
    The project normally uses:
    question, option_a, option_b, option_c, option_d, correct_answer, subject_id
    """
    cur = conn.cursor()
    cur.execute("PRAGMA table_info(questions)")
    columns = [row[1] for row in cur.fetchall()]

    return columns


def add_questions():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    try:
        subject_id = get_subject_id(conn)
        columns = get_question_columns(conn)

        print("Questions table columns:")
        print(columns)

        # Expected project structure.
        required = {
            "subject_id",
            "question",
            "option_a",
            "option_b",
            "option_c",
            "option_d",
            "correct_answer",
        }

        missing = required - set(columns)

        if missing:
            print("\n❌ Missing columns in questions table:")
            print(missing)
            print("\nCheck your existing database schema before running this script.")
            return

        added = 0
        skipped = 0

        for q, a, b, c, d, answer in questions:

            # Prevent duplicate questions in Chemistry.
            cur.execute(
                """
                SELECT id
                FROM questions
                WHERE subject_id = ?
                  AND question = ?
                LIMIT 1
                """,
                (subject_id, q)
            )

            if cur.fetchone():
                skipped += 1
                continue

            cur.execute(
                """
                INSERT INTO questions
                (
                    subject_id,
                    question,
                    option_a,
                    option_b,
                    option_c,
                    option_d,
                    correct_answer
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    subject_id,
                    q,
                    a,
                    b,
                    c,
                    d,
                    answer
                )
            )

            added += 1

        conn.commit()

        print("\n" + "=" * 55)
        print("✅ CHEMISTRY QUESTIONS IMPORT COMPLETE")
        print("=" * 55)
        print(f"✅ New questions added : {added}")
        print(f"⏭️ Already existing    : {skipped}")
        print(f"📚 Questions supplied  : {len(questions)}")
        print(f"🧪 Subject ID          : {subject_id}")
        print("=" * 55)

        # Show final Chemistry count.
        cur.execute(
            """
            SELECT COUNT(*)
            FROM questions
            WHERE subject_id = ?
            """,
            (subject_id,)
        )

        total = cur.fetchone()[0]

        print(f"📊 Total Chemistry questions in database: {total}")

    except Exception as e:
        conn.rollback()
        print("\n❌ ERROR:")
        print(e)

    finally:
        conn.close()


if __name__ == "__main__":
    add_questions()
