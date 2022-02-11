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



    
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)
    bot.send_message(message.from_user.id, "Я сказала стартуем )))",  reply_markup=keyboard1)
        

@bot.message_handler(content_types=['text'])
    
def jokes_text(message):
    
    if message.text.lower() == 'анекдот':
        con = sql.connect('anekdot.db')
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS 'test' ('number' INT, 'name' STRING)")
    
            cur.execute("SELECT * FROM 'test' ORDER BY RANDOM() LIMIT 1")
                
            rows = cur.fetchmany()
                
            for row in rows:
                    
                    
                bot.send_message(message.chat.id,row[0])



          
        con.commit()
        cur.close()

    

#Блок приветствия
    elif message.text == 'Привет':
        bot.send_message(message.from_user.id, 'О, привет, меня зовут Белка_bot и у меня лапки ^^ ')

    elif message.text.lower() == 'о разработчиках':
        bot.send_message(message.from_user.id, 'Мы скромные *_*')

#Блок событий

    elif message.text == '/start':
        bot.send_message(message.from_user.id, "Я сказала стартуем )))",  reply_markup=keyboard1)
    
    elif message.text == 'В этот день':
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
            
            



    


        
#Блок погоды
            
    elif message.text.lower() == 'Погода':
        bot.send_message(message.from_user.id,'Введите город . . . ')
        if message.text == "привет" or message.text == "Привет":
            pass
        else:
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(message.text)
              


                
            w = observation.weather
                
            temp = w.temperature('celsius')["temp"]
                          


            answer = (f'В городе {message.text} сейчас { w.detailed_status } '"\n")

            bot.send_message(message.chat.id, answer)
               
            answer = (f'Температура сейчас в районе  {temp}  градусов Цельсия' "\n\n")
            bot.send_message(message.chat.id, answer)
                
            if temp <10:
                answer = "На улице холодно, одевайся очень тепло"
                    
            elif temp <20:
                answer = "Сейчас прохладно, одевайся теплее"
                    
            elif temp > 20:
                answer = "Надевай что хочешь, там тепло"
                    
            bot.send_message(message.chat.id, answer)

                  
        
        
           
           
    #try:
    
            
            
    #except:
        #bot.send_message(message.chat.id, "Некорректно введен город")
       
            


@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200

   



if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000))) 








