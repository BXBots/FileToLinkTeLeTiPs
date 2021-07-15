import telebot
import time
import pyshorteners
import os

bot = telebot.TeleBot(token=os.getenv('TG_BOT_TOKEN'))

def short(url):
    return pyshorteners.Shortener().tinyurl.short(url)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hai, \n\n`Iam a simple File To Link Bot.send me any file I will give you short link`\n\n👲 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : [ʙx ʙᴏᴛᴢ](https://t.me/BX_Botz)')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Send me any type of a file & I will send you the shorten link of it')    

@bot.message_handler(content_types=['photo', 'video', 'audio', 'document'])
def file_sent(message):
    try:
        bot.send_message(message.chat.id, short(bot.get_file_url(message.document.file_id)))
    except AttributeError:
        try:
            bot.send_message(message.chat.id, short(bot.get_file_url(message.photo[0].file_id)))
        except AttributeError:
            try:
                bot.send_message(message.chat.id, short(bot.get_file_url(message.audio.file_id)))
            except AttributeError:
                try:
                    bot.send_message(message.chat.id, short(bot.get_file_url(message.video.file_id)))
                except AttributeError:
                    pass


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)

