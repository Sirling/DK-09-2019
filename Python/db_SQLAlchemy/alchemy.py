from sqlalchemy import *
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import create_session
from Python.db_SQLAlchemy.pwrd.pwrd import password
import os

connection_info = {
    'drivername':'mysql+pymysql',
    'database':'db_newsilpo_dev1',
    'host':'10.10.16.202',
    'port':'3306',
    'username':'a-b.shvets',
    'password':password
}

url = URL(**connection_info) #Создание урла коннекшина

file = "C:\Work\Projects\DK-09-2019\Python\db_SQLAlchemy\db_meta_container\db_metadata.py"
os.system('sqlacodegen --outfile {} {}'.format(file, url)) # создание файла с метаданными базы

Base = declarative_base()
engine = create_engine(url)         # подключение к базе

metadata = MetaData(bind=engine)    # метаданные в переменной
conn = engine.connect()             # соединение в переменной

class hr_vacancies(Base):
    __table__ = Table('hr_vacancy', metadata, autoload=True)

class product_store(Base):
    __table__ = Table('product_store', metadata, autoload=True)

class product(Base):
    __table__ = Table('product', metadata, autoload=True)

class store(Base):
    __table__ = Table('store', metadata, autoload=True)

session = create_session(bind=engine)       # создание соединения на основе подключения

def select_vacancy():
    vacancies = session.query(hr_vacancies).filter(hr_vacancies.manager_name == "Опанас")
    for row in vacancies:
        print(row.contact_one)

def select_product_and_store():
    """
    Поиск продуктов и магазинов, в которых они продаються
    Автоматический джоин через транзитную таблицу
    """
    result = session.query(product.title, func.count(store.title))\
        .filter(store.title.like("%Тор%"))\
        .group_by(product.title)\
        .limit(10)
    for row in result:
        print(row)

def select_force_join():
    """
    Тот же запрос, только через принудительный джоин
    """
    result = session.query(product.title, func.count(store.title))\
        .join(product_store, product.id==product_store.product_id)\
        .join(store, store.id==product_store.store_id)\
        .filter(store.title.like("%Тор%"))\
        .group_by(product.title)\
        .limit(10)
    for row in result:
        print(row)
select_product_and_store()  #короткий вариант
print("---------------------------------------------")
select_force_join()         #принудительный джоин