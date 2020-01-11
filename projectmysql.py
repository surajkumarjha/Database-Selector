import mysql.connector
import time
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
  host="localhost",
  user="demo",
  password="password",
  database="python_db"
)

mycursor = mydb.cursor()
a = []	
b = []

for i in range(100, 1001, 100):
	for y in range(i):
		start_time = time.time()
		sql = "INSERT INTO python_try (name, owner) VALUES (%s, %s)"
		val = ("John", "Highway 21")
		mycursor.execute(sql, val)
	end_time = time.time()
	total = end_time - start_time
	a.append(total)
	mydb.commit()
	print(y, "Records Inserted")
for x in range(100, 1001, 100):
	b.append(x)
print(a)
plt.plot(a, b, color='green', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=12) 

plt.xlabel('Time Taken')
plt.ylabel('No. of Records')
plt.title('Insertion Time Graph')
plt.show()
