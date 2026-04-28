import datetime as dt
import smtplib
import random
from email.mime.text import MIMEText
from email.header import Header


EMAIL = ""
DEST = ''
PASS = ""

with open("phrases.txt") as file:
    data = file.readlines()
    phrase = random.choice(data)

msg = MIMEText(phrase, "plain", "utf-8")
msg['From'] = EMAIL
msg['To'] = DEST
msg['Subject'] = Header('Monday Motivation 🫵🏿 🤏🏿', 'utf-8')

now = dt.datetime.now()

if now.weekday() == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASS)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=DEST,
            msg=msg.as_string()
        )
