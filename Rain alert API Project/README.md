# 🌧️ Rain Alert

Checks the weather forecast for your location and sends a Telegram message
if it's going to rain during the day.

## How it works

1. Fetches the next 12 hours weather forecast via OpenWeather API
2. Checks if any forecast has a weather code below 700 (rain, snow, storm)
3. If so, sends a Telegram message warning you to bring an umbrella

## Requirements

- Python 3.x
- `requests` library
- `python-dotenv` library

Install dependencies:

    pip install requests python-dotenv

## Configuration

Create a `.env` file in the project folder:

    TOKEN=your_telegram_bot_token
    CHAT_ID=your_telegram_chat_id
    API_KEY=your_openweather_api_key

To create a Telegram Bot and get your TOKEN, talk to [@BotFather](https://t.me/BotFather) on Telegram.

To get your CHAT_ID, send a message to your bot and access:

    https://api.telegram.org/bot<TOKEN>/getUpdates

## Usage

    python main.py

For best results, schedule this script to run every morning using
a task scheduler like `cron` (Linux/macOS) or Task Scheduler (Windows).

## Built With

- [OpenWeather API](https://openweathermap.org/api) — weather forecast data
- [Telegram Bot API](https://core.telegram.org/bots/api) — message delivery
- `python-dotenv` — environment variable management

## License

MIT