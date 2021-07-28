import time
import numpy as np
from shutil import copyfile
import matplotlib.pyplot as plt
start_time = time.time()
#create
f = open("text.txt","w+")
for i in range(10000):
  f.write("Hello World,I am Shashank Kirtania\n")
  f.write("I love MachineLeanrning I am a beginner in MAchineLearning\n")
f.close()
count = 0
a=[]
#copy
while (count < 1000):
  destination = 'copy'+str(count)+'.txt'
  copyfile('text.txt', destination)
  count = count + 1
 #uppercase
t = time.time()
for i in range(1000):
  fileName = 'copy'+str(i)+'.txt'
  with open(fileName) as infile, open(fileName, "a") as outfile:
	    for line in infile:
	        outfile.write(line.upper())
  if i%5 == 0:
    a.append(int(time.time() - t))
    t=time.time()
plt.plot(a)