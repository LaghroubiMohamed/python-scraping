from tkinter import *
from PIL import ImageTk, Image
import requests 
from scrapCoin import DataGetter
from DataBaseHelper import CSVSaver, DBHelper
from datetime import datetime



class Intereface():
    def __init__(self,title,width,height) :

        root = Tk()
        root.title(title)
        positionRight = int(root.winfo_screenwidth()/2 - width/2)
        positionDown = int(root.winfo_screenheight()/2 - height/2)
        root.geometry(f'{width}x{height}+{positionRight}+{positionDown}')
        root.config(background='white')
      

        img = ImageTk.PhotoImage(Image.open(requests.get("https://www.brandcrowd.com/gallery/brands/pictures/picture15100109443612.png", stream=True).raw))

        self.panel = Label(root, image = img)
        self.panel.pack()
        
        currencies =[
                "BTC-USD","ETH-USD","USDT-USD","DOT1-USD","DOT2-USD",
                "XRP-USD","ADA-USD","LINK-USD","LTC-USD","BCH-USD",
                "BNB-USD","USDC-USD","XLM-USD","BSV-USD","EOS-USD",
                "XMR-USD","XEM-USD","XTZ-USD","THETA-USD","VET-USD",
                "CCXX-USD","NEO-USD","ATOM1-USD","ATOM2-USD"]

        currency = StringVar()
        currency.set(currencies[0])
        
            
        self.combo=OptionMenu(root,currency, *currencies)
        self.combo.config(width=52)
        self.combo.pack()

        
        def recieveData():
            self.datelist,self.highlist,self.lowlist = DataGetter(url="https://finance.yahoo.com/quote/"+currency.get()+"/history/",output=self.output).getdata()
            for i , date in enumerate(self.datelist):
                try:
                    self.datelist[i] = datetime.strptime(date, '%b %d, %Y').strftime('%Y-%m-%d')
                except :
                    print("")
                return saveInCsv()
          
            
        def saveInCsv():
            fulldata=zip(self.datelist,self.highlist,self.lowlist)
            row0 = ['date','high','low']
            CSVSaver(filename='file.csv',dataTitleRow=row0,datalist=fulldata).SaveAsCSV()
            
        
        # def saveInDb():
        #     dataForDb= zip(self.datelist,self.highlist,self.lowlist)
        #     DBHelper(data=dataForDb ,path="base.db").SaveIntoDb()
            
                
                
        self.getData_button = Button(root, height = 2, 
                        width = 20,  
                        text ="get Data",command=recieveData)
        self.getData_button.pack()

        #get a scrollbar
        scroll = Scrollbar(root)
        scroll.pack(side=RIGHT, fill=Y)

        self.output = Text(root, height = 50,  
                    width = 52,  
                    bg = "light yellow",
                    wrap=NONE,
                    yscrollcommand=scroll.set) 
        self.output.insert('1.0',' welcome ')
        self.output.pack()

        # Configure the scrollbars
        scroll.config(command=self.output.yview)
        root.mainloop()

r= Intereface(title="Coin Scanner ", width=500,height=800)

