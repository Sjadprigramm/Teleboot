import os
import subprocess
import sys
import telebot
import time

# دالة لتحميل المكتبة إذا لم تكن موجودة
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# قائمة بالمكتبات المطلوبة
required_packages = ["pyTelegramBotAPI"]

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        install(package)

# توكن البوت
bot = telebot.TeleBot("7702360621:AAFEOfyYjfZ09c7n1EYPgoWRFwTHNqlQTYs")

def typing_message(chat_id, text, typing_speed=0.1):
    """دالة ترسل النص كأنه يتم كتابته ببطء"""
    message = ""
    msg = bot.send_message(chat_id, " ")
    for char in text:
        message += char
        bot.edit_message_text(message, chat_id, message_id=msg.message_id)
        time.sleep(typing_speed)

@bot.message_handler(commands=['start'])
def welcome_message(message):
    chat_id = message.chat.id
    welcome_text = "أهلا وسهلا بك في البوت! 👋\nهذا بوت ترحيب بسيط. إذا عندك أي استفسار لا تتردد تسألني 😊"
    typing_message(chat_id, welcome_text)

bot.polling()