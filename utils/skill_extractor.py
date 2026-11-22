
import re


# ==========================================
# 1. SKILL DATABASE
# ==========================================

SKILL_CATEGORIES = {

    "Technical Skills": [
        "Python",
        "Java",
        "C",
        "C++",
        "JavaScript",
        "HTML",
        "CSS",
        "SQL",
        "MySQL",
        "PostgreSQL",
        "MongoDB",
        "Machine Learning",
        "Deep Learning",
        "Data Structures",
        "Algorithms",
        "OOP",
        "Git",
        "GitHub",
        "Power BI",
        "Excel",
        "Streamlit",
        "Flask",
        "Django",
        "React",
        "Node.js",
        "Pandas",
        "NumPy",
        "Matplotlib",
        "JDBC",
        "Data Analysis",
        "Data Visualization"
    ],

    "Business Skills": [
        "Business Analysis",
        "Business Modelling",
        "Financial Modelling",
        "Strategic Planning",
        "Business Planning",
        "Business Operations",
        "Financial Analysis",
        "Market Research",
        "Data Analytics",
        "Decision Making",
        "Process Improvement",
        "Project Management",
        "Investor Relations",
        "Reporting"
    ],

    "Communication & Execution Skills": [
        "Communication",
        "Written Communication",
        "Verbal Communication",
        "Presentation Skills",
        "Documentation",
        "Report Writing",
        "Teamwork",
        "Leadership",
        "Multitasking",
        "Problem Solving",
        "Time Management",
        "Coordination",
        "Stakeholder Management",
        "Follow-up",
        "Attention to Detail"
    ]
}


# ==========================================
# 2. SKILL ALIASES / SYNONYMS
# ==========================================

SKILL_ALIASES = {

    "Excel": [
        "MS Excel",
        "Microsoft Excel"
    ],

    "Business Modelling": [
        "Business Models",
        "Build Business Models",
        "Business Model Development"
    ],

    "Financial Modelling": [
        "Financial Models",
        "Build Financial Models",
        "Financial Model Development"
    ],

    "Business Planning": [
        "Business Plan",
        "Business Plans"
    ],

    "Data Analytics": [
        "Data Analysis",
        "Analytics"
    ],

    "Presentation Skills": [
        "Presentations",
        "Preparing Presentations",
        "Presentation Preparation"
    ],

    "Reporting": [
        "Reports",
        "Internal Reports",
        "Preparing Reports"
    ],

    "Multitasking": [
        "Multiple Priorities",
        "Managing Multiple Tasks",
        "Handling Multiple Tasks"
    ],

    "Written Communication": [
        "Strong Writing",
        "Writing Skills",
        "Clear Writing"
    ],

    "Coordination": [
        "Coordinate",
        "Coordinating",
        "Team Coordination"
    ],

    "Problem Solving": [
        "Problem-Solving",
        "Analytical Problem Solving"
    ]
}


# ==========================================
# 3. CHECK WHETHER A SKILL EXISTS IN TEXT
# ==========================================

def matches_skill(text, skill):

    terms = [skill] + SKILL_ALIASES.get(skill, [])

    for term in terms:

        pattern = r"\b" + re.escape(term) + r"\b"

        # Prevent C from matching the C in C++
        if skill == "C":
            pattern += r"(?!\s*\+\+)"

        if re.search(pattern, text, re.IGNORECASE):
            return True

    return False


# ==========================================
# 4. EXTRACT ALL SKILLS
# ==========================================

def extract_skills(text):

    found_skills = []

    for category, skills in SKILL_CATEGORIES.items():

        for skill in skills:

            if matches_skill(text, skill):
                found_skills.append(skill)

    return found_skills


# ==========================================
# 5. EXTRACT SKILLS BY CATEGORY
# ==========================================

def extract_skills_by_category(text):

    categorized_skills = {}

    for category, skills in SKILL_CATEGORIES.items():

        found = []

        for skill in skills:

            if matches_skill(text, skill):
                found.append(skill)

        categorized_skills[category] = found

    return categorized_skills
