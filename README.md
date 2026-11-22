# SkillLens – Resume & Job Description Skill Gap Analyzer

SkillLens is a Python-based web application that analyzes a candidate's resume against a job description or role description.

It identifies matching and missing skills, calculates skill match percentages, and generates a downloadable analysis report.

## Features

- Upload resumes in PDF and DOCX formats.
- Extract skills from resumes and job descriptions.
- Categorize skills into Technical, Business, and Communication & Execution.
- Recognize alternative skill phrases using synonym matching.
- Calculate overall and category-wise skill match percentages.
- Identify matched and missing skills.
- Generate downloadable analysis reports.
- Interactive visual analytics dashboard using Plotly.
- Donut chart showing matched vs. missing skills.
- Bar chart displaying category-wise skill match percentages.
- Detailed downloadable skill gap analysis report.
- Supports both PDF and DOCX resume formats.

## Tech Stack

- Python
- Streamlit
- Pandas
- Plotly
- PyPDF
- python-docx

## Project Structure

```text
SkillLens/
├── tests/
├── utils/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/SkillLens.git
```

2. Navigate to the project directory:

```bash
cd SkillLens
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Run the application:

```bash
streamlit run app.py
```

## How It Works

1. Upload a PDF or DOCX resume.
2. Enter the job description or role responsibilities.
3. Click Analyze Resume.
4. Review the overall and category-wise skill matching results.
5. Download the detailed analysis report.

## Limitations

SkillLens currently uses a predefined skill database and keyword-based synonym matching. Its match percentage represents recognized skill coverage, not an assessment of overall job suitability.

## Author

Mainak Das
