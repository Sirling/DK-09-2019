from Silpo.src.back.DB.DataBase import EventReminder, EvEvent
from Silpo.src.back.DB.Session import session


def delete_phone(event: str, phone: str):

    try:
        reminder = session.query(EventReminder.phone)\
            .filter(EvEvent.title == event,
                    EventReminder.phone.like('%{}'.format(phone)))
        reminder.delete(synchronize_session=False)
    except Exception as error:
        raise error
