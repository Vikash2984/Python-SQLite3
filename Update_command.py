sqlStr = "UPDATE employee set emp_salary=30000 where emp_city='Chennai' ;"
table = connection.execute(sqlStr)
for row in list(table):
    print(f"Emp-city: {row[0]} UPdated Salary: {row[1]}")
