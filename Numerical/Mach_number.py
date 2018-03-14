#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 13:33:56 2018

@author: maxvansplunteren
"""
from SVV_FD_input import *
import numpy as np
def ISA(h):
    #Constants:
    gamma = 1.4
    ps = 101325.0
    Ts = 288.15
    rho = 1.225
    gs = 9.80665
    R = 287.00
    alt = [0, 11000, 20000, 32000, 47000, 51000, 71000, 86000, 1000000000];
    a = [-0.0065, 0.0, 0.001, 0.0028, 0.0, -0.0028, -0.002, 0.0];
    i = 0
 
    while h > alt[i]:
        if h >= alt[i+1]:
            he = alt[i+1] - alt[i]
        else:
            he = h - alt[i]
        T1 = Ts + a[i]*he
        if a[i] == 0.0:
            rho = rho*(np.exp((-gs/(R*T1))*(he)))
        else:
            rho = rho*(T1/Ts)**(-(gs)/((R*a[i]))-1)
        Ts = T1
        i = i+1
    
    p = rho*T1*R
    a = np.sqrt(gamma*R*T1)
    return rho , T1, p, a

def Mach_number(Vc,p):
    gamma = 1.4
    rho_0 = 1.225
    p_0 = 101325
    M = np.sqrt((2/(gamma-1))*((1+(p_0/p)*((1+(((gamma-1)*rho_0*(Vc**2))/(2*gamma*p_0)))**(gamma/(gamma-1))-1))**((gamma-1)/gamma)-1))

    return M

h = 11000*0.3048
[rho_isa,T_isa,p_isa,a] = ISA(h)
Vc = V_ias_m_c
TAT = TAT_m_c
M =  [Mach_number(i,p_isa) for i in Vc]
T_static = [(TAT[i]/(1+(0.2*(M[i]**2))))for i in range(len(M))]
T_delta = [TAT[i]-T_isa for i in range(len(M))]
hp = [h for i in range(len(M))]
thrust = np.transpose(np.vstack((hp,M,T_delta,FFL_m_c,FFR_m_c)))

