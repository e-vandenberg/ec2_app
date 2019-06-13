import _mysql

class Database:
        def __init__(self, endp, user, pwd, db):
                # contact the RDS Database
                self.db=_mysql.connect(endp, user, pwd, db)

        def get_age(self, name):
                self.db.query("""SELECT age FROM accounts WHERE name = '%s'""" % (name))
                result = self.db.use_result()
                return result.fetch_row()[0][0]
                self.db.close()
