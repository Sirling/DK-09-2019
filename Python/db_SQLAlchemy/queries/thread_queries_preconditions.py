from Python.db_SQLAlchemy.alchemy import Base, Table, metadata, session


class Product(Base):
    __table__ = Table('product', metadata, autoload=True)


class HRVacancies(Base):

    __table__ = Table('hr_vacancy', metadata, autoload=True)

class DeleteFromTable:

    def del_vacancy_by_manager_name(self, name):

        session.execute(HRVacancies.delete().where(HRVacancies.manager_name == '{}'.format(name)))


class Insert:

    def ins_vacancy(self):

        from Python.db_SQLAlchemy.queries.queries_data import nescafe_vacancy
        session.execute(HRVacancies.insert().values(nescafe_vacancy))

