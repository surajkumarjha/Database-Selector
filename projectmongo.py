import pymongo
import math
import random
import time
import matplotlib.pyplot as plt
connection = pymongo.MongoClient("mongodb://localhost")
database = connection.pes
collection = database.mca0
rand = ["name","aakash","suraj","chirag","bunty"]
a = []
b = []
c = []

for i in range(100, 1001, 100):
	start_time = time.time()
	for y in range(i):
		user_id = y
		name = rand[int(math.floor(random.random()*len(rand)))] 
		number = math.floor(random.random()*100);
		x = {"user_id":user_id,"name":name,"number":number}
		collection.insert(x)
	end_time = time.time()
	total = end_time - start_time
	a.append(total)
documents = collection.find()
for i in documents:
	print(i)
number = documents.count()
print(number)
print(a)
for x in range(100, 1001, 100):
	b.append(x)
print(b)
# plt.plot(a,b)
plt.plot(a, b, color='green', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=12) 

plt.xlabel('Time Taken')
plt.ylabel('No. of Records')
plt.title('Insertion Time Graph')
plt.show()
	



# for i in range(100, 1001, 100):
# 	for y in range(i):
# 		name = 'chirag'
# 		strt_time = time.time()
# 		documents.collection.findOne(name)
# 		endd_time = time.time()
# 		tot = endd_time - strt_time
# 		c.append(tot)
# print(c)


