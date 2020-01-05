from Silpo.src.back.DB.DataBase import EventReminder
from Silpo.src.back.DB.Session import session


def event_reminder_phone(phone: str):

    try:
        reminder = session.query(EventReminder)\
            .filter(EventReminder.phone.like('%{}'.format(phone)))
        print(reminder)
        return reminder
    except Exception as error:
        raise error
