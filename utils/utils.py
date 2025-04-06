import pandas as pd
import os
import fitz  # PyMuPDF

def extract_resumes_from_pdfs(pdf_folder):
    resumes = []

    # Iterate over all files in the specified folder
    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            file_path = os.path.join(pdf_folder, filename)

            # Open the PDF file
            with fitz.open(file_path) as doc:
                text = ""
                for page in doc:
                    text += page.get_text()

            # Store the extracted text along with the filename
            resumes.append({
                'filename': filename,
                'text': text
            })

    return resumes

def read_excel(file_path):
    return pd.read_excel(file_path)

def preprocess_text(text):
    # Implement any text cleaning or preprocessing logic here
    return text
