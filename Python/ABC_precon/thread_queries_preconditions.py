from Python.db_SQLAlchemy.alchemy import Base, metadata, session
from sqlalchemy import *


class HRVacancies(Base):
    # Создание таблицы
    __table__ = Table('hr_vacancy', metadata, autoload=True)


def del_vacancy_by_name(name):
    # Выбор необходимой вакансии
    vacancy = session.query(HRVacancies).filter(HRVacancies.name == ''.format(name))
    # Удаление этой вакансии
    vacancy.delete(synchronize_session=False)


def ins_vacancy():
    from Python.ABC_precon.queries_data import test_vacancy
    # добавление вакансии
    session.add(test_vacancy)
    session.flush()
