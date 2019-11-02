####
### Title: 	2.9
### Author: Spencer Riley
### Python Version: 2.7.13
####
import matplotlib.pyplot as plt
from numpy import *
# Constants
tau     = 1.0e6         # yrs
G       = 6.672e-11     # Nm^2/kg s^2
sigma   = 5.67e-8       # W/m^2/K^4
# Solar unit conversion
R_sun   = 6.9627e8      # m
L_sun   = 3.85e26       # W
M_sun   = 1.9891e30     # kg
# Protostar properties
dm_0    = 2.0e-6 * M_sun
R_0     = 3.0 * R_sun
M_0     = 0.01 * M_sun
# Time range
t = arange(0.05*tau, 0.95*tau + 0.05*tau, 0.05*tau)
# accretion mass rate
dm  = dm_0 - ((dm_0 * t)/(tau))
# Mass
M_t = (M_0 + (dm_0* t * (1.- (t/(2.*tau)))))
# Luminosity
L_t = (((G*M_t)/(2.*R_0)) * dm)/3.154e+7
# Temperature
T_t = ((L_t/(4.*pi*(R_0**2.)*sigma))**(1./4.))
# Maximum wavelength
l_t = ((2.89777e-3)/T_t)/(1e-6)
# Prints table
print("t [My]" + " \t | " + "M(t) [M_sun]" + " | " + "L(t) [L_sun]" + "  | " + "T(t) [K]" + " | " + "lambda(t) [um]")
print("---"*15)
for i in range(len(M_t)):
     print("{:.2E} | {:.2E} \t| {:.2E} \t| {:.2E} | {:.2E}".format(t[i]/tau,M_t[i]/M_sun, L_t[i]/L_sun, T_t[i], l_t[i]))

# Plots HR diagram
plt.scatter(T_t, L_t/L_sun)
plt.xlim(10000, 1000)
plt.xlabel("Temperature [K]")
plt.ylabel(r"Luminosity [$L_{\odot}$]")
plt.title("Hertzsprung-Russell Diagram of Protostar")
plt.show()