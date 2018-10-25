from __future__ import division, print_function
from visual import *
from visual.graph import *


graph1 = gdisplay(title="Spring Energies", x=0, y=400, width=400, height=400)
Kplot = gcurve(gdisplay = graph1, color=color.green)
Uplot = gcurve(gdisplay = graph1, color=color.red)
Kplusplot = gcurve(display= graph1, color=color.blue)



k = 1.5 #in N/m
L0 = 0.9 # in meters

wall1 		= box()
wall1.color = color.yellow
wall1.pos 	= vector(0, 0,0)
wall1.size	= vector(0.25, 1, 1)

block        = box(make_trail = True)
block.pos    = vector(0.6,0, 0)
block.size   = vector(0.75, 0.75, 0.75)
block.m      = 0.02
block.color  = color.magenta
block.p      = block.m * vector(0,0,0)

spring1 			 = helix()
spring1.pos          = wall1.pos
spring1.axis         = block.pos - wall1.pos
spring1.thickness    = 0.05
spring1.radius       = 0.3
spring1.coils        = 5
spring1.color        = color.blue

t = 0
dt = 0.001

eta = 0.03
A   = 0.75 * 0.75
g = 9.81

coeff = 0.15

Fnorm = g * block.m
Ffmag = coeff * Fnorm

while True:
	rate(1e6)

	s 		=  L0 - mag(block.pos)
	Fspring = k * s * norm(block.pos)

	Fdrag   = eta * A * block.p/block.m
	Ff      = Ffmag * norm(block.p)

	Fnet 	=  Fspring - Ff

	block.p     = block.p + Fnet*dt
	block.pos   = block.pos + block.p/block.m * dt

	spring1.axis = block.pos - wall1.pos

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
