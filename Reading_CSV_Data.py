# reading data from the csv file and feeding it to the employee table
import csv
sqlStr = "INSERT INTO employee VALUES('{e_id}', '{e_name}', '{e_city}', '{e_salary}');"
# read lines from the csv file and store them into the table
with open('emp_data.csv') as data_file:
    csv_reader = csv.reader(data_file)
    # reader to read from the data file with ',' as a delimiter/separator
    for each_row in csv_reader:
        # print (each_row)
        connection.execute(sqlStr.format(e_id=each_row[0], e_name=each_row[1], e_city=each_row[2], e_salary=each_row[3]))
connection.commit()   # to make the change permanent
print ("All records got inserted successfully...")
