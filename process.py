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

    def getDistinctTasks(self,sqlCon):
        todayDate =date.today()
        latestDateQuery = f"SELECT max(validfrom) FROM DailyTasks;" 
        latestDate = MySQLConnector.readdb(self,sqlCon,latestDateQuery)
        #check if max date is today date? 
        if todayDate < latestDate[0][0]:
            pass
        else:
            latest_str = latestDate[0][0].strftime("%Y-%m-%d")
            distinctTaskQuery = f"SELECT Distinct taskname FROM DailyTasks ;"
            distinctTasks = MySQLConnector.readdb(self,sqlCon,distinctTaskQuery)
            quantityTasksQuery = f"SELECT Distinct quantity FROM DailyTasks ;"
            quantityTasks = MySQLConnector.readdb(self,sqlCon,quantityTasksQuery)
            distinctTasksLists = []
            quantitytasksLists = []
            for i in range(len(distinctTasks)):
                distinctTasksLists.append(distinctTasks[i][0])
                quantitytasksLists.append(quantityTasks[i][0])
            distincttaskname_str = ', '.join([f"'{value}'" for value in distinctTasksLists])
            distincttaskname_list = distincttaskname_str.tolist()

            distinctTasksUpdateQuery = f"INSERT INTO DailyTasks (taskname, quantity, validfrom, validto, isdaily, iscompleted) VALUES ('{distincttaskname_list}', '{quantity}','{validfrom}','{validto}','{isdaily}','{iscompleted}');"
            #update the table with the distinct list and new date     

        #checkTaskquery =f"SELECT validto FROM "  

        #ic(query)
        return distincttaskname_str