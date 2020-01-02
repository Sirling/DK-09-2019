import mysql.connector
from Python.db_SQLAlchemy.pwrd.pwrd import password

print(mysql.connector.version.VERSION)

class Database:

    def connect(self):
        mysql_server = '10.10.16.202'
        database = 'db_newsilpo_dev1'

        connection = mysql.connector.connect(host=mysql_server,
                                             database=database,
                                             port=3306,
                                             user='a-b.shvets',
                                             password=password

                                             )
        return connection

    def select(self, query):
        connect = self.connect()
        cursor = connect.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()                                                                                                                                                          
            for row in result:
                print(row)
        except mysql.connector.Error as error:
            print(error)
        finally:
            if connect.is_connected():
                cursor.close()

    def update(self, query):
        connect = self.connect()
        cursor = connect.cursor()
        try:
            cursor.execute(query)
            connect.commit()

        except mysql.connector.Error as error:
            print("Failed to update record to DB rollback: {}".format(error))
            connect.rollback()

        finally:
            if connect.is_connected():
                cursor.close()
