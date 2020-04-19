import matplotlib.pyplot as plt
from numpy import *

a       = 0.06
T_s     = 5779.13
R_s     = 6.9627e8
D       = 67.357e9
theta   = linspace(-pi/2, pi/2, 100)
Temp    = pow(1 - a, 1./4.) * T_s * sqrt(R_s/D) * pow(cos(theta),1./4.)
plt.scatter(rad2deg(theta), Temp)
plt.xlabel(r"$\theta$ [$^\circ$]")
plt.xlim(-100, 100)
plt.ylabel("Temperature [K]")
plt.title("Surface Temperature of Mercury by Latitude")
plt.show()
