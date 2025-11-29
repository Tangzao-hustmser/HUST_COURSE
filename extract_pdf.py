import pypdf
import os

pdf_path = r"d:\coding\HUST_COURSE\2024级本科专业人才培养方案_通信工程.pdf"

try:
    reader = pypdf.PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    print(text)
except Exception as e:
    print(f"Error reading PDF: {e}")
