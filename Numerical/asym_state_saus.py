#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 08:35:58 2018

@author: maxvansplunteren
"""

import numpy as np
from math import *
import scipy as sp
import matplotlib.pyplot as plt
from control.matlab import *
from Cit_par import *

# parameter values
V = V0

y_b = (V*CYb)/(b*2*mub)
y_f = (V*CL)/(b*2*mub)
y_p = (V*CYp)/(b*2*mub)
y_r = (V*(CYr-(4*mub)))/(b*2*mub)
y_da = (V*CYda)/(b*2*mub)
y_dr = (V*CYdr)/(b*2*mub)

l_b = (V*(Clb*KZ2+Cnb*KXZ))/(b*4*mub*(KX2*KZ2-KXZ**2))
l_f = 0
l_p = (V*(Clp*KZ2+Cnp*KXZ))/(b*4*mub*(KX2*KZ2-KXZ**2))
l_r = (V*(Clr*KZ2+Cnr*KXZ))/(b*4*mub*(KX2*KZ2-KXZ**2))
l_da = (V*(Clda*KZ2+Cnda*KXZ))/(b*4*mub*(KX2*KZ2-KXZ**2))
l_dr = (V*(Cldr*KZ2+Cndr*KXZ))/(b*4*mub*(KX2*KZ2-KXZ**2))

n_b = (V*(Clb*KXZ+Cnb*KX2))/(b*4*mub*(KX2*KZ2-KXZ**2))
n_f = 0
n_p = (V*(Clp*KXZ+Cnp*KX2))/(b*4*mub*(KX2*KZ2-KXZ**2))
n_r = (V*(Clr*KXZ+Cnr*KX2))/(b*4*mub*(KX2*KZ2-KXZ**2))
n_da = (V*(Clda*KXZ+Cnda*KX2))/(b*4*mub*(KX2*KZ2-KXZ**2))
n_dr = (V*(Cldr*KXZ+Cndr*KX2))/(b*4*mub*(KX2*KZ2-KXZ**2))

# matrices
A = np.matrix([[y_b, y_f, y_p, y_r], #4x4
               [0., 0., 2*V/b, 0.],
               [l_b, 0., l_p, l_r],
               [n_b, 0., n_p, n_r]])
B = np.matrix([[0.,y_dr],    #4x2
               [0.,0.],
               [l_da,l_dr],
               [n_da,n_dr]])
C = np.matrix([[0., 0., 0., 1.],
               [0., 0., 1., 0.]]) #2x4
D = np.matrix([[0.,0.],[0.,0.]]) #2x2

T = np.arange(0.,15.1,0.1)
U1 = np.zeros((len(T),2))
U1[1:11,1]=0.025
# system for pitch
sys = ss(A, B,C,D)
y, t, x = lsim(sys,U1,T)

plt.plot(t,y*(2*V/b))
plt.show()

print sp.linalg.eig(A)