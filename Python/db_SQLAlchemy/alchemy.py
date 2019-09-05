from sqlalchemy import *
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import create_session
from Python.db_SQLAlchemy.pwrd.pwrd import password
import os

connection_info = {
    'drivername': 'mysql+pymysql',
    'database': 'db_newsilpo_dev1',
    'host': '10.10.16.202',
    'port': '3306',
    'username': 'a-b.shvets',
    'password': password
}

url = URL(**connection_info)  # Создание урла коннекшина

file = "C:\\Work\\Projects\\DK-09-2019\\Python\\db_SQLAlchemy\\db_meta_container\\db_metadata.py"
os.system('sqlacodegen --outfile {} {}'.format(file, url))  # создание файла с метаданными базы

Base = declarative_base()
engine = create_engine(url)         # подключение к базе

metadata = MetaData(bind=engine)    # метаданные в переменной
conn = engine.connect()             # соединение в переменной

session = create_session(bind=engine)       # создание соединения на основе подключения


