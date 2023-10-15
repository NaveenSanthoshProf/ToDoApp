import os 

import mysql.connector
from mysql.connector import Error


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='mysql',
                                         user='root',
                                         password='031068')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")










#class DBConnection:
#    def __init__(self):
#        #self.password = os.getenv("PASSWORD")
#        self.mydb = mysql.connector.connect(
#            host="localhost",
#            user="root",
#            passwd="031068",
#            database="mysql"
#        )
#        self.cur = self.mydb.cursor()
#
#    def __enter__(self):
#        return self
#    
#    def __exit__(self,exc_type, exc_val, exc_tb):
#        self.mydb.connection.close()
#
#    def dbstatus(self):
#        print("Connecting to the database...")
#        self.mydb.isconnected() 


    