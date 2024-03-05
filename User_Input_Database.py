# insert n number of records (where n is one user given integer) 
# from user given keyboard inputs (e.g. n = 2)
n = int(input("Please enter the number of records:"))
cursor = connection.cursor()
for i in range(n):
    empid = int(input("Please enter Emp-ID:"))
    empname = input("Please enter Emp-Name:")
    empcity = input("Please enter Emp-City:")
    empsalary = int(input("Please enter Emp-Salary:"))
    cursor.execute("INSERT INTO employee VALUES (?,?,?,?)", (empid, empname, empcity, empsalary))
connection.commit()
print ("All the records have got inserted sucessfully...")