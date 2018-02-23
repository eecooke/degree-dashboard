# Partition course codes into broader learning themes
themes = {
    "MATH": "MATH",
    "CO": "MATH",
    "STAT": "MATH",
    "PMATH": "MATH",
    "AMATH": "MATH",
    "CS": "CS",
    "COOP": "COOP",
    "PHIL": "PHILOSOPHY",
    "HUMSC": "PHILOSOPHY",
    "KOREA": "LANGUAGE",
    "RS": "LANGUAGE",
    "INTEG": "MISC",
    "MUSIC": "MISC",
    "PSYCH": "MISC",
    "SPCOM": "MISC"
}

# My transcript. A story of God's grace to me.
# Record of all courses taken and respective grades. Ongoing courses are indicated by a grade of -1
completed = {
    "MATH": [
        ["135", "Algebra", 60, "1A"],
        ["137", "Calculus 1", "WD", "1A"],
        ["136", "Linear Algebra 1", 52, "1B"],
        ["137", "Calculus 1", 74, "1B"],
        ["136", "Linear Algebra 1", 72, "2A"],
        ["138", "Calculus 2", 42, "2A"],
        ["239", "Intro to Combinatorics", 36, "2A"],
        ["138", "Calculus 2", 50, "2AC"],
        ["235", "Linear Algebra 2", 62, "2AA"],
        ["239", "Intro to Combinatorics", 77, "2B"]
    ], "CS": [
        ["135", "Designing Functional Programs", 76, "1A"],
        ["136", "Elementary Algorithm Design & Data Abstraction", 66, "1B"],
        ["234", "Data Types & Structures", 86, "2A"],
        ["246", "Object-Oriented Software Development", 52, "2AA"],
        ["330", "Management Information Systems", 76, "2B"]
    ], "STAT": [
        ["230", "Probability", 50, "2A"],
        ["231", "Statistics", 79, "2AA"],
        ["331", "Applied Linear Models", 76, "2B"]
    ], "CO": [
        ["250", "Intro to Optimization", 79, "3A"],
        ["342", "Intro to Graph Theory", 70, "3A"]
    ], "PMATH": [
        ["330", "Intro to Mathematical Logic", 93, "3A"]
    ], "PHIL": [
        ["145", "Critical Thinking", 86, "2AA"],
        ["256", "Intro to Cognitive Science", 89, "2B"],
        ["283", "Great Works: Ancient & Medieval", 88, "3A"]
    ], "PSYCH": [
        ["101", "Intro to Psychologoy", 89, "1A"],
        ["212R", "Educational Psychology", 78, "1B"]
    ], "MUSIC": [
        ["140", "History of Pop Music", 90, "3A"]
    ], "KOREA": [
        ["101R", "First-Year Korean 1", 80, "1B"]
    ], "INTEG": [
        ["251", "Creative Thinking", 91, "2B"]
    ], "SPCOM": [
        ["100", "Interpersonal Communication", 82, "1A"]
    ], "PD": [
        ["1", "Co-op Fundamentals", "CR", "2A"],
        ["2", "Critical Reflection & Report Writing", "CR", "2AC"],
        ["6", "Problem Solving", "CR", "2AAC"],
        ["8", "Intercultural Skills", "CR", "2BC"],
        ["5", "Project Management", -1, "3AC"]
    ], "COOP": [
        ["1", "Sheridan College", "CR", "2AC"],
        ["2", "GEO Semiconductor", "CR", "2AAC"],
        ["3", "ISARA Corporation", "CR", "2BC"],
        ["4", "Canadian Solar", -1, "3AC"]
    ], "WKRPT": [
        ["200", "Work Report 2", 89, "2AAC"],
        ["300", "Work Report 3", 75, "2BC"],
        ["400", "Work Report 4", -1, "3AC"]
    ]
}

# Courses of interest to consider taking in future terms
# Offerings are encoded as (W) winter, (S) spring, (F) fall, or (A) all.
# Some are specified further as offered during (E) even or (O) odd years only.
ideas = {
    "RS": [
        ["133", "New Testament Greek 1", "A"],
        ["134", "New Testament Greek 2", "A"]
    ], "CO": [
        ["456", "Intro to Game Theory", "A"],
        ["380", "Mathematical Discovery and Invention", "SE", 1],
        ["480", "History of Mathematics", "SO", 2],
        ["351", "Network Flow Theory", "A", 1],
        ["453", "Network Design", "A"],
        ["353", "Computational Discrete Optimization", "A"],
        ["367", "Nonlinear Optimization", "F"],
        ["370", "Deterministic OR Models", "F", 3],
        ["454", "Scheduling", "S"],
        ["485", "The Math of PK Cryptography", "F"],
        ["487", "Applied Cryptography", "W"],
    ], "HUMSC": [
        ["201", "Great Dialogues: Reason and Faith", "A", 2]
    ], "PSYCH": [
        ["356", "Personality", "A"],
    ], "STAT": [
        ["442", "Data Visualization", "A"],
        ["443", "Forecasting", "A"],
        ["444", "Statistical Learning - Function Estimation", "A"]
    ], "CS": [
        ["230", "Intro to Computers & Systems", "W", 0],
        ["231", "Algorithmic Problem Solving", "S", 1],
        ["338", "Computer Applications in Business: Databases", "A", 3],
        ["370", "Numerical Computation", "A", 2],
        ["436", "Networks and Distributed Computer Systems", "W"],
        ["487", "Intro to Symbolic Computation", "W"]
    ], "PMATH": [
        ["320", "Euclidean Geometry", "A"],
        ["321", "Non-Euclidean Geometry", "A"],
        ["340", "Elementary Number Theory", "A"],
        ["360", "Geometry", "A"],
        ["370", "Chaos and Fractals", "A"]
    ], "AMATH": [
        ["390", "Mathematics and Music", "FE", 0] 
    ], "PHIL": [
        ["257", "Philosophy of Mathematics", "A"],
        ["285J", "Great Christian Thinkers", "A"],
        ["356", "Intelligence in Machines, Humans, and Other Animals", "A", 2]
    ], "HIST": [
        ["109", "Ten Days that Shook the World", "A"]
    ]
}