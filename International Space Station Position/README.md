# 🛸 ISS Tracker — International Space Station Alert

Tracks the real-time position of the International Space Station (ISS) 
and sends an email alert when it passes over your location at night.

## How it works

1. Fetches the current ISS position via the [Open Notify API](http://api.open-notify.org/iss-now.json)
2. Checks if the ISS is within 5 degrees of your coordinates
3. Checks if it is currently night at your location via the [Sunrise-Sunset API](https://sunrise-sunset.org/api)
4. If both conditions are met, sends an email alert

## Requirements

- Python 3.x
- `requests` library

```bash
pip install requests
```

## Configuration

Open `main.py` and update the following variables:

```python
MY_LAT = -23.656202   # your latitude
MY_LNG = -46.742464   # your longitude
```

Update the email credentials:

```python
connection.login(user="your@email.com", password="your_password")
```

> For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833) 
> instead of your regular password.

## Usage

```bash
python main.py
```

> For best results, schedule this script to run every 60 seconds 
> using a task scheduler like `cron` (Linux/macOS) or Task Scheduler (Windows).

## Built With

- [Open Notify API](http://api.open-notify.org/) — real-time ISS position
- [Sunrise-Sunset API](https://sunrise-sunset.org/api) — sunrise and sunset times
- `smtplib` — built-in Python email library

## License

MIT