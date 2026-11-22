
from utils.resume_parser import parse_resume

file_path = r"E:\MAINAK_DAS_Resume.pdf"

try:
    with open(file_path, "rb") as resume_file:
        text = parse_resume(resume_file)

    print("Resume parsing successful!")
    print("-" * 40)
    print(text[:1000])

except Exception as e:
    print("Error:", e)
