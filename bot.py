import telebot
import time
import pyshorteners
import os

bot = telebot.TeleBot(token=os.getenv('TG_BOT_TOKEN'))

def short(url):
    return pyshorteners.Shortener().tinyurl.short(url)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, '𝙷𝚊𝚒 𝙳𝚞𝚍𝚎,\n\n𝙸𝚊𝚖  𝚊  𝚜𝚒𝚖𝚙𝚕𝚎  𝙵𝚒𝚕𝚎  𝚃𝚘  𝙻𝚒𝚗𝚔  𝙱𝚘𝚝 . 𝚜𝚎𝚗𝚍  𝚖𝚎  𝚊𝚗𝚢  𝚏𝚒𝚕𝚎  𝙸  𝚠𝚒𝚕𝚕  𝚐𝚒𝚟𝚎 𝚢𝚘𝚞  𝚜𝚑𝚘𝚛𝚝  𝚕𝚒𝚗𝚔.\n\n👲 𝙼𝚊𝚒𝚗𝚝𝚊𝚒𝚗𝚎𝚍  𝙱𝚢 : @BX_Botz')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, '➠ 𝚂𝚎𝚗𝚍  𝙼𝚎  𝙰𝚗𝚢  𝚃𝚢𝚙𝚎  𝙾𝚏  𝙵𝚒𝚕𝚎 \n\n➠ 𝙸  𝚆𝚒𝚕𝚕  𝚂𝚎𝚗𝚍  𝚈𝚘𝚞  𝚂𝚑𝚘𝚛𝚝𝚎𝚗  𝙻𝚒𝚗𝚔\n\n👲 𝙼𝚊𝚒𝚗𝚝𝚊𝚒𝚗𝚎𝚍  𝙱𝚢 : @BX_Botz')    

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

