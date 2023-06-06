#бот для парсинга заказов
import requests
from config import *
from bs4 import BeautifulSoup
import telebot as tb

def order_parsing(x):
    response = requests.get(URL)
    soup = BeautifulSoup(response.text,'html.parser')
    orders_list = soup.find('div',class_="task__title") #парсим основную инфу
    print(orders_list.text,end='. ')
    return soup

def order_info_parsing(resp,info):
    order_data = (resp.find('span',class_="count")).text
    print(order_data)

resp = order_parsing(None)
if __name__ == '__main__':
    # parsing(None)
    def data_treatment():  # отправка данных в самого бота
        pass

