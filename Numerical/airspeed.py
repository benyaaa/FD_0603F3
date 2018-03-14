from SVV_FD_input import *
from Mach_number import *
import numpy as np
from SVV_FD_cog import *

hs = h_m_c

p_isa_s = [ISA(hs[i])[2] for i in range(len(hs))]
rho_isa_s = [ISA(hs[i])[0] for i in range(len(hs))]
L = 80.98 * 0.0254
mu = 1.599*10**(-5)
Ws = 60500
W_fuel_t = 4000*0.453592 - F_used_m_c
W = cog(pilot_1, pilot_2, coordinator, observer_1L, observer_1R, observer_2L, observer_2R, observer_3L, observer_3R, BEM, M_fuel_function, W_fuel_t)

a_0 = np.sqrt(gamma*R*288.15)

Ve = [a_0 * M[i] * np.sqrt(p_isa_s[i]/ps) for i in range(len(p_isa_s))]

Vt = [a_0 * M[i] * np.sqrt(T_static[i]/Ts) for i in range(len(M))]

Re = [(rho_isa_s[i]*Vt[i]*L)/mu for i in range(len(rho_isa_s))]

#V_red_e = Ve*np.sqrt(Ws/W)
