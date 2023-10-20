import os 

import pymysql


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


    def close(self):
            self.connection.close()
            print("MySQL connection is closed")













    