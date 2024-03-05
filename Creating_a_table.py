# importing the required module
import sqlite3

#use the database if it pre-exists or create it otherwise
try:
    connection = sqlite3.connect("myemp.db")
    print("Connected with the database successfully .....")
except:
    print("Database creation ERROR !!!")

# create employee table as employee (emp_id,emp_name, emp_city, emp_salary)
sqlStr = '''
        CREATE TABLE employee(
        emp_id INTEGER PRIMARY KEY,
        emp_name TEXT,
        emp_city TEXT,
        emp_salary REAL
        );
        '''
try:
    connection.execute(sqlStr)
    print("Database table has been created successfully....")
except:
    print("Error occurred while creating the datbase ")
