# MySQL Database Manipulation Program

This Python program enables users to perform various operations on a MySQL database. It establishes a connection to the MySQL server and provides a menu-driven interface to execute different tasks.

## Features

- **Database Connection:** The program establishes a connection to a local MySQL database.
- **Menu-Driven Interface:** Users can choose from four options to perform specific actions:
  1. **Show Databases:** Displays a list of available databases.
  2. **Create Database:** Creates a new database named 'jpt'.
  3. **Create Table:** Generates a table named 'ORDERLIST' with specified columns.
  4. **Show Tables:** Shows a list of tables in the connected database.

## Prerequisites

- Python installed on your machine
- MySQL Connector Python library (`mysql-connector-python`)

## Usage

1. Ensure you have Python and the MySQL Connector Python library installed.
2. Modify the following connection parameters in the code:
   - `host`: Your MySQL server's hostname or IP address.
   - `user`: Your MySQL username.
   - `password`: Your MySQL password.
   - `database`: Your default database name.
3. Run the program in your Python environment.
4. Follow the on-screen instructions to select the desired action.

## Note

This program runs continuously and offers options from 1 to 4. However, selecting options 2 or 3 more than once may throw an error if the database or table already exists.

---
