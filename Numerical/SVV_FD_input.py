from numpy import *
from math import *
import scipy.interpolate as itp
import matplotlib.pyplot as plt

#Input file

rho_0 = 1.225           #[kg/m^3]
MAC = 2.055622        #[m]
#Weights and cog location
pilot_1 = array([[95],[131*0.0254]])                #[kg]
pilot_2 = array([[82],[131*0.0254]])                #[kg]
coordinator = array([[82],[170*0.0254]])            #[kg]
observer_1L = array([[89],[214*0.0254]])            #[kg]
observer_1R = array([[72],[214*0.0254]])            #[kg]
observer_2L = array([[61],[251*0.0254]])            #[kg]
observer_2R = array([[67],[251*0.0254]])            #[kg]
observer_3L = array([[77],[288*0.0254]])            #[kg]
observer_3R = array([[108],[288*0.0254],[150*0.0254]])           #[kg]
BEM = array([[9165*0.45359237],[292.18*0.0254]])



#Fuel Moment 4000-2500 [pounds, m*kg]
M_fuel_solo = array([1141820*0.0254*0.45359237,1113100*0.0254*0.45359237,1084387*0.0254*0.45359237,1055684*0.0254*0.45359237,1027008*0.0254*0.45359237,998340*0.0254*0.45359237,969697*0.0254*0.45359237,941062*0.0254*0.45359237,912480*0.0254*0.45359237,883904*0.0254*0.45359237,855405*0.0254*0.45359237,826906*0.0254*0.45359237,798434*0.0254*0.45359237,769960*0.0254*0.45359237,741533*0.0254*0.45359237,713100*0.0254*0.45359237])
M_fuel = array([arange(4000,2400,-100),M_fuel_solo])
M_fuel_function = itp.interp1d(M_fuel[0],M_fuel[1])






#measured data for stationary, C_L, C_D
t_m_c = array([1255, 1398, 1613, 1718, 1855, 1934])                     #[s]
h_m_c = array([11020, 11020, 11010, 11010, 11030, 11010]) * 0.3048      #[m]
V_ias_m_c = array([247, 221, 192, 161, 130, 118]) * 0.514444            #[m/s]
alpha_m_c = array([1.6, 2.4, 3.5, 5.4, 8.8, 11])                        #[degrees]
FFL_m_c = array([764, 662, 512, 449, 414, 415]) * 0.000125998           #[kg/s]
FFR_m_c = array([773, 635, 525, 466, 435, 445]) * 0.000125998           #[kg/s]
F_used_m_c = array([461, 504, 558, 585, 614, 631]) * 0.453592           #[kg]
TAT_m_c = array([0.5, -1.5, -3.5, -5.8, -7.2, -7.8]) + 273.15           #[K]

#measured data for elevator trim curve
t_m_e = array([2238, 2349, 2467, 2580, 2699, 2777, 2875])                     #[s]
h_m_e = array([11300, 11700, 11210, 12620, 11730, 11380, 10770]) * 0.3048     #[m]
V_ias_m_e = array([167, 157, 148, 138, 179, 187, 199]) * 0.514444             #[m/s]
alpha_m_e = array([4.8, 5.6, 6.4, 7.5, 4.0, 3.5, 3.1])                        #[degrees]
delta_e_m_e = array([0.2, -0.2, -0.5, -1.1, 0.6, 0.9, 1.1])                   #[degrees]
delta_e_tr_m_e = array([3, 3, 3, 3, 3, 3, 3])                                 #[degrees]
F_e_m_e = array([1, -13, -21, -42, 31, 62, 90])                               #[N]
FFL_m_e = array([459, 453, 445, 439, 457, 463, 474]) * 0.000125998            #[kg/s]
FFR_m_e = array([483, 477, 472, 462, 482, 488, 495]) * 0.000125998            #[kg/s]
F_used_m_e = array([714, 747, 775, 809, 835, 853, 881]) * 0.453592            #[kg]
TAT_m_e = array([-5.8, -7.1, -9.0, -9.8, -6.0, -4.5, -3.0]) + 273.15          #[K]

#measured data for shift in centre of gravity
t_m_s = array([3006, 3100])                                                   #[s]
h_m_s = array([11360, 11330]) * 0.3048                                        #[m]
V_ias_m_s = array([167, 167]) * 0.514444                                      #[m/s]
alpha_m_s = array([4.7, 4.8])                                                 #[degrees]
delta_e_m_s = array([0.2, -0.4])                                              #[degrees]
delta_e_tr_m_s = array([3, 3])                                                #[degrees]
F_e_m_s = array([2, -34])                                                     #[N]
FFL_m_s = array([460, 460]) * 0.000125998                                     #[kg/s]
FFR_m_s = array([484, 482]) * 0.000125998                                     #[kg/s]
F_used_m_s = array([915, 941]) * 0.453592                                     #[kg]
TAT_m_s = array([-6.0, -6.0]) + 273.15                                        #[K]
