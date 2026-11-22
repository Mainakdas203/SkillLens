from utils.report_generator import generate_report


candidate_name = "Mainak Das"

candidate_skills = {
    "Technical Skills": ["Python", "Java", "Excel"],
    "Business Skills": ["Data Analytics"],
    "Communication & Execution Skills": [
        "Communication",
        "Problem Solving"
    ]
}

match_result = {
    "categories": {
        "Technical Skills": {
            "matched_skills": ["Python", "Excel"],
            "missing_skills": ["Java"],
            "match_percentage": 66.67
        },
        "Business Skills": {
            "matched_skills": ["Data Analytics"],
            "missing_skills": ["Business Modelling"],
            "match_percentage": 50.0
        },
        "Communication & Execution Skills": {
            "matched_skills": ["Communication", "Problem Solving"],
            "missing_skills": ["Presentation Skills"],
            "match_percentage": 66.67
        }
    },
    "overall_match_percentage": 66.67,
    "total_required": 6,
    "total_matched": 4
}

report = generate_report(
    candidate_name,
    candidate_skills,
    match_result
)

print(report)
