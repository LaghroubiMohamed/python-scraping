from bs4 import BeautifulSoup 
from selenium import webdriver
import time

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
                highList.append(item.findAll('td', class_='Py(10px) Pstart(10px)')[1].text)
                lowList.append(item.findAll('td', class_='Py(10px) Pstart(10px)')[2].text)
            driver.quit
        except:
            print("check the internet access or verify the webdriver path")
            self.output.insert("1.0"," Oops! Something Went Wrong \n Please check your internet First and Try Again \n Or Contact Our Support ")
        return dateList,highList,lowList


# DataGetter(url='https://finance.yahoo.com/quote/BTC-USD/history/').getdata()
# for item in zip( dateList,highList, lowList):
#    print(item )
