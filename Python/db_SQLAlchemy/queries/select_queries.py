from Python.db_SQLAlchemy.alchemy import Base, metadata, session
from sqlalchemy import *


class HRVacancies(Base):
    # Создание таблицы вакансий
    __table__ = Table('hr_vacancy', metadata, autoload=True)


class ProductStore(Base):
    # Создание таблицы связи продуктов и магазинов
    __table__ = Table('product_store', metadata, autoload=True)


class Product(Base):
    # Создание таблицы продуктов
    __table__ = Table('product', metadata, autoload=True)


class Store(Base):
    # Создание таблицы магазинов
    __table__ = Table('store', metadata, autoload=True)


def select_vacancy():
    # Выборка вакансии по имени контактного лица
    vacancies = session.query(HRVacancies).\
        filter(HRVacancies.manager_name == "Опанас")
    for row in vacancies:
        print(row.contact_one)


def select_product_and_store():
    """
    Поиск продуктов и магазинов, в которых они продаються
    Автоматический джоин через транзитную таблицу
    """
    result = session.query(Product.title, func.count(Store.title))\
        .filter(Store.title.like("%Тор%"))\
        .group_by(Product.title)\
        .limit(10)
    for row in result:
        print(row)


def select_force_join():
    """
    Тот же запрос, только через принудительный джоин
    """
    result = session.query(Product.title, func.count(Store.title))\
        .join(ProductStore, Product.id == ProductStore.product_id)\
        .join(Store, Store.id == ProductStore.store_id)\
        .filter(Store.title.like("%Тор%"))\
        .group_by(Product.title)\
        .limit(10)
    for row in result:
        print(row)


select_product_and_store()  # короткий вариант
print("---------------------------------------------")
select_force_join()         # принудительный джоин