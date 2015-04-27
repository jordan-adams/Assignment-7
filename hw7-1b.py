# -*- coding: utf-8 -*-
# Jordan Adams
# Assignment 7 1b

import numpy as np
import math as mh
import pylab as py

N = 1000
a = 0.0
b = 10.0
h = (b-a)/N              # All of these from examples in book pg 337
g = 9.81                 # Gravitational constant (in m/s)
l = 0.15                 # Length of pendulum (in m)
r = np.array([89,0],float)
t = 0.0
tpts = np.arange(a,b,h)
xpts = []
ypts = []

def f(r,t):
    omega = r[1]
    theta = r[0]
    f.theta = omega
    f.omega = -1*(g)*mh.sin(theta)
    return np.array ([f.theta,f.omega],float)
    
def j(t):
    return t

for t in tpts:
    xpts.append(r[0])
    ypts.append(r[1])
    halfstep = j(t) + (0.5*h*f(r,t))
    k1 = h*f(halfstep,t + 0.5*h)
    singlestep = j(t) + k1
    r += (j(t) + h*f(halfstep,t + 0.5*h)) - (halfstep + h*f(singlestep,t + h))

py.plot(tpts,xpts)
py.xlabel("Time (sec)")
py.ylabel("Theta (deg)")
py.show()
    