""" Patient's inflammation analysis for day 1 """

import numpy as np
import matplotlab.pyplot as plt

data = np.loadtxt(fname='data/inflammation1.csv', delimiter=',')

#Finding dimensions of data
print(data.shape)
print(data)

#Print just the first row of data getting day 1 data
print(data[0])

#Plotting data

image-1=plt.plot(data)
# Test merge change

plt.show(image-1)

#Adrienne's changes!