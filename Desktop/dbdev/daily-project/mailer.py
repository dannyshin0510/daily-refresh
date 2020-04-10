import smtplib
import config 
import main
from email.message import EmailMessage
from pathlib import Path

msg = EmailMessage()
msg['Subject'] = "Daily Alerts"
msg['From'] = config.EMAIL_ADDRESS
msg['To'] = "shindannybms@gmail.com"


path = Path(__file__).parent / "template\mail.html"
htmlFile = path.open('r', encoding="utf-8")
source_code = htmlFile.read()
htmlFile.close()
msg.add_alternative(str(source_code), subtype='html')

def sendEmail(message):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        # message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.send_message(message)
        server.quit()
        print("Email sent successfully")
    except:
        print("Email failed to send")


sendEmail(msg)