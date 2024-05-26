import mysql.connector

connect_module=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mukul2004@",
    database="face"
)

cur=connect_module.cursor()
s="SELECT *FROM BOOK"
cur.execute(s)
result=cur.fetchall()# fetch all data from server

for i in result:
    print(i)

# s= "UPDATE book SET BOOKID=BOOKID+20 WHERE BOOKID>13"
# cur.execute(s)
# connect_module.commit()