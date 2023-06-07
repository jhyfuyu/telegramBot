#бот для парсинга заказов
import requests
from config import *
from bs4 import BeautifulSoup
import telebot
import time

orders_list = None
def order_parsing():
    old_value = None
    global orders_list

    while True:
        response = requests.get(URL)
        soup = BeautifulSoup(response.text,'html.parser')
        orders_list = (soup.find('div',class_="task__title")).text #парсим основную инфу
        list1 = [soup,orders_list]
        orders_list = new_value
        if new_value != old_value:
            return list1
            orders_list = old_value
        time.sleep(300)


def order_info_parsing(flag):
    initialDataForParsing = order_parsing()
    order_data = (initialDataForParsing[0].find('span',class_="count")).text
    return order_data


if __name__ == '__main__':
    bot=telebot.TeleBot(TOKEN)
    @bot.message_handler(commands=['start'])

    def data_treatment(message):  # отправка данных в самого бота
        bot.send_message(message.from_user.id, "Добрый день, Меня зовут Глэм, я ваш бот для поиска заказов")
        def sending_message(o_parameter,oi_parameter):
            while True:
                order_name = o_parameter
                bot.send_message(message.from_user.id,order_name[1])
                bot.send_message(message.from_user.id, oi_parameter)
                time.sleep(1800)
        sending_message(order_parsing(),order_info_parsing(False))
    bot.infinity_polling()