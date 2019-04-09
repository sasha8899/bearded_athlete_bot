import telebot
import random
import misc
from telebot import types
import pyowm

token = misc.token
bot = telebot.TeleBot(token)


# @bot.message_handler(commands=["start"])
###Меню 1
# def keybord(message):
#     key = types.ReplyKeyboardMarkup()
#     key.row("1", "2", "3")
#     bot.send_message(message.chat.id, "Выберите цифру", reply_markup=key)
#
# @bot.message_handler(content_types=["text"])
# def main(message):
#     if message.text == "1":
#         bot.send_message(message.chat.id, "Выбрано меню 1")
#     elif message.text == "2":
#         bot.send_message(message.chat.id, "Выбрано меню 2")
#     elif message.text == "3":
#         bot.send_message(message.chat.id, "Выбрано меню 3")
###Меню 1

###Меню 2
@bot.message_handler(commands=["table"])
def inline(message):
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Таблица антропометрии", url="https://docs.google.com/spreadsheets/d/1vRBOLzJmv7TWG6V13bXOICY4HYNwKpstnQF_oQm3UqA/edit#gid=0")
    but_2 = types.InlineKeyboardButton(text="Написать тренеру", callback_data="sendmessage")
    but_3 = types.InlineKeyboardButton(text="Погода", callback_data="weather")
    key.add(but_1, but_2, but_3)
    bot.send_message(message.chat.id, "Выберите необходимый раздел", reply_markup=key)


@bot.callback_query_handler(func=lambda c: True)
def inlin(c):
    if c.data == "sendmessage":
        bot.send_message(c.message.chat.id, "Задавай вопрос @bearded_athlete")
    elif c.data == "weather":
        bot.send_message(c.message.chat.id, "Для отображения погоды воспользуйтесь командой - /weather")
###Меню 2

###Погода

@bot.message_handler(commands=["weather"])
def weather(message):
    city = bot.send_message(message.chat.id, "В каком городе Вам показать погодку?")
    bot.register_next_step_handler(city, weath)


def weath(message):

    import weather


    txt = weather.weathers1(message.text)
    # city = message.text
    bot.send_message(message.chat.id, txt)

###Погода

if __name__ == "__main__":
    bot.polling(none_stop=True)
