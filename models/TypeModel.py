from .setup import db

class TypeModel:
    
    def __init__(self, name):
        self.name = name

    def save(self):
        cursor = db.cursor()
        cursor.execute("INSERT INTO Types(name) VALUES(%s)", (self.name, ))
        db.commit()
        cursor.close()