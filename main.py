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
        return list1
        time.sleep(1800)


def order_info_parsing(flag):
    initialDataForParsing = order_parsing()
    order_data = (initialDataForParsing[0].find('span',class_="count")).text
    return order_data


if __name__ == '__main__':
    bot=telebot.TeleBot(TOKEN)
    @bot.message_handler(commands=['start'])

    def data_treatment(message):  # отправка данных в самого бота
        while True:
            order_name = order_parsing()
            bot.send_message(message.from_user.id,order_name[1])
            bot.send_message(message.from_user.id, order_info_parsing(False))
            time.sleep(1800)
    bot.infinity_polling()