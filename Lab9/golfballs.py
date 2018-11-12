# Spencer Riley
from __future__ import division, print_function
from visual import *
from visual.graph import *

# Creates the graphical display for the trajectory of each scenario
graph1 		= gdisplay(title="Trajectories with Varying Spin", x=0, y=400, width=800, height=400, xtitle="Position in X [m]", ytitle="Position in Y [m]")
senone 		= gcurve(display= graph1, color=color.cyan)
label(display=graph1.display, pos=(300,50),color=color.cyan, text="No spin")
sentwo 		= gcurve(display= graph1, color=color.green)
label(display=graph1.display, pos=(300,60),color=color.green, text="Normal Spin")
senthree 	= gcurve(display= graph1, color=color.red)
label(display=graph1.display, pos=(300,70),color=color.red, text="50% More Spin")
senfour 	= gcurve(display= graph1, color=color.magenta)
label(display=graph1.display, pos=(300,80),color=color.magenta, text="C = 0.5")

# Constant
g 	= 9.81 # in m/s^2
senario = [0, 0.25, 1.5 * 0.25, "Four"]

# Creates X axis
x_axis 		= arrow()
x_axis.pos 	= vector(0,0,0)
x_axis.axis 	= 60 *vector(1, 0, 0)
x_axis.color 	= color.red

# Creates Y axis
y_axis 		= arrow()
y_axis.pos 	= vector(0,0,0)
y_axis.axis 	= 60 *vector(0, 1, 0)
y_axis.color 	= color.blue

# Creates Z axis
z_axis 		= arrow()
z_axis.pos 	= vector(0,0,0)
z_axis.axis 	= 60 *vector(0, 0, 1)
z_axis.color 	= color.yellow

for i in senario:
# Creates ball
	golfball 	= sphere(make_trail=True)
	golfball.radius = 1
	golfball.pos 	= vector(0, 0, 0)
# Mass of the ball
	golfball.m 	= 0.04  # in kg
# Velocity of the ball, magnitude is 70 m/s
	golfball.v 	= 70 * vector(cos(radians(9)), sin(radians(9)), cos(radians(90)))  # in m/s

	golfball.p 	= golfball.v * golfball.m # in kg m/s
	Fgrav 		= golfball.m * vector(0, -g, 0) # in N
# Drag Coefficient
	C 	= 7/mag(golfball.v)
# Air Density at sea level
	rho 	= 1.225  		# in kg.m^3
# Radius of golf ball, diamter: 0.04267 m
	radius 	= 0.021335 		# in m
# Cross-Sectional Area
	A 	= pi * radius ** 2 	# in m^2
# Inital Time
	t 	= 0 # in s
# Time Step
	dt 	= 0.1
	while i == senario[0]:
		rate(10)
		golfball.color = color.cyan
# When the ball goes below zero it stops
		if golfball.pos.y < 0.0:
			break
# Force of Drag
		Fdrag 	= -C * rho * A * mag(golfball.v)** 2 * norm(golfball.v) # in N
# Net Force
		Fnet 	= Fgrav + Fdrag # in N
# Updates ball momentum
		golfball.p 	= golfball.p + Fnet * dt # in kg m/s
# Update ball velocity
		golfball.v 	= (golfball.p / golfball.m) # in m/s
# Update ball position
		golfball.pos 	= golfball.pos + golfball.v * dt # in m
# Plots trajectory plot
		senone.plot(pos=(golfball.pos.x, golfball.pos.y))
# Update Time
		t = t + dt # in s

	while i == senario[1]:
		rate(10)
		golfball.color = color.green
# When the ball goes below zero it stops
		if cannon.pos.y < 0.0:
			break
# Force of Drag
		Fdrag 	= -C * rho * A * mag(cannon.v)** 2 * norm(cannon.v) # in N
# Magnus Force
		Fmagnus = vector(-i * cannon.p.y, i * cannon.p.x, 0) # in N
# Net Force
		Fnet 	= Fgrav + Fdrag + Fmagnus # in N
# Updates ball momentum
		golfball.p 	= golfball.p + Fnet * dt # in kg m/s
# Update ball velocity
		golfball.v 	= (golfball.p / golfball.m) # in m/s
# Update ball position
		golfball.pos 	= golfball.pos + golfball.v * dt # in m
# Plots trajectory plot
		sentwo.plot(pos=(golfball.pos.x, golfball.pos.y))
# Update Time
		t = t + dt # in s
	while i == senario[2]:
		rate(10)
		golfball.color = color.red
# When the ball goes below zero it stops
		if cannon.pos.y < 0.0:
			break
# Force of Drag
		Fdrag 	= -C * rho * A * mag(golfball.v)** 2 * norm(golfball.v) # in N
# Magnus Force
		Fmagnus = vector(-i * golfball.p.y, i * golfball.p.x, 0) # in N
# Net Force
		Fnet 	= Fgrav + Fdrag + Fmagnus # in N
# Updates ball momentum
		golfball.p 	= golfball.p + Fnet * dt # in kg m/s
# Update ball velocity
		golfball.v 	= (golfball.p / golfball.m) # in m/s
# Update ball position
		golfball.pos 	= golfball.pos + golfball.v * dt # in m
# Plots trajectory plot
		senthree.plot(pos=(golfball.pos.x, golfball.pos.y))
# Update Time
		t = t + dt # in s
	while i == senario[3]:
		rate(10)
		golfball.color = color.magenta
# When the ball goes below zero it stops
		if cannon.pos.y < 0.0:
			break
# Coefficient of Drag
		C 	= 0.5
# Force of Drag
		Fdrag 	= -C * rho * A * mag(golfball.v)** 2 * norm(golfball.v) # in N
# Magnus Force
		Fmagnus = vector(-0.25 * golfball.p.y, 0.25 * golfball.p.x, 0) # in N
# Net force
		Fnet 	= Fgrav + Fdrag + Fmagnus # in N
# Updates ball momentum
		golfball.p 	= golfball.p + Fnet * dt # in kg m/s
# Update ball velocity
		golfball.v 	= (golfball.p / golfball.m) # in m/s
# Update ball position
		golfball.pos 	= golfball.pos + golfball.v * dt # in m
# Plots trajectory plot
		senfour.plot(pos=(golfball.pos.x, golfball.pos.y))
# Update Time
		t = t + dt # in s
