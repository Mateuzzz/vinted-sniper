import threading
from telegram import Bot

def SendMessage(BOT_TOKEN, CHAT_ID, new_item):
    bot = Bot(token=BOT_TOKEN)
    def send_message():
        bot.send_message(chat_id=CHAT_ID, text=new_item, parse_mode="HTML")

    threading.Thread(target=send_message).start()