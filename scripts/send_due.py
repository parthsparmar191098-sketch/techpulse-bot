#!/usr/bin/env python3
"""Send queued Tech Pulse Daily posts whose time has come.

Each post is a file in queue/ like:

    send_at: 2026-10-11T08:00:00+05:30
    ---
    <b>Morning Brief</b>
    ...post text (Telegram HTML)...

Due posts are sent to the Telegram channel and moved to sent/.
Posts that fail twice (HTML, then plain text) are moved to failed/.
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUEUE, SENT, FAILED = ROOT / "queue", ROOT / "sent", ROOT / "failed"
MAX_LEN = 4096

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
CHAT_ID = (ROOT / "channel.txt").read_text().strip()


def parse(path):
    raw = path.read_text(encoding="utf-8")
    head, sep, body = raw.partition("\n---\n")
    if not sep:
        raise ValueError("missing '---' line after header")
    meta = {}
    for line in head.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip().lower()] = v.strip()
    when = datetime.fromisoformat(meta["send_at"])
    if when.tzinfo is None:
        raise ValueError("send_at needs a UTC offset, e.g. +05:30")
    return when, body.strip()


def strip_tags(html):
    html = re.sub(r'<a\s+href="([^"]*)"[^>]*>(.*?)</a>', r"\2 (\1)", html, flags=re.S)
    html = re.sub(r"<[^>]+>", "", html)
    return html.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")


def telegram(text, html=True):
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "link_preview_options": {"is_disabled": True},
    }
    if html:
        payload["parse_mode"] = "HTML"
    req = urllib.request.Request(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        try:
            return json.load(e)
        except Exception:
            return {"ok": False, "description": f"HTTP {e.code}"}


def move(path, dest, note=None):
    dest.mkdir(exist_ok=True)
    target = dest / path.name
    text = path.read_text(encoding="utf-8")
    if note:
        text = f"error: {note}\n{text}"
    target.write_text(text, encoding="utf-8")
    path.unlink()


def main():
    if not TOKEN:
        sys.exit("TELEGRAM_BOT_TOKEN secret is not set")
    now = datetime.now(timezone.utc)
    files = sorted(p for p in QUEUE.glob("*.txt"))
    sent = 0
    for path in files:
        try:
            when, body = parse(path)
        except Exception as e:
            print(f"BAD FORMAT {path.name}: {e}")
            move(path, FAILED, f"bad format: {e}")
            continue
        if when > now:
            continue
        if len(body) > MAX_LEN:
            print(f"TOO LONG {path.name}: {len(body)} chars")
            move(path, FAILED, f"too long ({len(body)} chars)")
            continue
        res = telegram(body, html=True)
        if not res.get("ok"):
            print(f"HTML failed for {path.name}: {res.get('description')} -> retry plain")
            res = telegram(strip_tags(body), html=False)
        if res.get("ok"):
            print(f"SENT {path.name}")
            move(path, SENT)
            sent += 1
        else:
            print(f"FAILED {path.name}: {res.get('description')}")
            move(path, FAILED, res.get("description"))
    print(f"done: {sent} sent, {len(list(QUEUE.glob('*.txt')))} still queued")


if __name__ == "__main__":
    main()
