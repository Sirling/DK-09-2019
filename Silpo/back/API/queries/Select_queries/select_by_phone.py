from Silpo.back.API.DB.DataBase import EventReminder
from Silpo.back.API.DB.session import session


def event_reminder_phone(phone: str):

    try:
        reminder = session.query(EventReminder)\
            .filter(EventReminder.phone.like('%{}'.format(phone)))
        print(reminder)
        return reminder
    except Exception as error:
        raise error
