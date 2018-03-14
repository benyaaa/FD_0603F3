from SVV_FD_input import *
from Mach_number import *
import numpy as np

L = 80.98 * 0.0254
mu = 1.599*10**(-5)

a_0 = np.sqrt(gamma*R*288.15)

Ve = [a_0 * M[i] * np.sqrt(p_isa/ps) for i in range(len(M))]

Vt = [a_0 * M[i] * np.sqrt(T_static[i]/Ts) for i in range(len(M))]

Re = [(rho_isa*Vt[i]*L)/mu for i in range(len(Vt))]

