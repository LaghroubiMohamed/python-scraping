- 👋 Hi, I’m @LaghroubiMohamed
- 👀 I’m interested in Data Science and mobile app development with flutter and dart 🐦
- 🌱 I’m currently learning Python and R 
- 📫 How to reach me : laghroubi.mohamed@gmail.com


# python-scraping
this is a simple script to scrap crypto-currencies data from finance.yahoo.com

## Getting Started
 you can start the programe interface in the file interface.py
 
 # Note:
Make sure that the base.db has already an empty table with 5 field (date ,open, high, low,close) before 
You start the scripe in interface.py
	Or you can just run the Command "CREATE TABLE "coin" (\n
		"date"	DATETIME,
		"open"	NUMERIC,
		"hight"	NUMERIC,
		"low"	NUMERIC,
		"close"	NUMERIC
   		 );"
	to create the table for you

install a chrome driver depend on your current version of Google chrome and change the path in interface.py

if the make sure that the name of your dataBase is the same you pass to the DbHelper() in the interface.py and the the table name is the same in the the DBHelper
	in the DataBaseHelper.py file
