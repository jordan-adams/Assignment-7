# -*- coding: utf-8 -*-
# Jordan Adams
# Assignment 7 1a

import numpy as np
import math as mh
import pylab as py


N = 1000
a = 0.0
b = 10.0
h = (b-a)/N              # All of these from examples in book pg 337
g = 9.81                 # Gravitational constant (in m/s)
l = 0.1                  # Length of pendulum (in m)
r = np.array([178,0],float)
t = 0.0

def f(r,t):
    omega = r[1]
    theta = r[0]
    f.theta = omega
    f.omega = -1*(g)*mh.sin(theta)
    return np.array ([f.theta,f.omega],float)

tpts = np.arange(a,b,h)
xpts = []
ypts = []

for t in tpts:
    xpts.append(r[0])
    ypts.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6 # 4th order RK method from book

py.plot(tpts,xpts)
py.xlabel("Time (sec)")
py.ylabel("Theta (degrees)")
py.show()


print(tpts,xpts,ypts)
