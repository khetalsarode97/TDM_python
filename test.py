import mysql.connector

connection = mysql.connector.connect(host='14.99.175.107',port ='17633', database='flexib_db', user='root', password='root')
print(connection)