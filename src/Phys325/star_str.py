########
## Title: star_str.py
## Author: Spencer Riley
## Python 3.5.2
########
## Import Stuff
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
## Conversion Constants
sol_mass = 1.9891e30 # [kg]
sol_radi = 6.96e8 #[m]
## Data files
fname = "./structure_00000.txt"
fsum  = "./summary.txt"
# Imports Mass
mass        = loadtxt(fsum, delimiter=",", unpack=True)[2][0]
# Imports Luminosity
lumino      = loadtxt(fsum, delimiter=",", unpack=True)[3][0]
# Imports Radius
radius      = loadtxt(fsum, delimiter=",", unpack=True)[4][0]
# Imports central density
cen_den     = loadtxt(fsum, delimiter=",", unpack=True)[7][0]
# Imports central temperature
cen_temp    = loadtxt(fsum, delimiter=",", unpack=True)[6][0]
# Imports surface temperature
surf_temp   = loadtxt(fsum, delimiter=",", unpack=True)[5][0]
# Imports radial coordinate
r_coor      = loadtxt(fname, delimiter=",", unpack=True)[1]
# Import Mass Coordinate
m_coor      = loadtxt(fname, delimiter=',', unpack=True)[0]
# Imports density data
rho         = loadtxt(fname, delimiter=",", unpack=True)[4]
# Imports luminosity data
lum         = loadtxt(fname, delimiter=",", unpack=True)[2]
# Imports temperature data
tem         = loadtxt(fname, delimiter=",", unpack=True)[5]
# Import Pressure Data
pres        = loadtxt(fname, delimiter=",", unpack=True)[3]
e_pres      = loadtxt(fname, delimiter=",", unpack=True)[13]
r_pres      = loadtxt(fname, delimiter=",", unpack=True)[14]

# Import Energy Generation Data
e_nu        = loadtxt(fname, delimiter=",", unpack=True)[19]
e_pp        = loadtxt(fname, delimiter=",", unpack=True)[20]
e_cno       = loadtxt(fname, delimiter=",", unpack=True)[21]
e_3a        = loadtxt(fname, delimiter=",", unpack=True)[22]

# Import Energy loss data
e_nn        = loadtxt(fname, delimiter=",", unpack=True)[23]
e_nnn       = loadtxt(fname, delimiter=",", unpack=True)[24]
e_gc        = loadtxt(fname, delimiter=",", unpack=True)[25]

mean_den    = (mass * sol_mass)/((4.0/3.0) * pi * ((10**(radius)) * sol_radi)**3)

## Prints out properties given by the handout
print("The Luminosity:\t\t {:.2E} L_sun".format(10**(lumino)))
print("The Radius:\t\t {:.2E} R_sun".format(10**(radius)))

print("The mean density:\t {:.2E} kg/m^3".format(mean_den))
print("The central density:\t {:.2E} kg/m^3".format(10**(cen_den)))

print("The central temperature: {:.2E} K".format(10**(cen_temp)))
print("The surface temperature: {:.2E} K".format(10**(surf_temp)))

# Plots Density against Radial Corrdinate
fig1 = plt.figure(1)
ax1 = fig1.add_subplot(2,1,1)
ax1.set_title(r"Radial Coordiante vs $\rho$")
ax1.plot(r_coor, rho)
ax1.axhline(mean_den, color="r", label=r"$\bar\rho$ = {:.2}".format(mean_den))
ax1.set_ylabel(r"Density [kg/m$^3$]")
plt.legend()

# Plots Pressure against Radial Corrdinate
ax2 = fig1.add_subplot(2,1,2)
ax2.set_title("Radial Coordinate vs Pressure")
ax2.plot(r_coor, pres)
ax2.plot(r_coor, e_pres, label=r"e$^-$ Pressure")
ax2.plot(r_coor, r_pres, label="Radiation Pressure")
ax2.set_xlabel(r"Radius [R/R$_\odot$]")
ax2.set_ylabel(r"Pressure [N/m$^2$]")
plt.legend()
plt.subplots_adjust(left=0.13, hspace=0.34)

# Plots Luminosity against Radial Corrdinate
fig2 = plt.figure(2)
ax1 = fig2.add_subplot(2,1,1)
ax1.set_title("Radal Coordinate vs Luminosity")
ax1.plot(r_coor, lum)
ax1.set_ylabel(r"Luminosity [L/L$_\odot$]")

# Plots Temperature against Radial Corrdinate
ax2 = fig2.add_subplot(2,1,2)
ax2.set_title("Radial Coordiante vs Temperature")
ax2.plot(r_coor, tem)
ax2.set_xlabel(r"Radius [R/R$_\odot$]")
ax2.set_ylabel(r"Temperature [K]")
plt.subplots_adjust(left=0.13, hspace=0.34)

# Plots Energy Generation against Radial Corrdinate
fig3 = plt.figure(3)
ax1 = fig3.add_subplot(2,1,1)
ax1.set_title("Energy Generation in Star")
ax1.plot(r_coor, e_nu, label="Total")
ax1.plot(r_coor, e_pp, label="PP Chains")
ax1.plot(r_coor, e_cno, label="CNO Chains")
ax1.plot(r_coor, e_3a, label=r"3$\alpha$ Chains")
ax1.set_ylabel(r"Power [W/kg]")
ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2E'))
plt.legend()

# Plots Energy Loss against Radial Corrdinate
ax2 = fig3.add_subplot(2,1,2)
ax2.set_title("Energy Loss in Star")
ax2.plot(r_coor, e_nn, label="Nuclear Neutrinos")
ax2.plot(r_coor, e_nnn, label="Non-Nuclear Neutrinos")
ax2.plot(r_coor, e_gc, label="Gravitational Contraction")
ax2.set_xlabel(r"Radius [R/R$_\odot$]")
ax2.set_ylabel(r"Power [W/kg]")
ax2.yaxis.set_major_formatter(FormatStrFormatter('%.2E'))
plt.subplots_adjust(left=0.19, hspace=0.34)
plt.legend()

# Plots Mass coordinate against Radial Coordinate
fig4 = plt.figure(4)
plt.plot(r_coor, m_coor)
plt.title("Radial Coordinate vs Mass Coordinate")
plt.xlabel(r"Radius [R/R$_\odot$]")
plt.ylabel(r"Mass [M/M$_\odot$]")
# Shows some plots
plt.show()
