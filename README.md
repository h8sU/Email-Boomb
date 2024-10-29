![alt text](https://i.ibb.co/93XBwPm/2.jpg)

# EMAIL Sending Interval Tester

This project is a Python script for testing email server load handling by sending emails at specified intervals.
It is intended for education purposes, allowing users to observe the server's response to controlled email flow. This script is useful for examining email rate limiting, server respinse and general email sending performance under a set frequency.

## Features

- Sends a set number of emails with a delay between each send.
- Configurable SMTP server, email account, and send interval.
- Basic error handeling for troubleshooting

## Requirements 

- Python 3.x
- SMTP server credentials (address, port, email and password)

## Installation

1. Clone this repostory
2. Navigate to the project directory:
    cd email-sending-interval-tester
3. Configuration
    Update the configuration section  in the script with your SMTP server details, email address and other settings

    SMTP_SERVER = "smtp.your-server.com" # Your SMTP server address
    SMTP_PORT = 587 # SMTP port (e.g. 587 for TLS)
    EMAIL_ADDRESS = "your_email@example.com" # email address to send from
    EMAIL_PASSWORD = "your_password" # Password for the email account

    EMAIL_COUNT = # Number of emails to send
    INTERVAL = # Interval between emails in secounds

4. Usage 
    python email_sender.py

This script will send emails at the specified interval (INTERVAL) and display the status in the console

# SCRIPT EXPLANATION

This script cosists of three main functions:
    1. create_email: This function constructs an email object with the given subject, body and recipient.
    
    2. send_email: Connects to the SMTP server, authenticates and sends the email to specified recipient.
    
    3. send_email_with_interval: Calls send_email in a loop, with a delay between each email to simulate controlled email flow.

# EXAMPLE OUTPUT

When running the script, the console will display message like: 

    Send email 1
    Email successfully sent to recipient@example.com
    Send email 2
    Email successfully sent to recipient@example.com
    ...

# DISCLAIMER

This script is intended stricly for educational purposes. Ensure compliance with local regulations and obtain appropriate premissions before testing email sending functions on any server.
