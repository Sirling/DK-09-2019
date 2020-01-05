from sqlalchemy import *
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import create_session
from Python.db_SQLAlchemy.pwrd.pwrd import password
import os

# Урл подключения
from Silpo.src.back.DB import DataBase

connection_info = {
    'drivername': 'mysql+pymysql',
    'DB': 'db_newsilpo_dev1',
    'host': '10.10.16.202',
    'port': '3306',
    'username': 'a-b.shvets',
    'password': password
}
# Создание урла подключения
url = URL(**connection_info)
# Файл метаданных
file = "..\\DataBase.py"
# Создание файла с метаданными базы
os.system('sqlacodegen --outfile {} {}'.format(file, url))

Base = DataBase.Base
# Подключение к базе
engine = create_engine(url)
# Метаданные в переменной
metadata = DataBase.metadata
# Соединение в переменной
conn = engine.connect()

# Создание соединения на основе подключения
session = create_session(bind=engine)
