
from DataBaseHelper import CSVSaver, DBHelper
from datetime import datetime

import pandas as pd
from scrapCoin import DataGetter
import numpy as np


class DataProcessing():
    def __init__(self, output,currency):
        
        self.currency = currency
        self.output = output
        
        def dataReciever():
            self.datelist,self.openlist,self.highlist,self.lowlist,self.closelist = DataGetter(url="https://finance.yahoo.com/quote/"+self.currency.get()+"/history/",output=self.output).getdata()
            return dateFormater()
            
            
        def dateFormater (): 
            for i , date in enumerate(self.datelist):
                self.datelist[i] = datetime.strptime(date, '%b %d, %Y')
            return dataTypeEditor()
            
        def dataTypeEditor():
            for  n , i in enumerate(self.highlist):
                if i == '-':
                    self.highlist[n]=np.nan
                    self.lowlist[n]=np.nan  
                    self.openlist[n]=np.nan
                    self.closelist[n]=np.nan
                else:
                    self.closelist[n]=float(self.closelist[n]) 
                    self.highlist[n]=float(self.highlist[n])
                    self.openlist[n]=float(self.openlist[n])  
                    self.lowlist[n]=float(self.lowlist[n])  
            return saveInDb()
        
        def saveInCsv():
            dataDF = pd.DataFrame({'date': self.datelist,'high':self.highlist,'low': self.lowlist,'open':self.openlist, 'close':self.closelist})                              
            CSVSaver(dataframe=dataDF,path='data.csv')
            
        def saveInDb():
            dataForDb= zip(self.datelist,self.openlist,self.highlist,self.lowlist,self.closelist)
            DBHelper(data=dataForDb ,path="base.db").SaveIntoDb()
            return saveInCsv()
           
            
        return dataReciever()