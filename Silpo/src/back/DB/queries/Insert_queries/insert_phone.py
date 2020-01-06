from datetime import datetime

from Silpo.src.back.DB.DataBase import EventReminder
from Silpo.src.back.DB.Session import session


def insert_phone(event_id: int, phone: str):

    try:
        new_reminder = EventReminder(event_id=event_id,
                                     email='',
                                     phone=phone,
                                     created_at=datetime.now())
        session.add(new_reminder)
        session.flush()
    except Exception as error:
        session.rollback()
        raise error
