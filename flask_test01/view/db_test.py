import pymysql


class DbTest:
    def __init__(self):
        self.db = pymysql.connect("localhost","root","","test01")
        self.cursor = self.db.cursor()

    def db_data(self,name):

        sql = "SELECT * FROM user WHERE name = '%s' " %(name)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result

        except:
            print("Error: unable to fetch data")
        self.db.close()








