# Tech Pulse Daily – Posting Guide

Instructions for the daily run that writes the channel's posts.

## Channel
- Name: **Tech Pulse Daily** (Telegram channel)
- Language: **English** — simple, clear, no jargon without a short explanation
- Audience: curious readers worldwide who want global tech news in a few minutes

## Daily post: one Daily Digest at 08:00 IST
Post ONE message per day, sent at 08:00 IST (+05:30), covering the last 24 hours:

```
<b>⚡ Tech Pulse Daily | 11 Oct</b>

<b>🤖 AI</b>
• One-line summary in your own words. <a href="URL">Source</a>
• ...

<b>🚀 Space</b>
• ...

<b>🛡️ Defence Tech</b>
• ...

<b>🔬 Science</b>
• ...

<b>⚙️ Robotics &amp; Automation</b>
• ...

<b>📱 Gadgets &amp; Big Tech</b>
• ...

<b>💡 Did You Know?</b>
One verified, surprising tech or science fact in 1–2 sentences.

📡 @CHANNEL
```

- 1–2 stories per section, 8–10 stories in total. Each bullet is 1–2 short lines.
- Skip a section if there's no good story that day. Never add filler.
- Whole message must stay under 3,800 characters (Telegram's hard limit is 4,096).
- File name: `queue/YYYY-MM-DD_0800_digest.txt`. If 08:00 has already passed when the run happens, set send_at to the current time plus 5 minutes.

## Research rules
- Only stories from the last 24–36 hours (Did You Know can be timeless).
- Prefer original or reputable sources: company/agency announcements (NASA, ESA, ISRO, SpaceX, OpenAI, Google, Anthropic, Nvidia…), Reuters, AP, BBC, The Verge, TechCrunch, Ars Technica, Wired, MIT Technology Review, Space.com, Nature, ScienceDaily.
- Check key numbers and claims against at least two sources when possible.
- Defence: official or reputable reporting only; no rumours, leaks or unverified videos.
- No investment advice, no stock tips, no medical advice.
- Don't repeat a story already posted in the last 3 days (check `sent/`).

## Writing rules
- Write everything in your own words. Never copy sentences from articles; quotes, if any, under 15 words.
- Every bullet ends with its source link: `<a href="URL">Source</a>`.
- Telegram HTML only: `<b>`, `<i>`, `<u>`, `<s>`, `<a href="">`, `<code>`, `<blockquote>`. Escape `&`, `<`, `>` in normal text as `&amp;`, `&lt;`, `&gt;`.
- Emojis only in the section headings shown above, not inside bullets.
- Footer on every post: `\n\n📡 @CHANNEL` (use the username in `channel.txt`).

## File format
Create the digest as one file in `queue/`, e.g. `queue/2026-10-11_0800_digest.txt`:

```
send_at: 2026-10-11T08:00:00+05:30
---
<b>⚡ Tech Pulse Daily | 11 Oct</b>

<b>🤖 AI</b>
• ...
```

Commit and push to `main`. The GitHub Action checks every 15 minutes and sends posts whose time has passed.
