# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 09:58:29 2019

@author: Brodie
"""

import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1,1], [2,2.5], [3, 1], [5, 5], [6, 6.5], [7, 5]])
Y = ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']

fig, ax = plt.subplots()
ax.add_patch(plt.Circle((0, 0), 3, color='r'))#, alpha=0.5))
plt.scatter(X[:, 0], X[:, 1], s = 170, color = Y[:])

t1 = plt.Polygon(X[:3,:], color=Y[0])
plt.gca().add_patch(t1)
#
#t2 = plt.Polygon(X[3:6,:], color=Y[3])
#plt.gca().add_patch(t2)

plt.show()
