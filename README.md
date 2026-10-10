# techpulse-bot

Auto-posting for the **Tech Pulse Daily** Telegram channel.

- Claude writes the day's posts each morning and drops them into `queue/`.
- A GitHub Action (`.github/workflows/send.yml`) runs every 15 minutes and sends any post whose time has come, then moves it to `sent/` (or `failed/` with the error).

## Setup
1. Repo secret `TELEGRAM_BOT_TOKEN` = token from @BotFather.
2. `channel.txt` = the channel's username, e.g. `@techpulsedaily`.
3. The bot must be an admin of the channel with "Post Messages" permission.

See `POSTING_GUIDE.md` for the content rules and file format.
