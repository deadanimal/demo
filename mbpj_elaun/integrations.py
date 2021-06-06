# query.py

import cx_Oracle

# Establish the database connection
connection = cx_Oracle.connect(
    user="hr", 
    password="userpwd",
    dsn="dbhost.example.com/orclpdb1")

# Obtain a cursor
cursor = connection.cursor()

# Data for binding
manager_id = 145
first_name = "Peter"

# Execute the query
sql = """SELECT first_name, last_name
         FROM employees
         WHERE manager_id = :mid AND first_name = :fn"""
cursor.execute(sql, mid=manager_id, fn=first_name)

# Loop over the result set
for row in cursor:
    print(row)