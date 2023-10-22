import os 
import pymysql
from icecream import ic

class MySQLConnector:

    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database
            )
        except pymysql.Error as err:
            print(f"Error: {err}")
        
        return self.connection

    def modifydb(self,sqlCon,query):
         cursor = sqlCon.cursor()
         cursor.execute(query)
         print("data updated")
         sqlCon.commit()
    
    def readdb(self,sqlCon,query):
         cursor = sqlCon.cursor()
         cursor.execute(query)
         updatedRow = cursor.fetchall()
         data = []
         for column in updatedRow:
            data.append(column)
         ic(data)
         return data
           

    def close(self):
            self.connection.close()
            print("MySQL connection is closed")













    