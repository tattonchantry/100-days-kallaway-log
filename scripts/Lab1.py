# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 20:25:32 2019

@author: Brodie
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size': 16})

# Define variable t as t=0:dt:3.1, where dt=0.1
dt = 0.1
t = np.arange(0,3.2,.1)#0:dt:3.1
#   o Calculate x=sin(t)
x = np.sin(t)
#   o Calculate variable y
#     o y(i)=(x(i+1)-x(i))/dt for i=1:31
i = np.linspace(0,30,31, dtype=int)
y = (x[i+1] - x[i]) / dt

#   o Calculate variable tm
#     o tm(i)=(t(i)+t(i+1))/2 for i=1:31
tm = (t[i] + t[i+1])/2
#     o Plot x vs t and y vs tm in the same figure

plt.plot(t,x, label=r'$\sin(x)$')
plt.plot(tm, y, label=r'$\frac{d}{dx} \sin(x)$')
plt.xlabel('Time')
plt.ylabel('y')
plt.tight_layout()
plt.legend()

plt.savefig('x_y.png')