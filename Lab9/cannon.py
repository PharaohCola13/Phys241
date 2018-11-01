# Spencer Riley
from __future__ import division, print_function
from visual import *
from visual.graph import *

# Creates the graphical display for Energy
#graph1 = gdisplay(title="Spring Energies", x=0, y=400, width=800, height=400, xtitle="Time [t]", ytitle="Energy [J]")

g = 9.81
x_axis = arrow()
x_axis.pos = vector(0,0,0)
x_axis.axis = 1e4 *vector(1, 0, 0)
x_axis.color = color.red

y_axis = arrow()
y_axis.pos = vector(0,0,0)
y_axis.axis = 1e4 *vector(0, 1, 0)
y_axis.color = color.blue

z_axis = arrow()
z_axis.pos = vector(0,0,0)
z_axis.axis = 1e4 *vector(0, 0, 1)
z_axis.color = color.yellow

angles = [30, 35, 40, 45, 50, 55] # in degrees

for i in angles:
	cannon = sphere()
	cannon.radius = 1000
	cannon.pos = vector(0, 0, 0)
	cannon.m = 10  # in kg
	if i == 30:
		cannon.color = color.orange
	elif i == 35:
		cannon.color = color.green
	elif i == 40:
		cannon.color = color.blue
	elif i == 45:
		cannon.color = color.magenta
	elif i == 50:
		cannon.color = color.cyan
	elif i == 55:
		cannon.color = color.red

	cannon.v = 700 * vector(cos(radians(i)), sin(radians(i)), cos(radians(90)))  # in m/s
	cannon.p = cannon.v * cannon.m
	Fgrav = cannon.m * vector(0, -g, 0)

	rho_0  = 1.225 #in kg/m^3
	y_0    = 1e4 # in m
	T_0    = 288.2 # in K
	alpha  = 2.5
	a      = 6.5e-3 # in K/m
	rho    = rho_0 * (1 - ((a*cannon.pos.y)/T_0))**alpha
	B = 4e-4
	B = B * (rho/rho_0)
	Fdrag = -B * mag(cannon.v)**2 * norm(cannon.v)

	Fnet = Fgrav + Fdrag

	t = 0
	dt = 0.1

	while True:
		rate(1000)

		if cannon.pos.y < 0.0:
			break

		cannon.p = cannon.p + Fnet * dt
		cannon.v = (cannon.p/cannon.m)
		cannon.pos = cannon.pos + cannon.v * dt

		t = t + dt

	t = t + dt
