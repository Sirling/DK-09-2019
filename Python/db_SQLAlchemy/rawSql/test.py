from Python.db_SQLAlchemy.rawSql.cursor import Database
from Python.db_SQLAlchemy.rawSql import queries


def dk():
    db = Database()
    # db.select(query=queries.select_vacancy)
    # db.update(query=queries.update_vacancies)
    # db.select(query=queries.select_vacancy)
    # db.update(query=queries.insert_vacancy, )
    db.select(query=queries.select_inserted_vacancies)

dk()
