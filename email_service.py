import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_interview_email(candidate_name, interview_date, interview_time, interview_link):
    sender_email = "your_email@example.com"
    receiver_email = "candidate_email@example.com"
    password = "your_password"

    subject = "Interview Invitation"
    body = f"Dear {candidate_name},\n\nWe are pleased to invite you for an interview on {interview_date} at {interview_time}.\n\nPlease join the interview using the following link: {interview_link}\n\nBest regards,\nHR Team"

    # Create email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
