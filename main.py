import dataconn
import display

class App(object):
    def run(self,string):
        print ("HELLO {}!!".format(string))
        #dataconn.DBConnection.dbstatus(self)
        dataconn()

if __name__ == "__main__" :
    App().run(string="random")
