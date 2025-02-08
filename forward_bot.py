import requests

# Replace these with your actual bot tokens
FORWARD_BOT_TOKEN = "7590032089:AAGPcypOUnYHzT39j2SVTHcfJ1T_sNa_Ryw"
ARTICLEX_BOT_TOKEN = "7880727134:AAEVsfspPNTyBA9hJVBW80JMInOs0TFGxvs"

# Replace with the chat ID where NewsBot sends messages
NEWSBOT_CHAT_ID = 8177080880  # Update with your actual chat ID

# Get new messages from NewsBot
def get_newsbot_messages():
    url = f"https://api.telegram.org/bot{FORWARD_BOT_TOKEN}/getUpdates"
    response = requests.get(url).json()
    
    messages = []
    if "result" in response:
        for update in response["result"]:
            if "message" in update and update["message"]["chat"]["id"] == NEWSBOT_CHAT_ID:
                messages.append(update["message"]["text"])
    
    return messages

# Send messages to ArticleX
def send_to_articlex(message):
    url = f"https://api.telegram.org/bot{ARTICLEX_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": NEWSBOT_CHAT_ID, "text": message}
    requests.post(url, data=payload)

# Main function to forward messages
def forward_messages():
    messages = get_newsbot_messages()
    for msg in messages:
        send_to_articlex(msg)

if __name__ == "__main__":
    forward_messages()
