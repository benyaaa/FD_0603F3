from SVV_FD_input import *
from Mach_number import *
import numpy as np
from SVV_FD_cog import *
import matplotlib.pyplot as plt
import scipy.interpolate as itp

#constants
L = 80.98 * 0.0254
mu = 1.599*10**(-5)
Ws = 60500
W_fuel_t = 4000*0.453592 - F_used_m_c
a_0 = np.sqrt(gamma*R*288.15)
W = [9.81*cog(pilot_1, pilot_2, coordinator, observer_1L, observer_1R, observer_2L, observer_2R, observer_3L, observer_3R, BEM, M_fuel_function, W_fuel_t,1)[0][i] for i in range(len(cog(pilot_1, pilot_2, coordinator, observer_1L, observer_1R, observer_2L, observer_2R, observer_3L, observer_3R, BEM, M_fuel_function, W_fuel_t,1)[0]))]


# airspeed and Reynolds for stationary
hs = h_m_c
p_isa_s = [ISA(hs[i])[2] for i in range(len(hs))]
rho_isa_s = [ISA(hs[i])[0] for i in range(len(hs))]
Vcs = V_ias_m_c
TAT_s = TAT_m_c
Ms =  [Mach_number(Vcs[i],p_isa_s[i]) for i in range(len(Vcs))]
T_static_s = [(TAT_s[i]/(1+(0.2*(Ms[i]**2))))for i in range(len(Ms))]


V_e_s = [a_0 * Ms[i] * np.sqrt(p_isa_s[i]/ps) for i in range(len(p_isa_s))]
V_t_s = [a_0 * Ms[i] * np.sqrt(T_static_s[i]/Ts) for i in range(len(Ms))]
Re_s = [(rho_isa_s[i]*V_t_s[i]*L)/mu for i in range(len(rho_isa_s))]


# airpseed and Reynolds for Elevation
he = h_m_e
p_isa_e = [ISA(he[i])[2] for i in range(len(he))]
rho_isa_e = [ISA(he[i])[0] for i in range(len(he))]
Vce = V_ias_m_e
TAT_e = TAT_m_e
Me =  [Mach_number(Vce[i],p_isa_e[i]) for i in range(len(p_isa_e))]
T_static_e = [(TAT_e[i]/(1+(0.2*(Me[i]**2))))for i in range(len(Me))]

V_e_e = [a_0 * Me[i] * np.sqrt(p_isa_e[i]/ps) for i in range(len(p_isa_e))]
V_t_e = [a_0 * Me[i] * np.sqrt(T_static_e[i]/Ts) for i in range(len(Me))]
Re_e = [(rho_isa_e[i]*V_t_e[i]*L)/mu for i in range(len(rho_isa_e))]
V_red_e = [V_e_e[i]*np.sqrt(Ws/W[i]) for i in range(len(W))]

#plot Fe-V_red_e
F_red_e = [F_e_m_e[i]*(Ws/W[i]) for i in range(len(W))]
x = np.arange(V_red_e[3], V_red_e[5], 0.001)
f = itp.interp1d(V_red_e, F_red_e, kind='cubic')
print V_red_e
print F_red_e
plt.plot(V_red_e, F_red_e, 'o', x,f(x), '-')
plt.legend(['data',  'cubic interpolation'], loc='best')
plt.xlabel('V_red_e')
plt.ylabel('F_red_e')
plt.title('X')
plt.show()
