# Telegram Bot Starter (Aiogram v3)

A clean starter template for a Telegram bot using **Aiogram v3** (polling). Loads token from `.env`, registers basic commands, and runs with logging enabled.

## Quickstart

1) Create a bot with @BotFather and copy the token.
2) Clone this repo and set up environment:
```bash
python -m pip install -r requirements.txt
cp .env.example .env   # Windows: copy .env.example .env
# Edit .env and paste your token
```
3) Run:
```bash
python -m bot.main
```

## Features
- Aiogram v3 with `Dispatcher` + `Router`
- `/start` and `/help` commands
- Simple echo fallback
- Environment variables via `python-dotenv`

## Files
- `bot/main.py`: entrypoint
- `.env.example`: sample environment

## Production Notes
- Prefer Webhook in production; this template uses polling for simplicity.
- Add rate limiting, persistence (DB/Redis) as needed.
