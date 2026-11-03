import os, requests

TOKEN = os.environ["BOT_TOKEN"]
API = f"https://api.telegram.org/bot{TOKEN}"

def reply(text):
    t = (text or "").strip()
    if t.startswith("/start"):
        return "Привет! Я бот. Напиши что-нибудь."
    if t.startswith("/help"):
        return "Команды: /start, /help, /ping"
    if t.startswith("/ping"):
        return "pong"
    return f"Ты написал: {t}"

updates = requests.get(f"{API}/getUpdates", timeout=30).json().get("result", [])

for u in updates:
    msg = u.get("message")
    if msg and "text" in msg:
        requests.post(f"{API}/sendMessage", data={
            "chat_id": msg["chat"]["id"],
            "text": reply(msg["text"]),
        })

if updates:
    last = updates[-1]["update_id"]
    requests.get(f"{API}/getUpdates", params={"offset": last + 1})