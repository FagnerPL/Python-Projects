import requests
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.environ.get("TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
API_KEY = os.environ.get("API_KEY")

if not TOKEN or not CHAT_ID or not API_KEY:
    raise ValueError("Missing environment variables. Check your .env file")

# Telegram
message = "It's going to rain today. Remember to bring an ☔"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"

# OpenWeather
parameters = {
    "lat": -23.65607,
    "lon": -46.74256,
    "appid": API_KEY,
    "lang": "pt_br",
    "units": "metric",
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

it_rain = False
for weather in data["list"]:
    print(f"previsão do tempo: {weather['dt_txt']}")
    print(f"Temp max: {weather['main']['temp_max']} | Temp min: {weather['main']['temp_min']}")
    print(f"{weather['weather'][0]['description'].title()}\n")
    if weather['weather'][0]['id'] < 700:
        it_rain = True

if it_rain:
    requests.get(url)