import mysql.connector


class Database:
    def __init__(self, endp, user, pwd, db):
        # contact the RDS Database
        self.db=mysql.connector.connect(host=endp, user=user, password=pwd, database=db)

    def get_age(self, name):
        cursor = self.db.cursor()
        cursor.execute("""SELECT age FROM accounts WHERE name = '%s'""" % (name))
        row = cursor.fetchone()
        return row[2]

    def new_user(self, name, age):
        cursor = self.db.cursor()
        cursor.execute("""INSERT INTO accounts (name, age) VALUES ('%s', '%s')""" % (name, age))
        return "new account created"
