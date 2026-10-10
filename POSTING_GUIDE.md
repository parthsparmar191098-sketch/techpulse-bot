# Tech Pulse Daily – Posting Guide

Instructions for the daily run that writes the channel's posts.

## Channel
- Name: **Tech Pulse Daily** (Telegram channel)
- Language: **English** — simple, clear, no jargon without a short explanation
- Audience: curious readers worldwide who want global tech news in a few minutes

## Daily schedule (IST, +05:30)
| Time  | Post | What goes in it |
|-------|------|-----------------|
| 08:00 | 🌍 Morning Brief | Top 5 global tech headlines from the last 24 hours, one line each + source link |
| 12:30 | 🤖 AI / Robotics | One important AI or robotics story, explained in 120–200 words |
| 17:00 | 🚀 Space / 🛡️ Defence / 🔬 Science | Rotate by weekday: Mon/Thu Space, Tue/Fri Defence tech, Wed/Sat Science, Sun pick the biggest |
| 20:30 | 💡 Did You Know | One surprising, verified tech or science fact, 2–4 sentences |

If there is no good story for a slot, skip that slot. Never post filler.

## Research rules
- Only stories from the last 24–36 hours (Did You Know can be timeless).
- Prefer original or reputable sources: company/agency announcements (NASA, ESA, ISRO, SpaceX, OpenAI, Google, Anthropic, Nvidia…), Reuters, AP, BBC, The Verge, TechCrunch, Ars Technica, Wired, MIT Technology Review, Space.com, Nature, ScienceDaily.
- Check key numbers and claims against at least two sources when possible.
- Defence: official or reputable reporting only; no rumours, leaks or unverified videos.
- No investment advice, no stock tips, no medical advice.
- Don't repeat a story already posted in the last 3 days (check `sent/`).

## Writing rules
- Write everything in your own words. Never copy sentences from articles; quotes, if any, under 15 words.
- End every post with source link(s): `<a href="URL">Source</a>`.
- Keep posts short: Morning Brief ≤ 900 characters, others ≤ 1200 characters (hard limit 4096).
- Telegram HTML only: `<b>`, `<i>`, `<u>`, `<s>`, `<a href="">`, `<code>`, `<blockquote>`. Escape `&`, `<`, `>` in normal text as `&amp;`, `&lt;`, `&gt;`.
- One or two emojis per post, not more.
- Footer on every post: `\n\n📡 @CHANNEL` (use the username in `channel.txt`).

## File format
Create one file per post in `queue/`, named `YYYY-MM-DD_HHMM_slot.txt`, e.g. `queue/2026-10-11_0800_brief.txt`:

```
send_at: 2026-10-11T08:00:00+05:30
---
<b>🌍 Morning Brief – 11 Oct</b>

1. ...
```

Commit and push to `main`. The GitHub Action checks every 15 minutes and sends posts whose time has passed.
