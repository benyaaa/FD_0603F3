%Input file

rho_0 = 1.225;           %[kg/m^3]

%Weight
pilot_1 = 95;            %[kg]
pilot_2 = 82;            %[kg]
coordinator = 82;        %[kg]
observer_1L = 89;        %[kg]
observer_1R = 72;        %[kg]
observer_2L = 61;        %[kg]
observer_2R = 67;        %[kg]
observer_3L = 77;        %[kg]
observer_3R = 108;       %[kg]

%location
pilot_1 = 95;            %[m]
pilot_2 = 82;            %[m]
coordinator = 82;        %[m]
observer_1L = 89;        %[m]
observer_1R = 72;        %[m]
observer_2L = 61;        %[m]
observer_2R = 67;        %[m]
observer_3L = 77;        %[m]
observer_3R = 108;       %[m]

%initial fuel weight
W_f_i = 4000 * 0.453592; %[kg]

%measured data for stationary, C_L, C_D
t_m_c = [1255, 1398, 1613, 1718, 1855, 1934];                     %[s]
h_m_c = [11020, 11020, 11010, 11010, 11030, 11010] * 0.3048;      %[m]
V_ias_m_c = [247, 221, 192, 161, 130, 118] * 0.514444;            %[m/s]
alpha_m_c = [1.6, 2.4, 3.5, 5.4, 8.8, 11];                        %[degrees]
FFL_m_c = [764, 662, 512, 449, 414, 415] * 0.000125998;           %[kg/s]
FFR_m_c = [773, 635, 525, 466, 435, 445] * 0.000125998;           %[kg/s]
F_used_m_c = [461, 504, 558, 585, 614, 631] * 0.453592;           %[kg]
TAT_m_c = [0.5, -1.5, -3.5, -5.8, -7.2, -7.8] + 273.15;           %[K]

%measured data for elevator trim curve
t_m_e = [2238, 2349, 2467, 2580, 2699, 2777, 2875];                     %[s]
h_m_e = [11300, 11700, 11210, 12620, 11730, 11380, 10770] * 0.3048;     %[m]
V_ias_m_e = [167, 157, 148, 138, 179, 187, 199] * 0.514444;             %[m/s]
alpha_m_e = [4.8, 5.6, 6.4, 7.5, 4.0, 3.5, 3.1];                        %[degrees]
delta_e_m_e = [0.2, -0.2, -0.5, -1.1, 0.6, 0.9, 1.1];                   %[degrees]
delta_e_tr_m_e = [3, 3, 3, 3, 3, 3, 3];                                 %[degrees]
F_e_m_e = [1, -13, -21, -42, 31, 62, 90];                              %[N]
FFL_m_e = [459, 453, 445, 439, 457, 463, 474] * 0.000125998;            %[kg/s]
FFR_m_e = [483, 477, 472, 462, 482, 488, 495] * 0.000125998;            %[kg/s]
F_used_m_e = [714, 747, 775, 809, 835, 853, 881] * 0.453592;            %[kg]
TAT_m_e = [-5.8, -7.1, -9.0, -9.8, -6.0, -4.5, -3.0] + 273.15;          %[K]

%measured data for shift in centre of gravity
t_m_s = [3006, 3100];                                                   %[s]
h_m_s = [11360, 11330] * 0.3048;                                        %[m]
V_ias_m_s = [167, 167] * 0.514444;                                      %[m/s]
alpha_m_s = [4.7, 4.8];                                                 %[degrees]
delta_e_m_s = [0.2, -0.4];                                              %[degrees]
delta_e_tr_m_s = [3, 3];                                                %[degrees]
F_e_m_s = [2, -34];                                                     %[N]
FFL_m_s = [460, 460] * 0.000125998;                                     %[kg/s]
FFR_m_s = [484, 482] * 0.000125998;                                     %[kg/s]
F_used_m_s = [915, 941] * 0.453592;                                     %[kg]
TAT_m_s = [-6.0, -6.0] + 273.15;                                        %[K]



