from pypdf import PdfReader
from docx import Document

def extract_text_from_pdf(file):
    reader= PdfReader(file)
    text=""
    for page in reader.pages:
        text+= page.extract_text() or""
        
    return text

def extract_text_from_docx(file):
    document= Document(file)
    text=""
    for paragraph in document.paragraphs:
        text += paragraph.text+ "\n"

    return text

def parse_resume(file):
    # identify file type and exttract resume text
    filename= file.name.lower()
    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file)
    elif filename.endswith(".docx"):
        return extract_text_from_docx(file)
    else:
        raise ValueError("Only PDF and DOCX files are supported")