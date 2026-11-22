def match_skills(candidate_skills, required_skills):

    candidate_lookup = {
        skill.lower(): skill for skill in candidate_skills
    }

    required_lookup = {
        skill.lower(): skill for skill in required_skills
    }

    matched_keys = set(candidate_lookup) & set(required_lookup)
    missing_keys = set(required_lookup) - set(candidate_lookup)

    if not required_lookup:
        percentage = 0
    else:
        percentage = (
            len(matched_keys) / len(required_lookup)
        ) * 100

    return {
        "matched_skills": sorted(
            [required_lookup[key] for key in matched_keys]
        ),
        "missing_skills": sorted(
            [required_lookup[key] for key in missing_keys]
        ),
        "match_percentage": round(percentage, 2)
    }


def match_skills_by_category(candidate_skills, required_skills):

    results = {}

    total_required = 0
    total_matched = 0

    for category in required_skills:

        candidate = candidate_skills.get(category, [])
        required = required_skills.get(category, [])

        result = match_skills(candidate, required)

        results[category] = result

        total_required += len(set(
            skill.lower() for skill in required
        ))

        total_matched += len(result["matched_skills"])

    if total_required == 0:
        overall_percentage = 0
    else:
        overall_percentage = (
            total_matched / total_required
        ) * 100

    return {
        "categories": results,
        "overall_match_percentage": round(overall_percentage, 2),
        "total_required": total_required,
        "total_matched": total_matched
    }
