# Spencer Riley
from __future__ import division, print_function
from visual import *
from visual.graph import *

# Creates the graphical display for Energies
graph1 = gdisplay(title="Spring Energies", x=0, y=400, width=800, height=400, xtitle="Time [t]", ytitle="Energy [J]")
Kplot = gcurve(gdisplay = graph1, color=color.green)
label(display=graph1.display, pos=(0,0.04),color=color.green, text="Kinetic Energy")
Uplot = gcurve(gdisplay = graph1, color=color.red)
label(display=graph1.display, pos=(0,0.02),color=color.red, text="Potential Energy")
Kplusplot = gcurve(display= graph1, color=color.blue)
label(display=graph1.display, pos=(0,0),color=color.blue, text="Total Energy")


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
block.p             = block.m * vector(0,0,0)
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


while True:
	rate(100)
# Spring Force
	s           = mag(block.pos) - L0
	Fspring     = -k * s * norm(block.pos)
	Fnet        = fgrav + Fspring
# Updates block momentum
	block.p     = block.p + Fnet*dt
# Updates block position
	block.pos   = block.pos + block.p/block.m * dt
# Updates spring final position
	spring.axis = block.pos - base.pos

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
