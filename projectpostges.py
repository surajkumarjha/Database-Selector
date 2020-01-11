import psycopg2
import time
import sys 
import matplotlib.pyplot as plt


mydb = psycopg2.connect(
  host="localhost",
  user="postgres",
  password="postgres",
  database="postgres"
)

mycursor = mydb.cursor()
a = []	
b = []

for i in range(10, 101, 10):
	for y in range(i):
		start_time = time.time()
		sql = "INSERT INTO company VALUES ( 'suraj', 23,'Delhi',5000)"
	mycursor.execute(sql)
	end_time = time.time()
	mydb.commit()
	total = end_time - start_time
	a.append(total)
	print(i,"records inserted.")
for x in range(10, 101, 10):
	b.append(x)
print(a)
plt.plot(a, b, color='green', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=12) 

plt.xlabel('Time Taken')
plt.ylabel('No. of Records')
plt.title('Insertion Time Graph')
plt.show()