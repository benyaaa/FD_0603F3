"""
Created on Wed Mar 14 10:09:50 2018

@author: Ferran
"""
import numpy as np
from math import *
import scipy as sp
import matplotlib.pyplot as plt
from control.matlab import *
from Cit_par import *

# parameter values
V = V0

CXdt = 0.
CZdt = 0.
Cmdt = 0.

x_u = (V*CXu)/(MAC*2*muc)
x_a = (V*CXa)/(MAC*2*muc)
x_theta = (V*CZ0)/(MAC*2*muc)
x_q = (V*CXq)/(MAC*2*muc)
x_de = (V*CXde)/(MAC*2*muc)
x_dt = (V*CXdt)/(MAC*2*muc)    #Need to determine CXdt; is CXdt = 0 since the trimtab angle does not change

z_u = (V/MAC)*(CZu/(2*muc-CZadot))
z_a = (V/MAC)*(CZa/(2*muc-CZadot))
z_theta = -(V/MAC)*(CX0/(2*muc-CZadot))
z_q = (V/MAC)*((2*muc+CZq)/(2*muc-CZadot))
z_de = (V/MAC)*(CZde/(2*muc-CZadot))
z_dt = (V/MAC)*(CZdt/(2*muc-CZadot))  #Need to determine CZdt; is CZdt = 0 since the trimtab angle does not change

m_u = (V/MAC)*((Cmu+CZu*(Cmadot)/(2*muc-CZadot))/(2*muc*KY2))   #Note KY2 is not supposed to be squared!!!
m_a = (V/MAC)*((Cma+CZa*(Cmadot)/(2*muc-CZadot))/(2*muc*KY2)) 
m_theta = -(V/MAC)*((CX0*(Cmadot)/(2*muc-CZadot))/(2*muc*KY2)) 
m_q = (V/MAC)*((Cmq+Cmadot*(2*muc+CZq)/(2*muc-CZadot))/(2*muc*KY2))
m_de = (V/MAC)*((Cmde+CZde*(Cmadot)/(2*muc-CZadot))/(2*muc*KY2)) 
m_dt = (V/MAC)*((Cmdt+CZdt*(Cmadot)/(2*muc-CZadot))/(2*muc*KY2))     #Need to determine CZdt; is CZdt = 0 since the trimtab angle does not change 
# matrices
A = np.matrix([[x_u, x_a, x_theta, x_q], #4x4
               [z_u, z_a, z_theta, z_q],
               [0., 0., 0., V/MAC],
               [m_u, m_a, m_theta, m_q]])
B = np.matrix([[x_de],    #4x1
               [z_de],
               [0.],
               [m_de]])
C = np.matrix([[1., 0., 0., 0.]]) #1x4
D = np.matrix([[0.]]) #1x1

# system

sys = ss(A, B,C,D)
T = np.arange(0.,20.1,0.1)
y, t = step(sys,T)
plt.plot(t,y)
plt.show()

print sp.linalg.eig(A)
