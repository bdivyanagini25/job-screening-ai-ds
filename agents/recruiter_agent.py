import pandas as pd
from models.summarizer import summarize_job_description
from models.cv_matcher import match_cv_to_job
from database.db import store_results

def recruit_candidates(job_description_file, resume_file):
    # Read the job descriptions and resumes
    job_data = pd.read_excel(job_description_file)
    resume_data = pd.read_excel(resume_file)

    # Process each job description
    for index, row in job_data.iterrows():
        job_desc = row['job_description']
        job_summary = summarize_job_description(job_desc)

        # For each resume, calculate match score
        for _, resume in resume_data.iterrows():
            cv_text = resume['cv_text']
            match_score = match_cv_to_job(cv_text, job_summary)
            if match_score > 5:  # Assuming 5 is the threshold for shortlisting
                store_results(resume['candidate_name'], match_score, job_desc)

