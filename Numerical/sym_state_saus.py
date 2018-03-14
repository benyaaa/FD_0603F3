"""
Created on Wed Mar 14 10:09:50 2018

@author: Ferran
"""
import numpy as np
from math import *
import scipy as sp
import matplotlib.pyplot as plt
from control.matlab import *

#from Cit_par import *
# parameter values
m = 3.0
b = 9.0
k = 60.0
# matrices
A = np.matrix([[-b/m, -k/m], [1, 0]])
B = np.matrix([[ 1/m], [ 0]])
C = np.matrix([[ 0, 1]])
D = np.matrix([[ 0]])
# system
sys = ss(A, B, C, D)
