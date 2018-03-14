#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 21:10:50 2018

@author: Roemer
"""

from SVV_FD_input import *

#Weight and Center of Gravity 
#Needs numerical input for fuel weight at time t in pounds
#returns cog[0] and cog[1]
def cog(pilot_1, pilot_2, coordinator, observer_1L, observer_1R, observer_2L, observer_2R, observer_3L, observer_3R, BEM, M_fuel_function, W_fuel_t):
    M_pilot_1 = pilot_1[0] * pilot_1[1]
    M_pilot_2 = pilot_2[0] * pilot_2[1]
    M_coordinator = coordinator[0] * coordinator[1]
    M_observer_1L = observer_1L[0] * observer_1L[1]
    M_observer_1R = observer_1R[0] * observer_1R[1]
    M_observer_2L = observer_2L[0] * observer_2L[1]
    M_observer_2R = observer_2R[0] * observer_2R[1]
    M_observer_3L = observer_3L[0] * observer_3L[1]
    M_observer_3R = observer_3R[0] * observer_3R[1]
    M_BEM = BEM[0] * BEM[1]
    W_total_t = pilot_1[0] + pilot_2[0] + coordinator[0] + observer_1L[0] + observer_1R[0] + observer_2L[0] + observer_2R[0] + observer_3L[0] + observer_3R[0] + BEM[0] + (W_fuel_t*0.45359237)
    M_total_t = M_pilot_1 + M_pilot_2 + M_coordinator + M_observer_1L + M_observer_1R + M_observer_2L + M_observer_2R + M_observer_3L + M_observer_3R + M_BEM + M_fuel_function(W_fuel_t)
    X_cog_datum = M_total_t/W_total_t
    return W_total_t, X_cog_datum #return aircraft total weight [kg] at time t and center of gravity [m] at time t
