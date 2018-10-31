from __future__ import division, print_function
from visual import *
from visual.graph import *

graph1 = gdisplay(title="Spring Energies", x=0, y=400, width=400, height=400)
Kplot = gcurve(gdisplay = graph1, color=color.green)
Uplot = gcurve(gdisplay = graph1, color=color.red)
Kplusplot = gcurve(display= graph1, color=color.blue)



k = 1.5 #in N/m
L0 = 0.9 # in meters

wall 		= box()
wall.color  = color.yellow
wall.pos 	= vector(0, 0,0)
wall.size	= vector(0.25, 1, 1)

block        = box(make_trail = True)
block.pos    = vector(0.6,0, 0)
block.size   = vector(0.75, 0.75, 0.75)
block.m      = 0.02
block.color  = color.magenta
block.p      = block.m * vector(0,0,0)

spring 			 	= helix()
spring.pos          = wall.pos
spring.axis         = block.pos - wall.pos
spring.thickness    = 0.05
spring.radius       = 0.3
spring.coils        = 5
spring.color        = color.blue

# Initial Time
t = 0
# Time Step
dt = 0.001

# Viscous Force
eta = 0.03
A   = 0.75 * 0.75 # in m^2
g = 9.81 # in m/s^2

# Sliding Frictional Force
coeff = 0.15
Fnorm = g * block.m
Ffmag = coeff * Fnorm

while t <= 3000 * dt:
	rate(1e2)
# Spring Force
	s 		=  L0 - mag(block.pos)
	Fspring = k * s * norm(block.pos)

# Frictional Forces
	Fdrag   = eta * A * block.p/block.m
	Ff      = Ffmag * norm(block.p)

# Net Force
#	Fnet 	= Fspring
#	Fnet 	=  Fspring - Ff
	Fnet 	= Fspring - Fdrag
# Updates Block momentum
	block.p     = block.p + Fnet*dt
	block.pos   = block.pos + block.p/block.m * dt

# Updates Spring final position
	spring.axis = block.pos - wall.pos

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
	t = t +dt
