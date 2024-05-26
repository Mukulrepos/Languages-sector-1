import mysql.connector
iron_man=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mukul2004@",
    database="face"

)

mycursor=iron_man.cursor()
print("")