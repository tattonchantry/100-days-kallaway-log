# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 14:33:03 2019

@author: Brodie
"""

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10, 10, 30)


m = 1/2
b = 4
y = m * x + b


point1 = [4, 1]
point2 = [7, 11]

change_b = 1
change_m = 0


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(x, m * x + b, 'r', label='y=mx+b')
plt.plot(x, (m + change_m) * x + (b + change_b), 'g', label='y=(m +_)x +(b+_)')
if change_m > 0:
    plt.plot(x, (m + (2 + change_m)) * x + (b + (2 + change_b)),
             'b', label='y=(m + 2+_)x +(b + 2+_)')
    plt.plot(x, (m + (3 + change_m)) * x + (b + (3 + change_b)),
             'm', label='y=(m + 3+_)x +(b + 3+_)')
else:
    plt.plot(x, m * x + (b + (2 + change_b)),
             ':b', label='y=2x+3')
    plt.plot(x, m * x + (b + (3 + change_b)),
             '--m', label='y=2x-3')
u = [point1[0], point2[0]]
v = [point1[1], point2[1]]
new_m = ((point2[1] - point1[1])/(point2[0] - point1[0]))
new_b = point1[1] - (new_m * point1[0])

plt.scatter(u, v, s=50, c='r', marker="*")
plt.plot(x, new_m * x + new_b, 'c')

plt.legend(loc='upper left')
plt.show()
