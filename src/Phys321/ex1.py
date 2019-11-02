####
### Title: 	Numerical Solution Projectile Motion
### Author: Spencer Riley
### Python Version: 2.7.13
####

from numpy import *
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Time [s]
t       = linspace(0,8, 100)
# Angle off of horizon  [degrees]
theta   = deg2rad(30)

## Some Constants
g       = 9.81 # Gravitational acceleration [m/s^2]
D       = 76e-3 # Diameter [m]
m       = 0.145 # Mass [kg]
## Initial Conditions
r0      = 0.0 # Initial Height [m]
r1      = 30.0 # Initial Velocity [m/s]
init    = r0,r1
## Air Resistance coefficients
b       = 1.6e-4 * D # Linear
c       =  0.25 * (D**2) # Quadratic

# Analytical Solution without drag
y_p = -(0.5 * g * t**2) + r1*t +r0

## Linear Drag
# X-Component
def linear_x(y,t):
    x1 = y[1]*cos(theta)
    x2 = -((b/m) * x1)
    return x1,x2
# Y-Component
def linear_y(y,t):
    y1 = y[1]*sin(theta)
    y2 = -g - ((b/m) * y1)
    return y1,y2
## Quadratic Drag
# X-Component
def quad_x(y,t):
    x1 = y[1]*cos(theta)
    x2 = -((c/m)*(x1**2))
    return x1,x2
# Y-Component
def quad_y(y,t):
    y1 = y[1]*sin(theta)
    y2 = -g - ((c/m)*(y1**2))
    return y1,y2
## Both Linear and Quadratic Drag
# X-Component
def liqu_x(y,t):
    x1 = y[1]*cos(theta)
    x2 = -g - ((b/m)*x1) - ((c/m)*(x1**2))
    return x1,x2
# Y-Component
def liqu_y(y,t):
    y1 = y[1]*sin(theta)
    y2 = -g - ((b/m)*y1) - ((c/m)*(y1**2))
    return y1,y2
## Linear Drag ODE Solution
sol_ly  = odeint(linear_y, init, t)
sol_lx  = odeint(linear_x, init, t)
## Quadratic Drag ODE Solution
sol_qy  = odeint(quad_y, init, t)
sol_qx  = odeint(quad_x, init, t)
## Linear and Quadratic Drag ODE Solution
sol_lqy  = odeint(liqu_y, init, t)
sol_lqx  = odeint(liqu_x, init, t)

## Plot Stuff
plt.plot(r1*t, y_p, label="No Drag")
plt.plot(sol_lx[:,0], sol_ly[:, 0], label="Linear Drag")
plt.plot(sol_qx[:,0], sol_qy[:, 0], label="Quad Drag")
plt.plot(sol_lqx[:,0], sol_lqy[:, 0], label="Some More Drag")

plt.axhline(0)

plt.xlim(0, max(sol_lx[:,0] + sol_qx[:,0] + sol_lqx[:,0]))
plt.ylim(0, max(sol_ly[:,0] + sol_qy[:,0] + sol_lqy[:,0]))

plt.ylabel("Height [m]")
plt.xlabel("Distance [m]")
plt.title(r"Trajectories with Air Resistance {}$^o$".format(rad2deg(theta)))

plt.legend()
plt.show()
