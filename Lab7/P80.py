# Spencer Riley
from __future__ import print_function, division
from visual import *

from visual.graph import *

scene = display(x=0, y=0, width=500, height=500)
scene.range  = 3e8
scene.center = vector(-2e8, 0, 0)

graph1 = gdisplay(title="Orbital Energies", x=0, y=400, width=400, height=400)
Kplot = gcurve(gdisplay = graph1, color=color.green)
Uplot = gcurve(gdisplay = graph1, color=color.red)
Kplusplot = gcurve(display= graph1, color=color.blue)


# Declare constnts
D = 6.4e7  # 10 times the radius of the Earth in meters
G = 6.7e-11  # Gravitational Constant in Nm2/kg2

# Create objects
earth = sphere()
earth.pos = vector(0, 0, 0)
earth.radius = 6.4e6
earth.material = materials.earth
earth.m = 6e24  # in kg

moon = sphere()
moon.pos = vector(-4e8, 0, 0)
moon.radius = 1.7e6
moon.color = color.white
moon.m = 7.4e22 # in kg

craft = sphere(make_trail=True)
craft.pos = vector(D, 0, 0)
craft.radius = 1e6
craft.color = color.white

craft.m = 1.5e4  # in kg

# Orbits both Earth and Moon
craft.v = vector(0, 3.27e3, 0)

craft.p = craft.m * craft.v

t = 0  # Initial Time
dt = 60  # Time step

while True:
	rate(1e3)

	# Distance between the craft and the earth
	r = (craft.pos - earth.pos)
	rmag = mag(r)
	rhat = norm(r)
	#Distance between craft and moon
	r1 = (craft.pos - moon.pos)
	rmag1 = mag(r1)
	rhat1 = norm(r1)

	# Gravitational Force of Earth-craft system
	Fmag  = -G * (earth.m * craft.m)/rmag**2
	#Gravitational force of Moon-craft system
	Fmag1 = -G * (moon.m * craft.m)/rmag1**2

	# Net force
	Fnet = (Fmag * rhat) + (Fmag1 * rhat1)

	# Update Momentum of craft
	craft.p = craft.p + Fnet * dt

	# Update Position of craft
	craft.pos = craft.pos + (craft.p/craft.m) * dt

	#Calculates the Kinetic Energy
	K = 0.5 * (mag(craft.p)**2 / craft.m)
	#Calculates the gravitational potential energy
	U = (-G * (earth.m * craft.m)/rmag) + (-G * (moon.m * craft.m)/rmag1)

	#Plot Kinetic Energy as a function of the displacement
	Kplot.plot(pos=(rmag, K))
	#Plot Gravitational Potential energy as a function of displacement
	Uplot.plot(pos=(rmag, U))
	#Ploy the sum of both Kinetic and potential energies as a function of displacement
	Kplusplot.plot(pos=(rmag, K + U))
	# Update Time
	t = t + dt