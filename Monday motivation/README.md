# 📧 Monday Motivation

Automatically sends a random motivational quote via email every Monday morning.

## How it works

1. Reads a list of motivational phrases from `phrases.txt`
2. Picks a random phrase
3. Checks if today is Monday
4. If so, sends an email with the phrase to the destination address

## Requirements

- Python 3.x
- `python-dotenv` library

Install dependencies:

    pip install python-dotenv

## Configuration

Create a `.env` file in the project folder:

    EMAIL=your@email.com
    DEST=destination@email.com
    PASS=your_app_password

For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833) instead of your regular password.

## Usage

    python main.py

For best results, schedule this script to run every Monday morning using a task scheduler like `cron` (Linux/macOS) or Task Scheduler (Windows).

## Built With

- `smtplib` — built-in Python email library
- `python-dotenv` — environment variable management

## License

MIT