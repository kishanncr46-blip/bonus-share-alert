import requests
from bs4 import BeautifulSoup
import time

# 🔧 अपने Telegram details डालो
BOT_TOKEN = "8412028159:AAGWGo5WpGHJtJKE5YlA63pS6iBHPm0fRBE"
CHAT_ID = "7354328780"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

def check_bonus_news():
    url = "https://www.bseindia.com/corporates/ann.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.find_all("tr")
    found = False

    for row in rows:
        if "Bonus" in row.text:
            message = f"📢 Bonus Share Alert!\n\n{row.text.strip()}"
            print(message)
            send_telegram_message(message)
            found = True
            break

    if not found:
        print("❌ अभी कोई Bonus announcement नहीं है।")

# 🔁 हर 10 मिनट में चेक करेगा
while True:
    check_bonus_news()
    print("⏳ 10 मिनट बाद फिर से चेक होगा...\n")
    time.sleep(600)
