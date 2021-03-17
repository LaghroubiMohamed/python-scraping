from DataBaseHelper import DBHelper
from tkinter.constants import END
from bs4 import BeautifulSoup 
from selenium import webdriver
import time




openList=[]
closeList=[]
dateList = []
highList =[]
lowList = []

class DataGetter ():
    def __init__(self,url,output):
        self.url = url
        self.output=output

    def getdata(self):
        try:
            
            driver = webdriver.Chrome(executable_path="/home/glitcher/Desktop/pythonProjet/chromedriver")
            driver.get(self.url)
            
            scrollTime = 1
            while scrollTime<4: 
                driver.execute_script("window.scrollBy(0,8000)") 
                time.sleep(0.5) 
                scrollTime+=1 

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            #find all the TR in the table
            myTr = soup.findAll('tr',{'class':'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'})
           
            #put all data in lists
            for  item in myTr:
                dateList.append( item.find('td', class_='Py(10px) Ta(start) Pend(10px)').text)
                highList.append(item.findAll('td', class_='Py(10px) Pstart(10px)')[1].text.replace(',',''))
                lowList.append(item.findAll('td', class_='Py(10px) Pstart(10px)')[2].text.replace(',',''))
                openList.append(item.findAll('td', class_='Py(10px) Pstart(10px)')[0].text.replace(',',''))
                closeList.append(item.findAll('td', class_='Py(10px) Pstart(10px)')[3].text.replace(',',''))
               
            
            driver.quit
                   
            self.output.delete('1.0',END)
            self.output.insert("1.0",[str(i)+'\n'  for i in zip(dateList,openList,highList,lowList,closeList)])
            self.output.insert("1.0","Date              /  Open       /     High    /    Low     /     Close   \n ")
        except:
            self.output.delete('1.0',END)
            print("check the internet access or verify the webdriver path")
            self.output.insert("1.0"," Oops! Something Went Wrong \n Please check your internet access First and Try Again \n Or Contact Our Support ")
        return dateList,openList, highList,lowList,closeList


# DataGetter(url='https://finance.yahoo.com/quote/BTC-USD/history/').getdata()
# for item in zip( dateList,openList ,highList, lowList,closeList):
#    print(item )
# dataDF = pd.DataFrame({'date': dateList,'high':highList,'low': lowList,'open':openList, 'close':closeList})             
# DBHelper(data=dataDF ,path="base.db").SaveIntoDb()
# print(type(highList[3]))
# print(highList[3])

# print(type(highList[5]))
# print(highList[5])
