# Spencer Riley
from __future__ import division, print_function
from visual import *
from visual.graph import *

# Creates the graphical display for Energy
graph1 = gdisplay(title="Trajectories with Varying Spin", x=0, y=400, width=800, height=400, xtitle="Position in X [m]", ytitle="Position in Y [m]")
senone = gcurve(display= graph1, color=color.blue)
label(display=graph1.display, pos=(300,50),color=color.blue, text="No spin")
sentwo = gcurve(display= graph1, color=color.green)
label(display=graph1.display, pos=(300,60),color=color.green, text="Normal Spin")
senthree = gcurve(display= graph1, color=color.red)
label(display=graph1.display, pos=(300,70),color=color.red, text="50% More Spin")
senfour = gcurve(display= graph1, color=color.magenta)
label(display=graph1.display, pos=(300,80),color=color.magenta, text="C = 0.5")

g = 9.81
x_axis = arrow()
x_axis.pos = vector(0,0,0)
x_axis.axis = 60 *vector(1, 0, 0)
x_axis.color = color.red

y_axis = arrow()
y_axis.pos = vector(0,0,0)
y_axis.axis = 60 *vector(0, 1, 0)
y_axis.color = color.blue

z_axis = arrow()
z_axis.pos = vector(0,0,0)
z_axis.axis = 60 *vector(0, 0, 1)
z_axis.color = color.yellow

senario = [0, 0.25, 1.5 * 0.25, "Four"]

for i in senario:
	cannon = sphere(make_trail=True)
	cannon.radius = 1
	cannon.pos = vector(0, 0, 0)
	cannon.m = 0.04  # in kg
	cannon.v = 70 * vector(cos(radians(9)), sin(radians(9)), cos(radians(90)))  # in m/s

	cannon.p = cannon.v * cannon.m
	Fgrav = cannon.m * vector(0, -g, 0)

	C = 7/mag(cannon.v)

	rho = 1.225  # in kg.m^3
	radius = 0.021335
	A = pi * radius ** 2

	t = 0
	dt = 0.1

	while i == senario[0]:
		rate(10)
		cannon.color = color.blue

		if cannon.pos.y < 0.0:
			break
		Fdrag = -C * rho * A * mag(cannon.v) ** 2 * norm(cannon.v)
		Fnet = Fgrav + Fdrag

		cannon.p = cannon.p + Fnet * dt
		cannon.v = (cannon.p / cannon.m)
		cannon.pos = cannon.pos + cannon.v * dt

		# Plot Kinetic Energy as a function of the displacement
		senone.plot(pos=(cannon.pos.x, cannon.pos.y))

		t = t + dt

	while i == senario[1]:
		rate(10)

		cannon.color = color.green

		if cannon.pos.y < 0.0:
			break

		Fdrag = -C * rho * A * mag(cannon.v) ** 2 * norm(cannon.v)

		Fmagnus = vector(-i * cannon.p.y, i * cannon.p.x, 0)

		Fnet = Fgrav + Fdrag + Fmagnus

		cannon.p = cannon.p + Fnet * dt
		cannon.v = (cannon.p / cannon.m)
		cannon.pos = cannon.pos + cannon.v * dt


	# Plot Kinetic Energy as a function of the displacement
		sentwo.plot(pos=(cannon.pos.x, cannon.pos.y))

		t = t + dt
	while i == senario[2]:
		rate(10)

		cannon.color = color.red

		if cannon.pos.y < 0.0:
			break

		Fdrag = -C * rho * A * mag(cannon.v) ** 2 * norm(cannon.v)

		Fmagnus = vector(-i * cannon.p.y, i * cannon.p.x, 0)

		Fnet = Fgrav + Fdrag + Fmagnus

		cannon.p = cannon.p + Fnet * dt
		cannon.v = (cannon.p / cannon.m)
		cannon.pos = cannon.pos + cannon.v * dt


	# Plot Kinetic Energy as a function of the displacement
		senthree.plot(pos=(cannon.pos.x, cannon.pos.y))

		t = t + dt
	while i == senario[3]:
		rate(10)

		cannon.color = color.magenta

		if cannon.pos.y < 0.0:
			break

		C = 0.5
		Fdrag = -C * rho * A * mag(cannon.v) ** 2 * norm(cannon.v)

		Fmagnus = vector(-0.25 * cannon.p.y, 0.25 * cannon.p.x, 0)

		Fnet = Fgrav + Fdrag + Fmagnus

		cannon.p = cannon.p + Fnet * dt
		cannon.v = (cannon.p / cannon.m)
		cannon.pos = cannon.pos + cannon.v * dt

		# Plot Kinetic Energy as a function of the displacement
		senfour.plot(pos=(cannon.pos.x, cannon.pos.y))

		t = t + dt
