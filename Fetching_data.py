# retrieving records from the database table
# SQL for fetching all records from the table
sqlStr = "SELECT * FROM employee;"
# read from the table and point the cursor to the variable cur_table
cur_table = connection.execute(sqlStr)
# print (list(cur_table))
for row in list(cur_table):
    print(f"Emp-ID: {row[0]}, Emp-Name: {row[1]}, Emp-City: {row[2]}, Emp-Salary: {row[3]}")
sqlStr = "SELECT emp_name, AVG(emp_salary) FROM employee GROUP BY emp_city  ;"
cur_table = connection.execute(sqlStr)
for row in list(cur_table):
    print(f"Emp-City: {row[0]} and Avg-Emp-Salary: {row[1]}")
