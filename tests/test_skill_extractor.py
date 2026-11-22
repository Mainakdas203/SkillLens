
from utils.skill_extractor import (
    extract_skills,
    extract_skills_by_category
)


role_description = """
Requirements:
Engineering graduate with strong Python and SQL knowledge.
Proficient in MS Excel and business modelling.

Responsibilities:
Support strategic planning and business operations.
Prepare presentations, investor materials and internal reports.
Perform data analytics and financial analysis.
Coordinate with teams and manage multiple priorities.
Strong written communication and problem solving skills.
"""


print("SKILL EXTRACTION TEST")
print("=" * 40)

skills = extract_skills(role_description)

print("\nAll Extracted Skills:")
print(skills)

print("\nCategorized Skills:")

categorized = extract_skills_by_category(role_description)

for category, found_skills in categorized.items():

    print(f"\n{category}:")

    for skill in found_skills:
        print("-", skill)
