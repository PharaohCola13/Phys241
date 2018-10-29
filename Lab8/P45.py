from __future__ import division, print_function
from visual import *
from visual.graph import *

# Creates the graphical display for position
gd1 = gdisplay(x=550,y=0,width=700,height=500,
			   title='Position of block',
			   xtitle='Time [s]',
			   ytitle='Position [m]')

graph1 = gdisplay(title="Spring Energies", x=0, y=400, width=400, height=400)
Kplot = gcurve(gdisplay = graph1, color=color.green)
Uplot = gcurve(gdisplay = graph1, color=color.red)
Kplusplot = gcurve(display= graph1, color=color.blue)



k   = 0.9 # in N/m
L0  = 0.20 # in m
g   = 9.81 # in m/s^2

base                = box()
base.size           = vector(0.2, 0.01, 0.2)
base.pos            = vector(0,0,0)
base.color          = color.green

block               = sphere(make_trail=True)
block.pos           = vector(0, -0.1, 0)
#block.pos           = vector(1, -0.1, 10)
#block.pos
block.radius        = 0.025
block.m             = 0.02
block.v             = vector(0,0,0)
block.p             = block.m * block.v
block.color         = color.orange

spring              = helix()
spring.pos          = base.pos
spring.axis         = block.pos - base.pos
spring.thickness    = 0.003
spring.radius       = 0.01
spring.coils        = 40

fgrav = block.m * g * vector(0,-1,0)

# Initial Time
t   = 0
# Time Step
dt  = 0.001

f1 = gcurve(gdisplay = gd1, color=color.white) # Define functions to plot

# Stuff needed for Frictional Force
A  = pi * block.radius**2 # Cross sectional area in m^2
rho = 1.225 # Density of Air in
C   = 0.5

while True:
	rate(1e5)
# Spring Force
	s           = mag(block.pos) - L0
	Fspring     = -k * s * norm(block.pos)
# Frictional Force
	Fdrag       = 0.5 * C * rho * A * (mag(block.p)/block.m)**2 * norm(block.p)
# Net Force
	Fnet        = fgrav + Fspring - Fdrag
# Updates block momentum
	block.p     = block.p + Fnet*dt
# Updates block position
	block.pos   = block.pos + block.p/block.m * dt
# Updates Spring final position
	spring.axis = block.pos - base.pos

	f1.plot(pos=(t, block.pos.y))  # Plots position vs time


# Calculates the Kinetic Energy
	K = 0.5 * (mag(block.p) ** 2 / block.m)
# Calculates the gravitational potential energy
	U = 0.5 * k * s**2

# Plot Kinetic Energy as a function of the displacement
	Kplot.plot(pos=(t, K))
# Plot Gravitational Potential energy as a function of displacement
	Uplot.plot(pos=(t, U))
# Ploy the sum of both Kinetic and potential energies as a function of displacement
	Kplusplot.plot(pos=(t, K + U))

# Update Time
	t = t + dt

# The rate of dissipation is not constant, there is a larger rate of dissipation towards the initial time
# As time progresses there is less available energy