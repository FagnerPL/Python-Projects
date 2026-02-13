import requests
from datetime import datetime
import smtplib

MY_LAT = -23.656202
MY_LNG = -46.742464

def compare_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
#Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_latitude <= MY_LNG+5:
        return True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
    "tzid": "America/Sao_Paulo"
}

def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour > sunset or time_now.hour < sunrise:
        return True


#If the ISS is close to my current position
if compare_position() and is_night():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="email", password="password")
        connection.sendmail(
            from_addr="email",
            to_addrs="email",
            msg="Subject:LOOK UP ☝️\n\nThe International Space Station is above you now. Look up."
        )



