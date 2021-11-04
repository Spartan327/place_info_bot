import logging
from log import create_log_message
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(
    filename="bot.log",
    format='%(asctime)s - %(levelname)s - %(message)s', 
    datefmt='%d-%b-%y %H:%M:%S', 
    level=logging.INFO
    )

#PROXY = {'proxy_url': settings.PROXY_URL,
#    'urllib3_proxy_kwargs':{'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}


def greet_user(update, context):
    print("Вызван /start")
    message = create_log_message(update)
    logging.info(message)
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def talk_to_me(update, context):
    text = update.message.text
    update.message.reply_text(text)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()
    logging.info("Бот остановлен")

if __name__ == "__main__":
    main()