# -*- coding: utf-8 -*-
# Jordan Adams
# Assignment 7 2

import numpy as np
import pylab as py

A,B,C,D = 1.0,0.5,0.5,2.0 # Coefficient parameters for differential equation
N = 1000
a = 0.0
b = 10.0
h = (b-a)/1000
tpts = np.arange(a,b,h)
xpts = []
ypts = []
r = np.array([2,2],float) #Initial conditions of x=2 y=2

def f(r,t):
    x = r[0]
    y = r[1]
    Gx = A*x-B*x*y
    Gy = C*x*y-D*y
    return np.array([Gx,Gy],float)
    
for t in tpts:
    xpts.append(r[0])
    ypts.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6 # 4th order RK method from book

py.plot(tpts,xpts,label="X as a function of time")
py.plot(tpts,ypts,label="Y as a function of time")
py.legend()
py.show()
