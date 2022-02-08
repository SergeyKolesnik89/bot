import os

from flask import Flask, request
#телебот
import telebot
#случайности для анекдота
import random
import sqlite3 as sql
import sqlite3

#блок событий


from bs4 import BeautifulSoup
import requests

#для погоды
import pyowm 
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps



#Дата и время
import datetime as dt

import time
import datetime as dt
import sys
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types


TOKEN = "1094693261:AAERSOmcqWAp38SMxc6Wbou_S8wTQsuLu8s"
APP_URL = f'https://belka418.herokuapp.com//{TOKEN}'

#https://belka418.herokuapp.com/
#https://belka418.herokuapp.com/
#bot = telebot.TeleBot("1094693261:AAERSOmcqWAp38SMxc6Wbou_S8wTQsuLu8s")
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)




owm = OWM('b71a7de29575570f5971685c60ef5628')
owm.config["language"] = "ru"

keyboard1 = types.InlineKeyboardMarkup()
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Анекдот', 'weather')
keyboard1.row( 'today', 'О разработчиках')
#keyboard1.row('Гороскоп', 'В этот день', 'О разработчиках')



    


        
#Блок погоды
@bot.message_handler(commands=['today'])
def today(message):
    
     
    URL = 'https://kakoysegodnyaprazdnik.ru/'
    HEADERS = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
    }
    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
        
    items = soup.findAll('div', class_='main')
    comps = []

    for item in items:
        comps.append({
        'title' : item.find('span').get_text(strip = True)
                            
         })

    global comp
    for comp in comps:
        bot.send_message(message.chat.id,(f'{comp["title"]}  '))
        print (f'{comp["title"]}  ')

        
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)



@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200

   



if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000))) 




bot.polling(none_stop=True, interval=0)

input() 






