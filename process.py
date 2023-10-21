from dataconn import MySQLConnector
from datetime import date


class DailyTasks():
    def __init__(self):
        pass

    def updateDaily(self,sqlCon):
        pass

    def getTasks(self,sqlCon):
        tasks = []
        query = f"SELECT taskname FROM DailyTasks"
        MySQLConnector.readdb(self,sqlCon,query)
        return tasks

    def addTasks(self,sqlCon,taskname,quantity,isdaily):
        validfrom = date.today()
        validto = '2099-01-01'
        iscompleted = 0 
        query = f"INSERT INTO DailyTasks (taskname, quantity, validfrom, validto, isdaily, iscompleted) VALUES ('{taskname}', '{quantity}','{validfrom}','{validto}','{isdaily}','{iscompleted}');"
        print(query)
        MySQLConnector.modifydb(self,sqlCon,query)