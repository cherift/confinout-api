from .setup import db

class DBModel :

    def __init__(self):
        """
        Initializes the tables used in the database.
        """

        cursor = db.cursor()

        if not self.tableExists("Types") :
            cursor.execute('''
                CREATE TABLE Types(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255)
                )
            ''')

        if not self.tableExists("Events") :
            cursor.execute('''
                CREATE TABLE Events(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    place VARCHAR(50),
                    address VARCHAR(255),
                    price FLOAT,
                    date DATETIME,
                    description VARCHAR(255),
                    typeid INT,
                    FOREIGN KEY (typeid) REFERENCES Types(id),
                    link VARCHAR(50),
                    number VARCHAR(12),
                    longitude FLOAT,
                    latitude FLOAT,
                    inside INT(1),
                    available INT(1),
                    handicap INT(1)
                )
            ''')

        if not self.tableExists("Notes"):
            cursor.execute('''
                CREATE TABLE Notes(
                    id INT AUTO_INCREMENT PRIMARY KEY, 
                    eventid INT,
                    FOREIGN KEY (eventid) REFERENCES Events (id),
                    value INT
                )
            ''')

        if not self.tableExists("Comments"):
            cursor.execute('''
                CREATE TABLE Comments(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    eventid INT,
                    FOREIGN KEY (eventid) REFERENCES Events(id),
                    value VARCHAR(255)
                )
            ''')

        if not self.tableExists("Notifs"):
            cursor.execute('''
                CREATE TABLE Notifs(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    eventid INT,
                    FOREIGN KEY (eventid) REFERENCES Events(id),
                    value VARCHAR(255)
                )
            ''')

    def tableExists(self, table_name):
        """
        Checks if table exists in database.
        
        Parameters
        ----------
        table : string
                the table name
        """
        cursor = db.cursor()
        cursor.execute("show tables like %s", (table_name, ))
        result = cursor.fetchone()
        cursor.close()

        return True if result else False

