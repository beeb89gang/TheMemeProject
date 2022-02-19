from telegram.ext import *
from dotenv import load_dotenv
import os
from os.path import join, dirname
import redditpraw

env_file = join(dirname(__file__), '.env')
load_dotenv(env_file)
telegram_secret = os.environ.get("telegram_key")

def start_command(update, context):
    name = update.message.chat.first_name
    update.message.reply_text("Ciao " + name)
    update.message.reply_text("Invia un immagine")

def image_handler(update, context):
    name = update.message.chat.first_name
    date = update.message.date.date()
    file = update.message.photo[-1].get_file()
    file.download(f"{name}_{date}.jpg")
    
    update.message.reply_text("Immagine ricevuta")

def echo(update, context):
    file = update.message.animation.get_file()
    file.download("culo.mp4")
    #print(update.message)
    update.message.reply_text("Culo")

def reddit_handler(update, contex):
    print(update.message.text)
    for i in update.message.entities:
        print(i)
        url = update.message.text[i["offset"]:i["offset"]+i["length"]]
        try:
            redditpraw.reddit_image_succ(url)
        except:
            update.message.reply_text("HOOOOOOOOH dude its not reddit")
    update.message.reply_text("69 nice")

def main():
    print("Started")
    TOKEN = telegram_secret
    updater = Updater(TOKEN, use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))

    dp.add_handler(MessageHandler(Filters.photo, image_handler))
    #handler per test, non fa altro che ripetere quello che dici
    #dp.add_handler(MessageHandler(Filters.text,echo))

    dp.add_handler(MessageHandler(Filters.animation,echo))
    dp.add_handler(MessageHandler(Filters.entity('url'),reddit_handler))

    updater.start_polling()
    updater.idle()

    

if __name__ == '__main__':
    main()
