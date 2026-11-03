import os, requests

token = os.environ["BOT_TOKEN"]
chat_id = os.environ["CHAT_ID"]

requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    data={"chat_id": chat_id, "text": "Бот работает!"},
)