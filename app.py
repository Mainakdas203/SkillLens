import streamlit as st

from utils.resume_parser import parse_resume
from utils.skill_extractor import extract_skills_by_category
from utils.skill_matcher import match_skills_by_category
from utils.report_generator import generate_report


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="SkillLens - Resume Analyzer",
    page_icon="🎯",
    layout="wide"
)


# ==========================================
# APPLICATION HEADER
# ==========================================

st.title("🎯 SkillLens")

st.subheader("Resume & Job Description Skill Gap Analyzer")

st.write(
    "Analyze how well your resume aligns with a job description "
    "or role description."
)

st.divider()


# ==========================================
# USER INPUTS
# ==========================================

st.header("1. Candidate Information")

candidate_name = st.text_input(
    "Candidate Name",
    placeholder="Enter your name"
)

st.header("2. Upload Your Resume")

uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf", "docx"]
)

st.header("3. Enter Job or Role Description")

job_description = st.text_area(
    "Paste the job description or role responsibilities:",
    height=250,
    placeholder="Paste the job description, responsibilities and requirements..."
)


# ==========================================
# ANALYSIS
# ==========================================

if st.button("Analyze Resume", type="primary"):

    if not candidate_name.strip():
        st.error("Please enter your name.")

    elif uploaded_file is None:
        st.error("Please upload your resume.")

    elif not job_description.strip():
        st.error("Please enter a job description.")

    else:

        try:

            # Extract resume text
            resume_text = parse_resume(uploaded_file)

            if not resume_text.strip():
                st.error("Could not extract text from the uploaded resume.")
                st.stop()

            # Extract categorized skills
            candidate_skills = extract_skills_by_category(resume_text)

            required_skills = extract_skills_by_category(job_description)

            if not any(required_skills.values()):
                st.warning(
                    "No recognized skills found in the role description."
                )
                st.stop()

            # Match skills
            result = match_skills_by_category(
                candidate_skills,
                required_skills
            )

            # Generate report
            report = generate_report(
                candidate_name.strip(),
                candidate_skills,
                result
            )

            # ==================================
            # DISPLAY RESULTS
            # ==================================

            st.divider()

            st.header("4. Analysis Results")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Overall Match",
                f"{result['overall_match_percentage']}%"
            )

            col2.metric(
                "Matched Skills",
                result["total_matched"]
            )

            col3.metric(
                "Missing Skills",
                result["total_required"] - result["total_matched"]
            )

            st.progress(
                result["overall_match_percentage"] / 100
            )

            st.caption(
                "This score measures recognized skill coverage, "
                "not overall job suitability."
            )

            # ==================================
            # CATEGORY-WISE ANALYSIS
            # ==================================

            st.divider()

            st.header("5. Category-wise Analysis")

            for category, details in result["categories"].items():

                with st.expander(
                    f"{category} — {details['match_percentage']}%",
                    expanded=True
                ):

                    st.metric(
                        "Category Match",
                        f"{details['match_percentage']}%"
                    )

                    st.progress(
                        details["match_percentage"] / 100
                    )

                    st.write("**Matched Skills**")

                    if details["matched_skills"]:
                        st.success(
                            ", ".join(details["matched_skills"])
                        )
                    else:
                        st.info("No matched skills found.")

                    st.write("**Missing Skills**")

                    if details["missing_skills"]:
                        st.warning(
                            ", ".join(details["missing_skills"])
                        )
                    else:
                        st.success("No missing skills.")

            # ==================================
            # CANDIDATE SKILLS
            # ==================================

            st.divider()

            st.header("6. Skills Found in Resume")

            for category, skills in candidate_skills.items():

                st.write(f"**{category}**")

                if skills:
                    st.write(", ".join(skills))
                else:
                    st.write("No recognized skills found.")

            # ==================================
            # DOWNLOAD REPORT
            # ==================================

            st.divider()

            st.header("7. Download Analysis Report")

            st.download_button(
                label="Download Detailed Analysis Report",
                data=report,
                file_name="SkillLens_Analysis_Report.txt",
                mime="text/plain"
            )

        except Exception as error:

            st.error(f"Analysis failed: {error}")