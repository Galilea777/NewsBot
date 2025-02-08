import requests
import telebot

# NewsBot Token
NEWSBOT_TOKEN = "YOUR_NEWSBOT_TOKEN"
bot = telebot.TeleBot(NEWSBOT_TOKEN)

# ArticleX Chat ID (replace with the actual ID you found in Step 1)
ARTICLEX_CHAT_ID = "953116189"

# Function to send articles to ArticleX
def send_articles_to_articlex(articles):
    message = "\n".join(articles)
    url = f"https://api.telegram.org/bot{NEWSBOT_TOKEN}/sendMessage"
    data = {"chat_id": ARTICLEX_CHAT_ID, "text": message}
    requests.post(url, data=data)

# Example: Fetching 5 AI news articles (This is where your scraping logic is)
articles = [
    "Breaking: AI-powered tool revolutionizes healthcare with early disease detection.",
    "New AI model outperforms GPT-4 in creative writing tasks.",
    "Top trends in AI for 2025: What you need to know.",
    "AI startup raises $100M to build autonomous robotic systems.",
    "Debate intensifies over AI ethics in decision-making processes."
]

# Send the articles to ArticleX
send_articles_to_articlex(articles)

# Run the bot
bot.polling()
