import logging
# import requests
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler, Filters, MessageHandler, Updater

# from url_editor import create_url
# from log import create_log_message
import game, settings

logging.basicConfig(
    filename="bot.log",
    format='%(asctime)s - %(levelname)s - %(message)s', 
    datefmt='%d-%b-%y %H:%M:%S', 
    level=logging.INFO
    )

#PROXY = {'proxy_url': settings.PROXY_URL,
#    'urllib3_proxy_kwargs':{'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}


def start_game(update, context):
    reply_keyboard = [['Камень', 'Ножницы', 'Бумага', 'Конец']]
    update.message.reply_text(
        'Это игра "камень, ножницы, бумага".\n'
        'Отправь /cancel или нажми "Конец" чтобы остановить игру.\n\n'
        'Выбирайте:',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, 
            one_time_keyboard=True
        )
    )
    return "play_round"

def play_round(update, context):
    try:
        if update.message.text == 'Конец':
            update.message.reply_text(
                'Конец игры.', reply_markup=ReplyKeyboardRemove()
            )
            return ConversationHandler.END
        update.message.reply_text(
            game.check_choise(update.message.text)
        )
    except:
        print(update.message.text)
    reply_keyboard = [['Камень', 'Ножницы', 'Бумага', 'Конец']]
    update.message.reply_text(
        'Выбирайте:',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True
        )
    )
    return "play_round"



#    print("Вызван /start")
#    message = create_log_message(update)
#    logging.info(message)
#    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')


def cancel(update, context):
    update.message.reply_text(
        'Конец игры.', reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


# def find(update, context):
#     print("Вызван /find")
#     message = create_log_message(update)
#     logging.info(message)
#     obj_find = str(update.message.text).split('/find ')
#     try:
#         text = "Поиск " + obj_find[1]
#         logging.info(text)
#         update.message.reply_text(text)
#         url = create_url(obj_find[1])
#         r = requests.get(url)
#         print(r.text)
#     except (TypeError, IndexError):
#         text = "Некорректный запрос. Для поиска введите команду и укажите искомое место. Пример: /find 'объект поиска'"
#         update.message.reply_text(text)
#         logging.error()


#def talk_to_me(update, context):
#    try:
#        print(context.args)
#        if update.message.text.lower() == "игра":
#            update.message.reply_text("Начинаю игру!")
#            logging.info("play game")
#    except:
#        print("error")

# def play_jkp(update, context):
#     print("Вызван /play_jkp")


def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher

    game_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start_game", start_game)],
        states={
            "play_round":[MessageHandler(Filters.regex('^(Камень|Ножницы|Бумага|Конец)$'), play_round)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    # dp.add_handler(CommandHandler("find", find))
    # dp.add_handler(CommandHandler("play_jkp", play_jkp))
#    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(game_conv_handler)
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()
    logging.info("Бот остановлен")

if __name__ == "__main__":
    main()