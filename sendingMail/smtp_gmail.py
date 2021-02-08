import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

message = MIMEMultipart()
message["From"] = "caliskan345599@gmail.com"
message["To"] = "evrem99@hotmail.com"
message["Subject"] = "Smtp Mail"

text = "*** MERVE ÇALIŞKAN ***"

message_body = MIMEText(text,"plain")
message.attach(message_body)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("caliskan345599@gmail.com","evrem1999")
    mail.sendmail(message["From"],message["To"],message.as_string())
    print("Mail was sent successfully.")
    mail.close()
except:
    sys.stderr.write("There's a problem!")
    sys.stderr.flush()
