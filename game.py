import random


CHOISES_TUPLE = (("Камень", 0), ("Ножницы", 1), ("Бумага", 2))


def check_choise(user_choise):
    bot_choise = random_choise()
    print(bot_choise)
    return compare_choises(bot_choise,user_choise)


def random_choise():
    random_number = random.randint(0,2)
    for choise in CHOISES_TUPLE:
        if choise[1] == random_number:
            return choise[0]


def compare_choises(bot_choise, user_choise):
    if bot_choise == user_choise:
        return "Бот выбрал: " + bot_choise + "\nНичья"
    if user_choise == CHOISES_TUPLE[0][0]:
        if bot_choise == CHOISES_TUPLE[1][0]:
            return  "Бот выбрал: " + bot_choise + "\nПобеда пользователя!"
        return "Бот выбрал: " + bot_choise + "\nПобеда бота!"
    if user_choise == CHOISES_TUPLE[1][0]:
        if bot_choise == CHOISES_TUPLE[2][0]:
            return  "Бот выбрал: " + bot_choise + "\nПобеда пользователя!"
        return "Бот выбрал: " + bot_choise + "\nПобеда бота!"
    if user_choise == CHOISES_TUPLE[2][0]:
        if bot_choise == CHOISES_TUPLE[0][0]:
            return  "Бот выбрал: " + bot_choise + "\nПобеда пользователя!"
        return "Бот выбрал: " + bot_choise + "\nПобеда бота!"
    return 0
