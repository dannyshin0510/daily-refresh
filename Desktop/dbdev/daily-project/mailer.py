import smtplib
import config 
import time
import covid_api
from email.message import EmailMessage
from pathlib import Path
import datetime
ALARM_ACTIVATED = True

def sendEmail(message):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        server.send_message(message)
        server.quit()
        print("SUCCESS: Notification sent successfully to: " + msg['To'])
    except:
        print("ERROR: Notification failed to send")

def createMessage(destination, msg):
    msg['Subject'] = "Daily Alerts"
    msg['From'] = config.EMAIL_ADDRESS
    msg['To'] = destination
    path = Path(__file__).parent / "template\mail.html"
    htmlFile = path.open('r', encoding="utf-8")
    source_code = str(htmlFile.read())%(covid_api.canCases, covid_api.canDeaths, covid_api.torCases, covid_api.torDeaths)
    htmlFile.close()
    msg.add_alternative(str(source_code), subtype='html')

# execution of program
alarmHour = 20
alarmMin = 36
print("ALARM: active...")
while (ALARM_ACTIVATED):
    time.sleep(60)
    if (datetime.datetime.now().hour == alarmHour and datetime.datetime.now().minute == alarmMin):
        print("MESSAGE: Alarm has been Triggered")
        for destination in config.EMAIL_DESTINATIONS:
            msg = EmailMessage()
            createMessage(destination, msg)
            sendEmail(msg)
        break
print("Operation Completed")
        

    
