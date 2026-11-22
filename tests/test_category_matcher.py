from utils.skill_matcher import match_skills_by_category

candidate_skills = {
    "Technical Skills": [
        "Python",
        "SQL",
        "Excel"
    ],

    "Business Skills": [
        "Data Analytics"
    ],

    "Communication & Execution Skills": [
        "Communication",
        "Problem Solving"
    ]
}


required_skills = {
    "Technical Skills": [
        "Python",
        "SQL",
        "Excel",
        "Java"
    ],

    "Business Skills": [
        "Data Analytics",
        "Business Modelling",
        "Financial Analysis"
    ],

    "Communication & Execution Skills": [
        "Communication",
        "Presentation Skills",
        "Problem Solving"
    ]
}


result = match_skills_by_category(
    candidate_skills,
    required_skills
)


print("CATEGORY MATCHING TEST")
print("=" * 40)

for category, details in result["categories"].items():

    print(f"\n{category}")
    print("Match:", details["match_percentage"], "%")
    print("Matched:", details["matched_skills"])
    print("Missing:", details["missing_skills"])

print("\nOverall Match:", result["overall_match_percentage"], "%")
print("Total Required:", result["total_required"])
print("Total Matched:", result["total_matched"])