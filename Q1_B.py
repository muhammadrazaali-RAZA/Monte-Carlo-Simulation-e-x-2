# -*- coding: utf-8 -*-
"""
Created on Sun May  9 08:46:36 2021

@author: Raza_Jutt
"""

import random
import matplotlib.pyplot as plt
import numpy as np

x = []
for i in range(0,101):
    x.append(i/100)
    
y=[]
for i in x:
    y.append(pow(2.71828,i*i))
    
rand_x = []
rand_y = []
for i in range(0,10000):
    rand_x.append(random.uniform(0.00,1.00))
    rand_y.append(random.uniform(1.00,2.75))
    
xpoints = np.array(x)
ypoints = np.array(y)

x_coordinates = rand_x
y_coordinates = rand_y

plt.plot(xpoints, ypoints,'r')
plt.scatter(x_coordinates, y_coordinates,s=0.1, marker="x")


plt.show()

count = 0
for i in range(0,10000):
    x=rand_x[i]
    if pow(2.71828,x*x) > rand_y[i] :
        count += 1

print(count/10000)