import sqlite3

DATABASE = "exam.db"

questions = [
    (
        "What is the scientific study of life or living things called?",
        "Chemistry",
        "Physics",
        "Biology",
        "Geology",
        "C"
    ),
    (
        "Which of the following is a characteristic of living things?",
        "Lack of complexity",
        "Response to stimuli",
        "Inability to reproduce",
        "Inability to adapt",
        "B"
    ),
    (
        "Which of the following is NOT a common characteristic of living systems?",
        "Being highly disordered",
        "Requiring energy for work",
        "Being composed of one or more cells",
        "Evolutionary adaptation to the environment",
        "A"
    ),
    (
        "Which tool is essential for biologists to observe cells?",
        "Beaker",
        "Test tube",
        "Microscope",
        "Bunsen burner",
        "C"
    ),
    (
        "Which of the following is a fundamental part of a biological investigation?",
        "Not utilizing any tools",
        "Using random guessing",
        "Ignoring collected data",
        "Following the scientific method",
        "D"
    ),
    (
        "What does the term 'homeostasis' refer to in living organisms?",
        "The ability to evolve",
        "The capacity for reproduction",
        "The need for genetic transmission",
        "Maintenance of relatively constant internal conditions",
        "D"
    ),
    (
        "What is the relationship between biology and chemistry in scientific study?",
        "They are completely unrelated",
        "Biology only borrows tools from physics",
        "Biology and chemistry study the same processes",
        "Chemistry provides tools and concepts to study biological molecules",
        "D"
    ),
    (
        "In biology, studying living organisms often requires merging information from which other field?",
        "Chemistry",
        "Geology",
        "Astronomy",
        "Economics",
        "A"
    ),
    (
        "Why do humans study living organisms and their habitats?",
        "To create new planets",
        "To improve technology",
        "For entertainment purposes",
        "Because of inborn curiosity about the natural world",
        "D"
    ),
    (
        "How has biology contributed to everyday life?",
        "By discovering new species",
        "By creating new languages",
        "By reducing the need for food",
        "By discovering drugs used to treat diseases",
        "D"
    ),
    (
        "Which of the following is an example of how biology affects agriculture?",
        "The construction of cities",
        "The invention of new sports",
        "Transformations in genetics and cell biology",
        "The development of transportation systems",
        "C"
    ),
    (
        "How does ecology help societies address environmental issues?",
        "By studying food patterns",
        "By increasing water pollution",
        "By evaluating issues like global warming",
        "By creating new forms of non-renewable energy",
        "C"
    ),
    (
        "Which biological process is used in the production of alcoholic drinks like beer and wine?",
        "Photosynthesis",
        "Fermentation",
        "Respiration",
        "Digestion",
        "B"
    ),
    (
        "What is the first step in the scientific method?",
        "Analyzing data",
        "Making observations",
        "Drawing conclusions",
        "Conducting an experiment",
        "B"
    ),
    (
        "Which step of the scientific method involves creating a testable explanation for observations?",
        "Conclusion",
        "Hypothesis formation",
        "Data collection",
        "Experimentation",
        "B"
    ),
    (
        "During which step of the scientific method do scientists gather and record data from experiments?",
        "Data collection",
        "Hypothesis formation",
        "Conclusion",
        "Communicating results",
        "A"
    ),
    (
        "What is the purpose of conducting an experiment in the scientific method?",
        "To test the hypothesis",
        "To draw conclusions without data",
        "To prove a theory",
        "To publish results",
        "A"
    ),
    (
        "What step comes after analyzing the data in the scientific method?",
        "Drawing a conclusion",
        "Formulating a new hypothesis",
        "Observing again",
        "Communicating results",
        "A"
    ),
    (
        "What is the primary function of a hand lens?",
        "To record data",
        "To measure temperature",
        "To magnify objects placed under it",
        "To observe detailed cell structures",
        "C"
    ),
    (
        "Compared to the naked eye, how does a hand lens assist in observing objects?",
        "It provides a clearer, larger image",
        "It records the object's properties",
        "It decreases the size of the object",
        "It enhances the color of the object",
        "A"
    ),
    (
        "Which microscope is commonly used in biology?",
        "Simple light microscope",
        "Electron microscope",
        "Compound light microscope",
        "X-ray microscope",
        "C"
    ),
    (
        "What is the magnification power of a compound light microscope?",
        "10X",
        "100X",
        "2000X",
        "2,000,000X",
        "C"
    ),
    (
        "What type of microscope uses a beam of electrons?",
        "Electron microscope",
        "Simple microscope",
        "Hand lens",
        "Light microscope",
        "A"
    ),
    (
        "Which of the following is used to view viruses?",
        "Hand lens",
        "Electron microscope",
        "Simple light microscope",
        "Compound light microscope",
        "B"
    ),
    (
        "Which type of microscope has a single lens?",
        "Simple light microscope",
        "Compound microscope",
        "Electron microscope",
        "Binocular microscope",
        "A"
    ),
    (
        "What type of microscope has two eyepieces?",
        "Simple microscope",
        "Monocular microscope",
        "Electron microscope",
        "Binocular compound microscope",
        "D"
    ),
    (
        "What is the primary use of glass slides?",
        "To magnify objects",
        "To hold specimens",
        "To sterilize materials",
        "To culture microorganisms",
        "B"
    ),
    (
        "What is the purpose of an autoclave?",
        "To sterilize materials",
        "To culture microorganisms",
        "To observe cells",
        "To measure mass",
        "A"
    ),
    (
        "What does an incubator do?",
        "Detects changes in physical properties",
        "Sterilizes equipment, materials, and waste",
        "Maintains a specific environment for culturing",
        "Provides a sterile environment for microbial growth",
        "C"
    ),
    (
        "What is the primary purpose of petri dishes?",
        "Measuring pH levels",
        "Culturing microorganisms",
        "Measuring mass",
        "Heating substances",
        "B"
    ),
    (
        "What tool is used to culture microorganisms in liquid form?",
        "Culture tubes",
        "Balance",
        "Incubator",
        "Beaker",
        "A"
    ),
    (
        "Which laboratory tool is used for mixing solutions?",
        "Beaker",
        "Flasks",
        "Autoclave",
        "Petri dish",
        "B"
    ),
    (
        "What is the main function of a balance in the laboratory?",
        "To measure mass",
        "To mix solutions",
        "To sterilize materials",
        "To measure temperature",
        "A"
    ),
    (
        "What tool is used to control the amount of solution being added to a sample?",
        "Dropper",
        "Flasks",
        "Tongs",
        "Incubator",
        "A"
    ),
    (
        "What are tongs used for in the laboratory?",
        "Mixing substances",
        "Holding small objects",
        "Lifting hot objects",
        "Sterilizing materials",
        "C"
    ),
    (
        "Which tool is used to hold or pick up small objects?",
        "Dropper",
        "Beaker",
        "Forceps",
        "Bunsen burner",
        "C"
    ),
    (
        "A spatula is shaped like which of the following?",
        "A spoon",
        "A funnel",
        "A knife",
        "A magnifying glass",
        "A"
    ),
    (
        "What are wash bottles used for?",
        "Heating solutions",
        "Rinsing laboratory materials",
        "Holding small objects",
        "Measuring pH levels",
        "B"
    ),
    (
        "Which tool is used for heating and sterilizing materials?",
        "Incubator",
        "Bunsen burner",
        "pH meter",
        "Dissecting tool kit",
        "B"
    ),
    (
        "What is the function of the dissecting tool kit?",
        "Heating solutions",
        "Dissecting animals",
        "Holding microorganisms",
        "Sterilizing laboratory equipment",
        "B"
    ),
    (
        "Which tool is used to collect insects?",
        "Insect net",
        "Fishing net",
        "Bunsen burner",
        "Culture tubes",
        "A"
    ),
    (
        "A fishing net is primarily used for which of the following?",
        "Fishing",
        "Culturing microorganisms",
        "Measuring pH",
        "Collecting insects",
        "A"
    ),
    (
        "What is the main difference between a simple and compound microscope?",
        "Compound microscope uses electrons",
        "Simple microscope uses multiple lenses",
        "Compound microscope uses multiple lenses",
        "Simple microscope has higher magnification",
        "C"
    ),
    (
        "Which of the following tools would be best suited for observing bacteria?",
        "Hand lens",
        "Dissecting pan",
        "Fishing net",
        "Compound light microscope",
        "D"
    ),
    (
        "Which tool is used to measure the pH of a substance?",
        "pH meter",
        "Autoclave",
        "Incubator",
        "Thermometer",
        "A"
    ),
    (
        "Which laboratory tool is used to heat solutions?",
        "Balance",
        "Hot plate",
        "Forceps",
        "Thermometer",
        "B"
    ),
    (
        "What is the primary use of a crucible in the laboratory?",
        "Heating liquids",
        "Measuring mass",
        "Melting elements",
        "Dissecting animals",
        "C"
    ),
    (
        "Which tool is used to mix substances into solutions?",
        "Tongs",
        "Spatula",
        "Incubator",
        "Bunsen burner",
        "B"
    ),
    (
        "What is the main function of a thermometer in the lab?",
        "Measuring pH",
        "Heating liquids",
        "Sterilizing objects",
        "Measuring temperature",
        "D"
    ),
    (
        "Which of the following laboratory tools can be used to hold hot or cold water?",
        "Beaker",
        "Autoclave",
        "Wash bottle",
        "Bunsen burner",
        "A"
    ),
    (
        "What is the function of forceps in a laboratory setting?",
        "Heating liquids",
        "Measuring temperature",
        "Picking up small objects",
        "Observing microorganisms",
        "C"
    ),
    (
        "Which of the following is NOT a field tool?",
        "Insect net",
        "Fishing net",
        "Soil test kits",
        "Dissecting tool kit",
        "D"
    ),
    (
        "Which tool is used to sterilize laboratory materials by exposing them to high temperature and pressure?",
        "Autoclave",
        "Bunsen burner",
        "Beaker",
        "Incubator",
        "A"
    ),
    (
        "Which device measures mass in a laboratory?",
        "Balance",
        "Spatula",
        "Dropper",
        "Thermometer",
        "A"
    ),
    (
        "What is a culture tube used for?",
        "Measuring mass",
        "Heating substances",
        "Culturing microorganisms",
        "Rinsing laboratory materials",
        "C"
    ),
    (
        "Which tool maintains a specific temperature for growing microorganisms?",
        "Incubator",
        "Autoclave",
        "Thermometer",
        "Bunsen burner",
        "A"
    ),
    (
        "What type of microscope uses a beam of light and multiple lenses?",
        "Simple microscope",
        "Electron microscope",
        "Monocular microscope",
        "Compound light microscope",
        "D"
    ),
    (
        "A microscope with two eyepieces is called a (an):",
        "Electron microscope",
        "Monocular microscope",
        "Simple light microscope",
        "Binocular compound microscope",
        "D"
    ),
    (
        "Which part of the microscope is used to look through?",
        "Nose piece",
        "Objective lens",
        "Condenser",
        "Eyepiece (Ocular)",
        "D"
    ),
    (
        "What is the function of the eyepiece tube?",
        "It holds the eyepiece",
        "It supports the microscope",
        "It holds the objective lenses",
        "It focuses light on the specimen",
        "A"
    ),
    (
        "Which component provides magnification in the range of 4x to 100x?",
        "Eyepiece",
        "Diaphragm",
        "Condenser",
        "Objective lenses",
        "D"
    ),
    (
        "The part that supports the microscope and holds all its components is the:",
        "Base",
        "Arm",
        "Stage",
        "Nose piece",
        "A"
    ),
    (
        "Which part connects the eyepiece to the objective lenses?",
        "Stage",
        "Body tube",
        "Condenser",
        "Nose piece",
        "B"
    ),
    (
        "What does the nose piece do?",
        "Holds the slide",
        "Focuses the light",
        "Holds the eyepiece",
        "Changes the magnification",
        "D"
    ),
    (
        "The coarse adjustment knob is used to:",
        "Sharpen the image",
        "Adjust light intensity",
        "Rotate the nose piece",
        "Move the specimen closer for general focus",
        "D"
    ),
    (
        "The fine adjustment knob helps to:",
        "Adjust the amount of light",
        "Rotate the objective lenses",
        "Move the stage up and down",
        "Sharpen the focus of the specimen",
        "D"
    ),
    (
        "Which part of the microscope is the platform where the slide is placed?",
        "Stage",
        "Condenser",
        "Nose piece",
        "Diaphragm",
        "A"
    ),
    (
        "What is the function of the stage clip?",
        "Move the stage",
        "Control the light",
        "Hold the stage in place",
        "Hold the glass slide in place",
        "D"
    ),
    (
        "The aperture is located on the stage to:",
        "Adjust the focus",
        "Move the stage clip",
        "Hold the objective lenses",
        "Allow light to reach the specimen",
        "D"
    ),
    (
        "What is the purpose of the microscope illuminator?",
        "Focus the specimen",
        "Provide a light source",
        "Adjust magnification",
        "Rotate the nose piece",
        "B"
    ),
    (
        "Where is the microscopic illuminator located?",
        "At the base",
        "Under the stage",
        "In the eyepiece",
        "Attached to the arm",
        "A"
    ),
    (
        "What is the function of the condenser?",
        "Move the stage",
        "Hold the eyepiece",
        "Rotate the objective lenses",
        "Focus light on the specimen",
        "D"
    ),
    (
        "Which part of the microscope controls the amount of light that reaches the specimen?",
        "Aperture",
        "Condenser",
        "Stage clip",
        "Diaphragm (Iris)",
        "D"
    ),
    (
        "Where is the diaphragm (Iris) located?",
        "At the base",
        "In the eyepiece",
        "Under the stage",
        "In the nose piece",
        "C"
    ),
    (
        "What is the function of the base of the microscope?",
        "Rotate the objective lenses",
        "Support all the microscope parts",
        "Hold the stage clip",
        "Hold the light source",
        "B"
    ),
    (
        "Which part of the microscope can change magnification?",
        "Base",
        "Eyepiece",
        "Nose piece",
        "Coarse adjustment knob",
        "C"
    ),
    (
        "Which component is used for fine-tuning the focus of a specimen?",
        "Condenser",
        "Diaphragm",
        "Fine adjustment knob",
        "Coarse adjustment knob",
        "C"
    ),
    (
        "Which part holds the objective lenses?",
        "Nose piece",
        "Aperture",
        "Stage clip",
        "Body tube",
        "A"
    ),
    (
        "The part that adjusts the distance between the stage and objective lens is:",
        "Stage",
        "Aperture",
        "Fine adjustment knob",
        "Coarse adjustment knob",
        "D"
    ),
    (
        "What part of the microscope is crucial for controlling the light that passes through the specimen?",
        "Stage",
        "Aperture",
        "Diaphragm",
        "Objective lens",
        "C"
    ),
    (
        "What part holds the microscope slide in place?",
        "Stage",
        "Stage clip",
        "Condenser",
        "Fine adjustment knob",
        "B"
    ),
    (
        "Which component focuses light onto the specimen?",
        "Eyepiece",
        "Diaphragm",
        "Condenser",
        "Illuminator",
        "C"
    ),
    (
        "Which part provides the illumination necessary for viewing the specimen?",
        "Illuminator",
        "Objective lenses",
        "Eyepiece",
        "Nose piece",
        "A"
    ),
    (
        "When carrying a microscope, which part should be held securely for safe transportation?",
        "Base and arm",
        "Eyepiece and stage",
        "Stage and objective lens",
        "Coarse adjustment knob and base",
        "A"
    ),
    (
        "Which focusing knob should be used first when focusing on a specimen under the low power objective?",
        "Fine adjustment knob",
        "Coarse adjustment knob",
        "Diaphragm control",
        "Light intensity knob",
        "B"
    ),
    (
        "What is the correct action after finishing with the microscope slide?",
        "Clean the slide with alcohol",
        "Turn off the microscope light",
        "Lower the stage and remove the slide",
        "Rotate the objective to the highest power",
        "C"
    ),
    (
        "Why should lens paper and alcohol be used to clean the microscope lenses?",
        "To remove dust particles",
        "To prevent the lens from fogging up",
        "To ensure the lens remains free from scratches",
        "To preserve the magnification power of the lenses",
        "C"
    ),
    (
        "Before storing the microscope, which objective lens should be set over the stage?",
        "4x",
        "10x",
        "40x",
        "100x",
        "A"
    ),
    (
        "When wrapping the power cord for storage, what is the recommended procedure?",
        "Leave it hanging loose",
        "Tuck it inside the microscope case",
        "Wrap it tightly around the eyepiece",
        "Wrap it neatly and secure it with a tie",
        "D"
    ),
    (
        "How should the oculars (eyepieces) be positioned when placing the microscope back into its cabinet?",
        "Tilted towards the stage",
        "Facing the back of the cabinet",
        "Tilted downwards towards the base",
        "Pointing towards the front of the cabinet",
        "D"
    ),
    (
        "Why is it important to follow instructions in the laboratory?",
        "To avoid boredom and to be happy",
        "To prevent accidents and maintain safety",
        "To impress the teacher and your classmates",
        "To ensure experiments are completed quickly",
        "B"
    ),
    (
        "Which of the following is NOT allowed in the laboratory?",
        "Drinking beverages",
        "Using gloves and masks",
        "Wearing protective clothing",
        "Following safety protocols",
        "A"
    ),
    (
        "What is the purpose of knowing the location of safety equipment in a laboratory?",
        "To respond quickly during an emergency",
        "To slow down the process of the experiment",
        "To make a long and complex experiment simple",
        "To record temperature at various environments",
        "A"
    ),
    (
        "Which of these is an important laboratory safety rule?",
        "Always work alone in the lab",
        "Never eat or drink in the laboratory",
        "Taste chemicals if unsure of their identity",
        "Wear regular clothes during lab activities",
        "B"
    ),
    (
        "When should you clean your experiment area?",
        "Every few days",
        "Only at the end of the day",
        "After each experiment",
        "Before starting the experiment",
        "C"
    ),
    (
        "What should you do if you spill a chemical in the laboratory?",
        "Ignore it and continue working",
        "Leave the laboratory immediately",
        "Clean it up immediately without telling anyone",
        "Inform your teacher and follow proper cleanup procedures",
        "D"
    ),
    (
        "Why should you never taste or sniff chemicals in the laboratory?",
        "It's rude and is considered cheating",
        "It can interfere with laboratory results",
        "It exposes us to drugs that can cause addiction",
        "It could be dangerous and harmful to your health",
        "D"
    ),
    (
        "What should you do before leaving the laboratory?",
        "Report to the teacher for extra credit",
        "Ask your laboratory partner to clean up",
        "Leave your work area as it is for the next user",
        "Switch off all electrical devices and clean your workspace",
        "D"
    ),
    (
        "Which of the following behaviors is appropriate in the laboratory?",
        "Ignoring safety signs",
        "Eating lunch while working",
        "Running and playing around",
        "Acting responsibly and carefully",
        "D"
    ),
    (
        "What should you do if you accidentally spill a chemical on yourself?",
        "Ignore it, as small spills are not harmful",
        "Ask someone else to clean it up for you",
        "Clean it up immediately using cold water",
        "Wait until the end of the experiment to clean it up",
        "C"
    )
]

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

subject = cursor.execute(
    "SELECT id FROM subjects WHERE name = ?",
    ("Biology",)
).fetchone()

if not subject:
    print("❌ Biology subject not found!")
    conn.close()
    exit()

subject_id = subject[0]

# Delete old Biology questions first
cursor.execute(
    "DELETE FROM questions WHERE subject_id = ?",
    (subject_id,)
)

for q in questions:
    cursor.execute(
        """
        INSERT INTO questions
        (subject_id, question, option_a, option_b, option_c, option_d, correct_answer)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (subject_id, *q)
    )

conn.commit()
conn.close()

print(f"✅ {len(questions)} Biology questions added successfully!")
