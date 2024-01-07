import mysql.connector
print("(Note: This program will run continuously, offering options from 1 to 4, which you can choose.\n However, if you select options 2 or 3 again, it will throw an error because the database and \ntable show an error indicating that the table or database already exists. )")

#connection is establish hear
mydb = mysql.connector.connect(
    host = "localhost",
    user = "Your_username",
    password = "Your_Password",
    database = "database_name"
)
print(mydb,"\nDB Connection successfull....")

    

def switch_case(c):
    #creating a instance of cursor
    cursor = mydb.cursor()
    if c==1:
        #Executing the SHOW DATABASES mysql query 
        cursor.execute("SHOW DATABASES")
        for x in cursor:
            print(x)
    elif c==2:
        #Executing the CREATE DATABASE mysql query to create a database
        cursor.execute("CREATE DATABASE jpt")
    elif c==3:
        #Storing the Mysql query in the orderlist
        orderlist = """CREATE TABLE ORDERLIST ( 
                   NAME  VARCHAR(20) NOT NULL,  
                   SIZES INT NOT NULL,
                   PAYMENT VARCHAR(5)
                   )"""
        #Executing the above query
        cursor.execute(orderlist)
    elif c==4:
        #It's show the list of tables
        cursor.execute("SHOW TABLES")
        for t in cursor:
            print(t)
    else:
        exit(1)
print("\nStart the actions By choosing below option: ")      
print("1.Show Database\n2.Create Database with Name jpt\n3.Create Table with Name Orderlist\n4.Show Lists of Tables")       

while (1):
    c = int(input("Enter the option: "))
    switch_case(c)

