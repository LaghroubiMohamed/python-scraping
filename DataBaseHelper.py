import sqlite3 as sql
class DBHelper:
    def __init__(self,data,path) :
        self.data=data
        self.path = path
        self.db=DbConnecter(self.path)
        

    def SaveIntoDb(self):
        query = ('INSERT INTO coin (date,open,high,low,close) VALUES (?,?,?,?,?)')
        clearQuery = ('delete from coin')
        self.db.clearDb(clearQuery)
        self.db.exec(query=query,data=self.data)

class DbConnecter:
    def __init__(self,path) :
        self.path = path
    def exec(self,query,data):
        with sql.connect(self.path) as conn:
           conn.executemany(query,data)
    def clearDb (self,clearQuery):
        with sql.connect(self.path)as conn:
            conn.execute(clearQuery)


class CSVSaver():
    def __init__(self,path,dataframe):
        self.path = path
        self.dataframe = dataframe
        self.dataframe.to_csv( self.path ,index = False, header=True)