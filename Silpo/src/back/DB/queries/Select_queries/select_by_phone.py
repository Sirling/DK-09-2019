from Silpo.src.back.DB.DataBase import EventReminder, EvEvent
from Silpo.src.back.DB.Session import session


def select_phone(event: str, phone: str):

    reminder = session.query(EventReminder.phone)\
        .filter(EvEvent.title == event,
                EventReminder.phone.like('%{}'.format(phone)))\
        .group_by(EventReminder.phone)
    for row in reminder:
        print(row[0])
