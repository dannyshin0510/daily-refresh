import smtplib
import config 
import main

def sendEmail(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, "shindannybms@gmail.com", message)
        server.quit()
        print("Email sent successfully")
    except:
        print("Email failed to send")
subject="TEST EMAIL" 
msg="Today's current  " + str(main.number)

sendEmail(subject, msg)