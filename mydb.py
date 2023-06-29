import pymysql

dataBase = pymysql.connect(
    host = 'localhost',
    user = 'username', #add your mysql username
    password = 'password' #add your mysql password

)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE website")
print('All Done !')
