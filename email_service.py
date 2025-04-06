import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_interview_email(candidate_name, interview_date, interview_time, interview_link):
    sender_email = "divyabachu25@gmail.com"
    receiver_email = "jahnavibattina@gmail.com"
    password = "yojc sqif ysdl hnsv"  # Use a secure method to handle passwords
    
    subject = "Interview Invitation"
    body = f"Dear {candidate_name},\n\nYou have been shortlisted for an interview on {interview_date} at {interview_time}.\nPlease use the following link to join the interview: {interview_link}\n\nBest regards,\nRecruitment Team"
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:  # Replace with your SMTP server
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print(f"Interview email sent to {candidate_name}")
    except Exception as e:
        print(f"Error sending email: {e}")
