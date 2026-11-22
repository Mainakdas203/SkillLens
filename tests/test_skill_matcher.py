
from utils.skill_matcher import match_skills

candidate_skills = [
    "Python",
    "Java",
    "SQL",
    "Git",
    "DSA"
]

required_skills = [
    "Python",
    "Java",
    "SQL",
    "React",
    "Git",
    "DSA"
]

result = match_skills(candidate_skills, required_skills)

print("Skill Matching Successful!")
print("-" * 40)

print("Matched Skills:", result["matched_skills"])
print("Missing Skills:", result["missing_skills"])
print("Match Percentage:", result["match_percentage"], "%")

print("-" * 40)
