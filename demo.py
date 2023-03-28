import sqlite3
con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()
#Once aConnection has been established, create a Cursor 
# object and call its execute() method to perform SQL commands:
cur = con.cursor()
# create table
cur.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
#insert a row of data
cur.execute("INSERT INTO stocks VALUES('2006-01-05','BUY','RHAT',100,35.14)")
#save the changes
con.commit()
con.close()