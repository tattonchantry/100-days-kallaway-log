# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 09:10:04 2019

@author: Brodie

Brownian walk in an array.

# TODO: Need to add labels.
# TODO: Not utilizing the dt.
"""
import matplotlib.pyplot as plt
import numpy as np

# Initiale condition
x = np.zeros((1000,100))

# Number of iterations to compute.
n = 100

# number of realizations to compute
m = 1000

# Time step
dt = 1/n

x[:1] = np.random.uniform(-1, 1, 100)

for k in range(1, len(x)):
    x[k:k + 1] = x[k-1:k] + np.random.uniform(-1, 1, 100)

plt.plot(x[0], c='k')

# How much it's above zero
w = np.array(x[0] > 0)

# How much it's below zero
u = np.array(x[0] < 0)

# Proportion of time it's above zero
v = sum(w) / len(x[0])
