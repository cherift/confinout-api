from .setup import db

class EventModel:
    """
        Represents an event object
    """

    def __init__(self, place, address, price, date, description, typeid,
                link = None, number = None, inside = 1, available = 1, handicap = 1):
        self.place = place
        self.address = address
        self.price = price
        self.date = date
        self.description = description
        self.typeid = typeid
        self.link = link
        self.number = number
        self.inside = inside
        self.available = available
        self.handicap = 1

    def save(self):
        cursor = db.cursor()
        cursor.execute("""INSERT INTO Events(place, address, price, date, description, typeid,
                        link, number, inside, available, handicap)
                        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                        (self.place, self.address, self.price, self.date, self.description, 
                         self.typeid, self.link, self.number, self.inside, self.available, self.handicap))
        db.commit()
        cursor.close()

