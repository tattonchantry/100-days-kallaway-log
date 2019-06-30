# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 09:10:04 2019

@author: Brodie

This still does not work, but I want to upload it to show some progress on
my 100 days of coding.
"""
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

# Initial condition.
x = 0.0
x0 = 0
x0 = np.asarray(x0)

# Number of iterations to compute.
n = 100

# number of realizations to compute
m = 1000


x = np.zeros((1000,100))
dt = 1/n

x[:3] = np.random.uniform(-1, 1, 100)

for k in range(m):
    x[k,:] = np.random.uniform(-1, 1, 50)

plt.plot(r)

