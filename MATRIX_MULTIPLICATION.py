#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import time
from matplotlib import pyplot as plt


# In[7]:


cross ={}
dot={}
for i in range(1,6):
    a = np.random.randint(1,100,(i*100,i*100))
    b = np.random.randint(1,100,(i*100,i*100))
    start = time.time()
    np.matmul(a,b)
    end = time.time()
    cross[i*100] = end - start
    start = time.time()
    c = a*b
    end = time.time()
    dot[i*100] = end - start


# In[8]:


dot_keys = list(dot.keys())


# In[9]:


dot_keys


# In[15]:


for i in list(dot.keys()):
    print(dot[i])


# In[16]:


for i in list(cross.keys()):
    print(str(cross_data[i]))


# In[18]:


plt.plot(list(dot.keys()),list(dot.values()),label="Dot Product")
plt.plot(list(cross.keys()),list(cross.values()),label="Matrix Product")
plt.legend()
plt.xlabel("Dimensions (a*a)")
plt.ylabel("Time")
plt.show()


# In[ ]:




