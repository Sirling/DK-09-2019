from queries_task.cursor import Database
from queries_task import queries


def dk():
    db = Database()
    # db.select(query=queries.select_vacancy)
    # db.update(query=queries.update_vacancies)
    # db.select(query=queries.select_vacancy)
    # db.update(query=queries.insert_vacancy, )
    db.select(query=queries.select_inserted_vacancies)

dk()
