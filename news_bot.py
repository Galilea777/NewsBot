import os
import feedparser
import requests
from datetime import datetime

# 🔹 Replace these with your actual values
TELEGRAM_BOT_TOKEN = "8177080880:AAEzDFcpClbpgqYmxj0MlhtBxk8Nsmdcw6o"  # From BotFather
TELEGRAM_CHAT_ID = "8027281580"  # Found using getUpdates

# 🔹 AI News RSS Feed URL
rss_url = "https://news.google.com/rss/search?q=Artificial+Intelligence&hl=en"
feed = feedparser.parse(rss_url)

# 🔹 Create a formatted message
message = f"📰 *AI News Update - {datetime.now().strftime('%B %d, %Y')}*\n\n"

if feed.entries:
    for i, entry in enumerate(feed.entries[:5]):  # Sends top 5 articles
        message += f"{i+1}. [{entry.title}]({entry.link})\n\n"
else:
    message += "No news available today."

# 🔹 Send news to Telegram
url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
params = {
    "chat_id": TELEGRAM_CHAT_ID,
    "text": message,
    "parse_mode": "Markdown"
}
response = requests.get(url, params=params)

# 🔹 Check if the message was sent successfully
if response.status_code == 200:
    print("✅ AI News sent to Telegram!")
else:
    print("❌ Failed to send news:", response.text)
