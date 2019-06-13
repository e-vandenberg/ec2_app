import _mysql

class Database:
        def __init__(self, endp, user, pwd, db):
                self.db=_mysql.connect(endp, user, pwd, db)

        def get_age(self, name):
                self.db.query("""SELECT age FROM accounts WHERE name = '%s'""" % (name))
                r = self.db.use_result()
                return r.fetch_row()[0][0]
                self.db.close()
