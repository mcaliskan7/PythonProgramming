import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

with open("mail_listesi","r",encoding="utf-8") as file:
    for kisiBilgisi in file:
        kisiBilgisi = kisiBilgisi[:-1]
        bilgiler = kisiBilgisi.split(",")

        message = MIMEMultipart()
        message["From"] = "username@gmail.com"
        message["To"] = bilgiler[1]
        message["Subject"] = "Smtp Mail"
        text = "Merhaba " + bilgiler[0]
        message_body = MIMEText(text,"plain")
        message.attach(message_body)

        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("username@gmail.com","******")
        mail.sendmail(message["From"],message["To"],message.as_string())
        print("Mail was sent successfully.")
        mail.close()

        try:
            mail = smtplib.SMTP("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login("username@gmail.com","******")
            mail.sendmail(message["From"],message["To"],message.as_string())
            print("Mail was sent successfully.")
            mail.close()
        except:
            sys.stderr.write("There's a problem!\n")
            sys.stderr.flush()

