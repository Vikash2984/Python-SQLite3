sqlStr = "DELETE FROM employee where emp_city='Kolkata' ;"
table = connection.execute(sqlStr)
for row in list(table):
    print(f"Emp-city: {row[0]} UPdated Salary: {row[1]}")
sqlStr = "SELECT * FROM employee;"
# read from the table and point the cursor to the variable cur_table
cur_table = connection.execute(sqlStr)
# print (list(cur_table))
for row in list(cur_table):
    print(f"Emp-ID: {row[0]}, Emp-Name: {row[1]}, Emp-City: {row[2]}, Emp-Salary: {row[3]}")
