import sqlite3 as sql
import csv
class DBHelper:
    def __init__(self,data,path) :
        self.data=data
        self.path = path
        self.db=DbConnecter(self.path)
        

    def SaveIntoDb(self):
        query = ('INSERT INTO coin (date,open,high,low,close) VALUES (?,?,?,?,?)')
        self.db.exec(query=query,data=self.data)

class DbConnecter:
    def __init__(self,path) :
        self.path = path
    def exec(self,query,data):
        with sql.connect(self.path) as conn:
           conn.executemany(query,data)


class CSVSaver():
    def __init__(self, filename, dataTitleRow,datalist):
        self.filename = filename
        self.dataTitleRow = dataTitleRow
        self.datalist = datalist

    def SaveAsCSV(self):
        with open(self.filename,'w',encoding="utf-8",newline='') as csvfile :
            dataWriter = csv.writer(csvfile)
            dataWriter.writerow(self.dataTitleRow)
            for item in self.datalist:
                dataWriter.writerow(item)