import bs4
import requests
from config import *
from bs4 import BeautifulSoup
import telebot as tb

def parsing():
    print(URL)
    response = requests.get(URL)
    soup = BeautifulSoup(response.text,'html.parser')
    print(soup.text)
    # for i_item in soup:
def data_treatment():
    pass
if __name__ == '__main__':
    parsing()
