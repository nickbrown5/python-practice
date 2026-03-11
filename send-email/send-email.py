import sys
import smtplib
from email.message import EmailMessage

# function to send an email
"""
    Need to have SMTP server running locally with
    aiosmtpd and `python -m aiosmtpd -n -l localhost:1025`
    Prints email to console rather than actually sending it
"""
def send_email(addressFrom, addressTo, subject, message):
    email = EmailMessage()
    email.set_content(message)
    email['Subject'] = subject
    email['From'] = addressFrom
    email['To'] = addressTo

    try:
        with smtplib.SMTP('localhost', 1025, timeout=10) as s:
            s.send_message(email)
            s.quit()
    except ConnectionRefusedError:
        print('Could not connect to SMTP server on localhost:25')
    except Exception as e:
        print(f'Email sending failed: {e}')

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print('Please provide the from address, to address, subject and message')
        sys.exit()
    
    addressFrom = sys.argv[1]
    addressTo = sys.argv[2]
    subject = sys.argv[3]
    message = sys.argv[4]
    send_email(addressFrom, addressTo, subject, message)
