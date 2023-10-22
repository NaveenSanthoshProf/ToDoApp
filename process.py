from dataconn import MySQLConnector
from datetime import date
from icecream import ic
import functools
import operator

class DailyTasks():
    def __init__(self):
        pass

    def updateDaily(self,sqlCon):
        pass

    def getTasks(self,sqlCon):
        tasks = []
        query = f"SELECT taskname FROM DailyTasks WHERE validto = '2099-01-01' AND iscompleted = '0' AND isdaily = '1'"
        tasks = MySQLConnector.readdb(self,sqlCon,query)
        return tasks

    def addTasks(self,sqlCon,taskname,quantity,isdaily):
        validfrom = date.today()
        validto = '2099-01-01'
        iscompleted = 0 
        query = f"INSERT INTO DailyTasks (taskname, quantity, validfrom, validto, isdaily, iscompleted) VALUES ('{taskname}', '{quantity}','{validfrom}','{validto}','{isdaily}','{iscompleted}');"
        print(query)
        MySQLConnector.modifydb(self,sqlCon,query)

    def updateTasks(self,sqlCon,taskname):
        today = date.today()
        taskname_str = ', '.join([f"'{value[0]}'" for value in taskname])
        query = f"UPDATE DailyTasks set iscompleted = 1 , validto = '{today}' WHERE taskname IN({taskname_str});"
        print(query)
        MySQLConnector.modifydb(self,sqlCon,query)