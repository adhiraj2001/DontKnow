import mysql.connector

from script import T_Subject , T_Cognitive_Test , T_Blood_Test
# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

# Create a cursor object
mycursor = mydb.cursor()

# Define the data to be inserted


# Define the SQL statement to insert data
sql = "INSERT INTO customers ({}) VALUES ({})"

# Get the column names from the first row of data
columns = list(data[0].keys())

# Build the placeholders for the SQL statement
placeholders = ', '.join(['%s' for _ in range(len(columns))])

# Replace the {} placeholders in the SQL statement with the column names and placeholders
sql = sql.format(', '.join(columns), placeholders)

# Create a list of values for each row of data
values = [[row[column] for column in columns] for row in data]

# Execute the SQL statement for each row of data
mycursor.executemany(sql, values)

# Commit the changes to the database
mydb.commit()

# Print the number of rows inserted
print(mycursor.rowcount, "rows were inserted.")
