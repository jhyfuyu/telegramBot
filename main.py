#бот для парсинга заказов
import requests
from config import *
from bs4 import BeautifulSoup
import telebot
import time

orders_list = None

def order_parsing(x):
    while True:
        global orders_list
        response = requests.get(URL)
        soup = BeautifulSoup(response.text,'html.parser')
        orders_list = (soup.find('div',class_="task__title")).text #парсим основную инфу
        return soup
        time.sleep(1800)

def order_info_parsing(resp,flag):
    order_data = (resp.find('span',class_="count")).text
    return order_data

resp = order_parsing(None)
if __name__ == '__main__':
    bot=telebot.TeleBot(TOKEN)
    @bot.message_handler(commands=['start'])

    def data_treatment(message):  # отправка данных в самого бота
        while True:
            bot.send_message(message.from_user.id,orders_list)
            bot.send_message(message.from_user.id, order_info_parsing(resp,False))
            time.sleep(1800)
    bot.infinity_polling()