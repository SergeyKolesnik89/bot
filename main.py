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
keyboard1.row('Анекдот', 'Погода')
keyboard1.row( 'В этот день', 'О разработчиках')
#keyboard1.row('Гороскоп', 'В этот день', 'О разработчиках')



    


        
#Блок погоды
@bot.message_handler(commands=['погода'])
def weather(message):
    
    bot.send_message(message.chat.id,'Введите город . . . ')
       
        
        
           
           
    try:
        
        #place = 'Petropavlovsk'
        if message.text == "привет" or message.text == "Привет":
            pass
        else:
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(message.text)
            print ('1')
            
            
            print ('2')
            w = observation.weather
            print ('3')
            temp = w.temperature('celsius')["temp"]
            print ('4')            
           
             
            answer = (f'В городе {message.text} сейчас { w.detailed_status } '"\n")
            
            bot.send_message(message.chat.id, answer)
            print ('5')
            answer = (f'Температура сейчас в районе  {temp}  градусов Цельсия' "\n\n")
            bot.send_message(message.chat.id, answer)
            print ('6')
            if temp <10:
                answer = "На улице холодно, одевайся очень тепло"
                print ('7')
            elif temp <20:
                answer = "Сейчас прохладно, одевайся теплее"
                print ('8')
            elif temp > 20:
                answer = "Надевай что хочешь, там тепло"
                print ('9')
            bot.send_message(message.chat.id, answer)
            
            print ('10')
    except:
        #bot.send_message(message.chat.id, "Некорректно введен город")
        print ('ошибка блеать')

        



@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200

   


if __name__ == '__main__':
    
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))           








