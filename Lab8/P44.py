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
g   = 9.81

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

t   = 0
dt  = 0.001

f1 = gcurve(gdisplay = gd1, color=color.white) # Define functions to plot


while True:
	rate(100)

	s           = mag(block.pos) - L0
	Fspring     = -k * s * norm(block.pos)
	Fnet        = fgrav + Fspring

	block.p     = block.p + Fnet*dt
	block.pos   = block.pos + block.p/block.m * dt

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

# a #K+U is not constant over time

# b #As the mass drops, the blue and red lines increase, while the green line decreases.

# c #As the kinetic energy increases the potential energy decreases at about the same amplitude, causing the sum to have little variation.
	t = t + dt