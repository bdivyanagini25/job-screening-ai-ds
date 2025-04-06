from agents.recruiter_agent import recruit_candidates
from email_service import send_interview_email
from database.db import create_database

def main():
    create_database()
    recruit_candidates("job_description.xlsx", "resume_data.xlsx")
    
    # For demonstration: send an interview email
    send_interview_email("John Doe", "2025-04-10", "10:00 AM", "http://interview_link.com")

if __name__ == "__main__":
    main()
