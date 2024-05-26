import mysql.connector

# Establishing the connection to the database
iron_man = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mukul2004@",
    database="face"
)

# Uncomment these lines if you want to take input from the user
# book = int(input("Enter book id only number 4 digit: "))
# title = str(input("Enter the book title: "))

# Alternatively, you can hardcode the values for testing
# book = 12
# title = "python3"

# Creating a cursor object using the cursor() method
cur = iron_man.cursor()

# Preparing the SQL query to insert a record into the database
s = "INSERT INTO book (BOOKID, TITLE) VALUES (%s, %s)"
books=[(13,"c"),(14,"c++"),(15,"java")]

# Executing the SQL command
cur.executemany(s, books)# for many data send at one time


# Commit your changes in the database
iron_man.commit()

# Closing the connection
iron_man.close()
