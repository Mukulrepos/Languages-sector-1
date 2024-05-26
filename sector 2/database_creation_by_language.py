import mysql.connector
iron_man=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mukul2004@",
    database="face"

)

# print(iron_man.connection_id)

cur=iron_man.cursor()
# cur.execute("create database face")
# cur.execute("use face")
# cur.execute("create table roots(order INT)")
s="CREATE TABLE BOOK(BOOKID INTEGER(4),TITLE VARCHAR(20))"
cur.execute(s)