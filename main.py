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






        







   


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))           








