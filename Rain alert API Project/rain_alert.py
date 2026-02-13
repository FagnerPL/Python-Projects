import requests
from twilio.rest import Client

TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""

api_key = ""

parameters = {
    "lat": -23.65607,
    "lon": -46.74256,
    "appid": api_key,
    "lang": "pt_br",
    "units": "metric",
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

it_rain = False
for weather in data["list"]:
    print(f"previsão do tempo: {weather["dt_txt"]}")
    print(f"Temp max: {weather["main"]["temp_max"]} | Temp min: {weather["main"]["temp_min"]}")
    print(f"{weather["weather"][0]["description"].title()}\n")
    if weather["weather"][0]["id"] < 700:
        it_rain = True

if it_rain:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="+12564149725",
        to="+550000000000"
    )

    # message = client.messages.create(
    #     from_="whatsapp:+14155238886",
    #     body="Vai chover hoje viu. Leva um guarda chuva.",
    #     to='whatsapp:+550000000000'
    # )
    # break