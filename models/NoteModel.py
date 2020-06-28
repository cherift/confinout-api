from .setup import db

class NoteModel:

    def __init__(self, event_id, value):
        self.event_id = event_id
        self.value = value

    def save(self):
        cursor = db.cursor()
        cursor.execute("INSERT INTO Notes(eventid, value) VALUES(%s, %s)", (self.event_id, self.value))
        db.commit()
        cursor.close()