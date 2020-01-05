from Silpo.src.back.DB import DataBase
from Silpo.src.back.DB.Session import session


def event_reminder_phone(event_id: int, phone: str):

    try:
        new_reminder = DataBase.EventReminder(event_id, phone)
        session.add(new_reminder)
        session.flush()
    except Exception as error:
        raise error

