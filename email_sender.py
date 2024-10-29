import smtplib
from email.mime.txt import MIMEText
from email.mime.multipart import MIMEMultipart
import time

#Configuration
SMTP_SERVER = "smtp.example.com" # SMTP server address
SMTP_PORT = 587 #  SMTP port (example 587 if use TLS)
EMAIL_ADDRESS = "your@example.com" # Email
EMAIL_PASSWORD = "password" # Password

# Sending frequency
EMAIL_COUNT = 5 # How many emails send
INTERVAL = 10 # Time interval between e-mails sending (seconds)

# Message content function
def create_email(subject, body, recipient):
    # Create e-mail object with title and body
    email = MIMEMultipart()
    email["FROM"] = EMAIL_ADDRESS
    email["To"] = recipient
    email["Subject"] = subject
    
    # Adding content to e-mail letter
    email.attach(MIMEText(body, "plain"))
    return email

# Sending function 
def send_email(subject, body, recipient):
    try:
        # Try connect to SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls() # Add TSL session (if needed)
            print(f"Email successfully sent to {recipient}")
    
    except Exception as e:
        print(f"Error can't send e-mail {e}")
        
# E-mail sending function with interval
def send_emails_with_interval():
    subject = "Test email"
    body = "This is test email, sending for server resources testing"
    recipient = "recipient@example.com"
    
    for i in range(EMAIL_COUNT):
        print(f"Sending email {i + 1}")
        send_email(subject, body, recipient)
        if i < EMAIL_COUNT - 1: # Interval between emnails, except for the last one
            time.sleep(INTERVAL)
            
#Main program
if __name__ == "__main__":
    send_emails_with_interval()
