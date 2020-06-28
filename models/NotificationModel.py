from .setup import db
import datetime

class NotificationModel:

    def __init__(self, event_id, value):
        self.event_id = event_id
        self.value = value
        self.date = datetime.datetime.now()

    def save(self):
        cursor = db.cursor()
        cursor.execute("INSERT INTO Notifs(eventid, date, value) VALUES(%s, %s, %s)", 
                        (self.event_id, self.date, self.value))
        db.commit()
        cursor.close()