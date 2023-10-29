from dataconn import MySQLConnector
from datetime import date
from icecream import ic
import functools
import operator
import pandas as pd


class DailyTasks():
    def __init__(self):
        pass

    def updateDaily(self,sqlCon):
        pass

    def getTasks(self,sqlCon):
        tasks = []
        today = date.today()
        query = f"SELECT taskname FROM DailyTasks WHERE validfrom ='{today}' AND iscompleted = '0' AND isdaily = '1'"
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

    def getDistinctTasks(self,sqlCon):
        ##to debug  updates db twice 
        todayDate =date.today()
        latestDateQuery = f"SELECT max(validfrom) FROM DailyTasks;" 
        latestDate = MySQLConnector.readdb(self,sqlCon,latestDateQuery)
        #check if max date is today date? 
        if todayDate < latestDate[0][0]:
            pass
        else:
            latest_str = latestDate[0][0].strftime("%Y-%m-%d")
            distinctTaskQuery = f"SELECT * FROM DailyTasks WHERE isdaily = 1 and validfrom = '{latestDate[0][0]}';"
            distinctTasks = MySQLConnector.readdb(self,sqlCon,distinctTaskQuery)
            Validfrom = todayDate.strftime("%Y-%m-%d")
            Validto='2099-01-01'
            isdaily = '1'
            iscomplete = '0'
            for i in (distinctTasks):
                distinctTasksUpdateQuery = f"INSERT INTO DailyTasks (taskname, quantity, validfrom, validto, isdaily, iscompleted) VALUES ('{i[1]}','{i[2]}','{Validfrom}','{Validto}','{isdaily}','{iscomplete}');"
                MySQLConnector.modifydb(self,sqlCon,distinctTasksUpdateQuery)
                
        return