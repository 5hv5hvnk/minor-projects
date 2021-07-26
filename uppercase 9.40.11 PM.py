import time
import numpy as np
from shutil import copyfile
import matplotlib.pyplot as plt
start_time = time.time()
#create
f = open("text.txt","w+")
for i in range(1000):
  f.write("Hello World,I am Shashank Kirtania\n")
  f.write("I love MachineLeanrning I am a beginner in MAchineLearning\n")
f.close()
count = 0
a=[]
#copy
while (count < 10):
  destination = 'copy'+str(count)+'.txt'
  copyfile('text.txt', destination)
  count = count + 1
 #uppercase
for i in range(10):
	fileName = 'copy'+str(i)+'.txt'
	with open(fileName) as infile, open(fileName, "a") as outfile:
	    for line in infile:
	        outfile.write(line.upper())
	if i%25 == 0:
		print("--- %s seconds ---" % (time.time() - start_time))
		a.append(int(time.time() - start_time))
plt.plot(a)