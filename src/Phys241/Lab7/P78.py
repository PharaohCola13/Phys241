# Spencer Riley
from __future__ import print_function, division
from visual import *
from visual.graph import *

graph1 = gdisplay(title="Orbital Energies", x=0, y=400, width=400, height=400)

Kplot = gcurve(gdisplay = graph1, color=color.green)

Uplot = gcurve(gdisplay = graph1, color=color.red)

Kplusplot = gcurve(display= graph1, color=color.blue)

# Declare constants
D = 6.4e7  # 10 times the radius of the Earth in meters
G = 6.7e-11  # Nm2/kg2

# Creates Earth
earth = sphere()
earth.pos = vector(0, 0, 0)
earth.radius = 0.1
earth.material = materials.earth
earth.v = vector(0, 0, 0)
earth.m = 6e24  # in kg
earth.p = earth.m * earth.v

# Space Craft
craft = sphere(make_trail=True)
craft.pos = vector(1, 0, 0)
craft.radius = 0.01
craft.color = color.white
craft.m = 1.5e4  # in kg

# Circular Orbit
#craft.v        = vector(0, sqrt(G * earth.m/(mag(craft.pos) * D)), 0)

# Elliptical Orbit
craft.v = 0.75 * vector(0, sqrt(G * earth.m / (mag(craft.pos) * D)), 0)

# Initial momentum of craft
craft.p = craft.m * craft.v

t = 0  # Initial Time
dt = 60  # Time step

while True:
	rate(1e3)

# Distance between the craft and the earth
	r = (craft.pos - earth.pos) * D
	rmag = mag(r)
	rhat = norm(r)

# Gravitational Force
	Fmag = G * (earth.m * craft.m) / rmag ** 2
	Fnet = -Fmag * rhat

# Update Momentum of craft
	craft.p = craft.p + Fnet * dt
# Update Position of craft
	craft.pos = craft.pos + (craft.p / craft.m / D) * dt

# Kinetic Energy
	K = 0.5 * (mag(craft.p)**2/craft.m)
# Potential Energy
	U = -G * (earth.m * craft.m)/rmag

#  Plots Kinetic Energy as a function of displacement
	Kplot.plot(pos=(rmag, K))
# Plots Potential Energy as a function of displacement
	Uplot.plot(pos=(rmag, U))
# Plots the sum of the Kinetic Potential Energy as a function of displacement
	Kplusplot.plot(pos=(rmag, K+U))

# Updates Time
	t = t + dt
