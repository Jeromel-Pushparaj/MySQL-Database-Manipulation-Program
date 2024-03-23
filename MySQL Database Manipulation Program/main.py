import mysql.connector
print("(Note: This program will run continuously, offering options from 1 to 4, which you can choose.\n However, if you select options 2 or 3 again, it will throw an error because the database and \ntable show an error indicating that the table or database already exists. )")

#connection is establish hear
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root"
    # database = "database_name"
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
        dbname = str(input("enter the dbname: "))
        cursor.execute("CREATE DATABASE "+ dbname)
    elif c==3:
        #Executing the CREATE DATABASE mysql query to create a database
        udbname = str(input("enter the dbname You want use: "))
        cursor.execute("USE "+ udbname)
    elif c==4:
        #Storing the Mysql query in the orderlist

        table_name = str(input("enter the table name: "))
        no_c = int(input("enter how many columns you need: "))

        columns = []  # Initialize an empty list outside the loop to hold column definitions

        for i in range(no_c):
            name_c = str(input("enter the column name: "))
            d_type = str(input("enter the datatype of the column: "))
            columns.append(name_c + " " + d_type)  # Append each column definition to the list
         
        """
        Now, to create the table content, you should join the columns into a single string

        Explaination for the .join() inbuit fuciton
        ", ".join(columns): This part is where the magic happens. ", ".join(columns) joins all the elements of the columns list into a single string, separated by ", ".
        For example, if columns is ['id INT', 'name VARCHAR(50)', 'age INT'], then ", ".join(columns) will result in 'id INT, name VARCHAR(50), age INT'.
        """

        table_content = "CREATE TABLE " + table_name + "(" + ", ".join(columns) + ")"
        print(table_content)
        #Executing the above query
        cursor.execute(table_content)
    elif c==5:
        #It's show the list of tables
        cursor.execute("SHOW TABLES")
        for t in cursor:
            print(t)
    elif c==6:
        #It's show the list of tables
        table_name = str(input("enter the table name, you want desc: "))
        cursor.execute("desc " + table_name + ";")
        for t in cursor:
            print(t)
    elif c == 7:
        table_name = str(input("Enter the table_name you want select: "))
        cursor.execute("select * from "+table_name)
        result = cursor.fetchall()
        for row in result:
            print(row)
    elif c == 8:
        column_name = {}
        table_name = str(input("Enter the table name you want to insert: "))
        c_n = str(input("Enter the columns name : "))
        value = str(input("Enter the value of the column you enter: "))
        column_name[c_n]=value
        numberOfColumn = cursor.execute("SELECT count(*) as No_of_Column FROM information_schema.columns WHERE table_name = '" + table_name +"';")
    else:
        exit(1)
print("\nStart the actions By choosing below option: ")      
print("1.Show Database\n2.Create Database\n3.to choose a database\n4.Create Table\n5.Show Lists of Tables\n6.desc the table\n7.select the table")       

while (1):
    c = int(input("Enter the option: "))
    switch_case(c)
