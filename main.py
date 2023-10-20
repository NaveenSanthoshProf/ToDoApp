from display import ApplicationUI
from dataconn import MySQLConnector

class MainApplication:
    def __init__(self, db_config):
        self.db_config = db_config
        self.mysql_connector = None

    def run(self):
        try:
            self.mysql_connector = MySQLConnector(
                host=self.db_config["host"],
                username=self.db_config["user"],
                password=self.db_config["password"],
                database=self.db_config["database"]
            )
            self.mysql_connector.connect()

            ApplicationUI(sqlCon=self.mysql_connector.connect())
            # Your main application logic goes here



        finally:
            print("debug")
            print(self.mysql_connector.connect())

            pass 
        
        #    if self.mysql_connector:
        #        self.mysql_connector.close()

if __name__ == "__main__":
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "031068",
        "database": "mysql"
    }

    app = MainApplication(db_config)
    app.run()