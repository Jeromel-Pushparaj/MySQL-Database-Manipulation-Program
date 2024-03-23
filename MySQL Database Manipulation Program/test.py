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