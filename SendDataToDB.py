import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='application', password='&0Dwr6VOj8O&lttzzpIXmvik', host='80.208.228.90', database='mydb')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
insert_stmt = (
   "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)"
   "VALUES (%s, %s, %s, %s, %s)"
)
data = ('Ramya', 'Ramapriya', 25, 'F', 5000)

try:
   # Executing the SQL command
   cursor.execute(insert_stmt, data)
   
   # Commit your changes in the database
   conn.commit()

except:
   # Rolling back in case of error
   conn.rollback()

print("Data inserted")

# Closing the connection
conn.close()