""" Patient's inflammation analysis for day 1 """

import numpy as np
import matplotlab.pyplot as plt

data = np.loadtxt(fname='data/inflammation1.csv', delimiter=',')

image-1=plt.plot(data)

plt.show(image-1)