import pandas as pd
from models.summarizer import summarize_job_description
from models.cv_matcher import match_cv_to_job
from database.db import store_results
from utils import extract_resumes_from_pdfs

def recruit_candidates(job_description_file, pdf_folder):
    # Load job descriptions from CSV
    job_data = pd.read_csv(job_description_file)
    
    # Extract resumes from PDFs
    resumes = extract_resumes_from_pdfs(pdf_folder)

    # Process each job description
    for index, row in job_data.iterrows():
        job_desc = row['job_description']
        job_summary = summarize_job_description(job_desc)

        # For each resume, calculate match score
        for resume_name, resume_text in resumes.items():
            match_score = match_cv_to_job(resume_text, job_summary)
            if match_score > 5:  # Assuming 5 is the threshold for shortlisting
                store_results(resume_name, match_score, job_desc)
