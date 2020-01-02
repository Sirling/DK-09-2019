from Python.db_SQLAlchemy.rawSql.cursor import Database
from Python.db_SQLAlchemy.rawSql import queries


def dk():
    db = Database()
    # DB.select(query=queries.select_vacancy)
    # DB.update(query=queries.update_vacancies)
    # DB.select(query=queries.select_vacancy)
    # DB.update(query=queries.insert_vacancy, )
    db.select(query=queries.select_inserted_vacancies)

dk()
