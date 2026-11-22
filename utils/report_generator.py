from datetime import datetime

def generate_report(candidate_name, candidate_skills, match_result):

    categories = match_result["categories"]

    report = f"""
==================================================
              SKILLLENS ANALYSIS REPORT
==================================================

Candidate Name: {candidate_name}
Analysis Date: {datetime.now().strftime("%d-%m-%Y %H:%M")}

--------------------------------------------------
                  MATCH SUMMARY
--------------------------------------------------

Overall Skill Match: {match_result['overall_match_percentage']}%

Total Required Skills: {match_result['total_required']}
Matched Skills: {match_result['total_matched']}
Missing Skills: {match_result['total_required'] - match_result['total_matched']}

--------------------------------------------------
               CATEGORY-WISE ANALYSIS
--------------------------------------------------
"""

    for category, details in categories.items():

        report += f"""

{category}
Match Percentage: {details['match_percentage']}%

Matched Skills:
"""

        if details["matched_skills"]:
            for skill in details["matched_skills"]:
                report += f"- {skill}\n"
        else:
            report += "- None\n"

        report += "\nMissing Skills:\n"

        if details["missing_skills"]:
            for skill in details["missing_skills"]:
                report += f"- {skill}\n"
        else:
            report += "- None\n"

    report += """
--------------------------------------------------
              SKILLS FOUND IN RESUME
--------------------------------------------------
"""

    for category, skills in candidate_skills.items():

        report += f"\n{category}:\n"

        if skills:
            for skill in skills:
                report += f"- {skill}\n"
        else:
            report += "- None\n"

    report += """
--------------------------------------------------
                 RECOMMENDATIONS
--------------------------------------------------
"""

    has_missing_skills = False

    for category, details in categories.items():

        if details["missing_skills"]:

            has_missing_skills = True

            report += f"\nFocus Area: {category}\n"

            for skill in details["missing_skills"]:
                report += f"- Develop knowledge of {skill}\n"

    if not has_missing_skills:
        report += "\nAll identified required skills were matched.\n"

    report += """
==================================================
                 END OF REPORT
==================================================
"""

    return report
