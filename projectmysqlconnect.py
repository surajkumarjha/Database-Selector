import mysql.connector as mc
from mysql.connector import Error
try:
    connection = mc.connect(host='localhost',
                             database='python_db',
                             user='demo',
                             password='password')
    if connection.is_connected():
       db_Info = connection.get_server_info()
       print("Connected to MySQL database... MySQL Server version on ",db_Info)
       cursor = connection.cursor()
       cursor.execute("select database();")
       record = cursor.fetchone()
       print ("Your connected to - ", record)
except Error as e :
    print ("Error while connecting to MySQL", e)
# finally:
#     #closing database connection.
#     if(connection.is_connected()):
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")

# ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root'
# grant all privileges on *.* to 'root'@'localhost';