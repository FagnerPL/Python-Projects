import datetime as dt
import smtplib
import random
from email.mime.text import MIMEText
from email.header import Header

from dotenv import load_dotenv
import os

load_dotenv()

DEST = os.environ.get("DEST")
PASS = os.environ.get("PASS")

if not EMAIL or not DEST or not PASS:
    raise ValueError("Missing environment variables. Check your .env file")

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
