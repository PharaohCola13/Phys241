# Spencer Riley
from __future__ import division, print_function
from visual import *
from visual.graph import *

# Creates the graphical display for the trajectory of each scenario
graph1 = gdisplay(title="Trajectories without Drag", x=0, y=400, xtitle="Positon in X [km]", ytitle="Position in Y [km]", ymax=2E1, ymin=-2E0)
# Constants
g 	= 9.81 # in m/s^2
# List of angles
angles = linspace(30, 55, 6).tolist()

# Creates X axis
x_axis 		= arrow()
x_axis.pos 	= vector(0,0,0)
x_axis.axis 	= 1e4 *vector(1, 0, 0)
x_axis.color 	= color.red

# Creates Y axis
y_axis 		= arrow()
y_axis.pos 	= vector(0,0,0)
y_axis.axis 	= 1e4 *vector(0, 1, 0)
y_axis.color 	= color.blue

# Creates Z axis
z_axis 		= arrow()
z_axis.pos 	= vector(0,0,0)
z_axis.axis 	= 1e4 *vector(0, 0, 1)
z_axis.color 	= color.yellow

# Part A
for i in angles:
	plot = gcurve(display=graph1)
	llabel = label(display=graph1.display, text="{}^o".format(i), height=10)
# Creates a ball
	cannon 		= sphere(make_trail=True)
	cannon.radius 	= 1000
	cannon.pos 	= vector(0, 0, 0) # in m
	cannon.m 	= 10  # in kg
# Velocity of the ball
	cannon.v 	= 700 * vector(cos(radians(i)), sin(radians(i)), cos(radians(90)))  # in m/s
# Momentum of ball
	cannon.p 	= cannon.v * cannon.m # in kg m/s
# Force of gravity on ball
	Fgrav 		= cannon.m * vector(0, -g, 0) # in N
# Drag coefficient
	B = 4e-4 # in kg/m
# Initial Time
	t = 0 # in s
# Time step
	dt = 0.01 # in s
	while True:
		rate(100000)
# Breaks loop when cannon hits floor
		if cannon.pos.y < 0.0:
			break
# Force of drag
		Fdrag = vector(0,0,0)
# Net force
		Fnet = Fgrav  + Fdrag # in N
		cannon.color = plot.color
# Updates momentum
		cannon.p = cannon.p + Fnet * dt  # in kg m/s
# Updates velocity
		cannon.v = (cannon.p / cannon.m)  # in m/s
# Updates position
		cannon.pos = cannon.pos + cannon.v * dt  # in m

		plot.plot(pos=(cannon.pos.x / 1000, cannon.pos.y / 1000))
		llabel.color = plot.color
		if i == 30:
			plot.color=color.red
			llabel.pos = (20, 6)
		elif i == 35:
			plot.color=color.orange
			llabel.pos=(25, 8)
		elif i == 40:
			plot.color = color.yellow
			llabel.pos=(25, 10)
		elif i == 45:
			plot.color = color.green
			llabel.pos=(25, 12)
		elif i == 50:
			plot.color=color.cyan
			llabel.pos=(30, 14)
		elif i == 55:
			plot.color=color.magenta
			llabel.pos=(25, 17)
# Updates Time
		t = t + dt # in s
# Part B
plot1 = gdisplay(title="Trajectories with Drag", x=500, y=400, xtitle="Positon in X [km]", ytitle="Position in Y [km]", ymax=2E1, ymin=-2E0,)
for i in angles:
	curve = gcurve(display=plot1)
	llabel = label(display=plot1.display, text="{}^o".format(i), height=10)
# Creates a ball
	cannon 		= sphere(make_trail=True)
	cannon.radius 	= 1000
	cannon.pos 	= vector(0, 0, 0) # in m
	cannon.m 	= 10  # in kg
# Velocity of the ball
	cannon.v 	= 700 * vector(cos(radians(i)), sin(radians(i)), cos(radians(90)))  # in m/s
# Momentum of ball
	cannon.p 	= cannon.v * cannon.m # in kg m/s
# Force of gravity on ball
	Fgrav 		= cannon.m * vector(0, -g, 0) # in N
# Drag coefficient
	B = 4e-4 # in kg/m
# Initial Time
	t = 0 # in s
# Time step
	dt = 0.01 # in s
	while True:
		rate(100000)
# Breaks loop when cannon hits floor
		if cannon.pos.y < 0.0:
			break
# Force of drag
		Fdrag = -B * mag(cannon.v) ** 2 * norm(cannon.v)  # in N
# Net force
		Fnet = Fgrav  + Fdrag # in N
		cannon.color = plot.color
# Updates momentum
		cannon.p = cannon.p + Fnet * dt  # in kg m/s
# Updates velocity
		cannon.v = (cannon.p / cannon.m)  # in m/s
# Updates position
		cannon.pos = cannon.pos + cannon.v * dt  # in m

		curve.plot(pos=(cannon.pos.x / 1000, cannon.pos.y / 1000))
		llabel.color = curve.color
		if i == 30:
			curve.color=color.red
			llabel.pos = (20, 20)
		elif i == 35:
			curve.color=color.orange
			llabel.pos=(20, 18)
		elif i == 40:
			curve.color = color.yellow
			llabel.pos=(20, 16)
		elif i == 45:
			curve.color = color.green
			llabel.pos=(20, 14)
		elif i == 50:
			curve.color=color.cyan
			llabel.pos=(20, 12)
		elif i == 55:
			curve.color=color.magenta
			llabel.pos=(20, 10)

# Updates Time
		t = t + dt # in s
# Part C
plot2 = gdisplay(title="Plot of 35 and 45 Degrees with and without Density Correction", x=500, y=400, xtitle="Positon in X [km]", ytitle="Position in Y [km]", ymax=2E1, ymin=-2E0,)
for i in [35, 45]:
	for m in ["with", "without"]:
		curve2 = gcurve(display=plot2)
		llabel = label(display=plot2.display, text="{}^o, {} density correction".format(i, m), height=10)
# Creates a ball
		cannon 		= sphere(make_trail=True)
		cannon.radius 	= 1000
		cannon.pos 	= vector(0, 0, 0) # in m
		cannon.m 	= 10  # in kg
# Velocity of the ball
		cannon.v 	= 700 * vector(cos(radians(i)), sin(radians(i)), cos(radians(90)))  # in m/s
# Momentum of ball
		cannon.p 	= cannon.v * cannon.m # in kg m/s
# Force of gravity on ball
		Fgrav 		= cannon.m * vector(0, -g, 0) # in N
# Initial Time
		t = 0 # in s
# Time step
		dt = 0.01 # in s
		if m == "with":
			while True:
				rate(100000)
# Breaks loop when cannon hits floor
				if cannon.pos.y < 0.0:
					break
				rho_0 = 1.225  # in kg/m^3
# Predefined variable
				y_0 = 1e4  # in m
# Absolute Temperature at sea level
				T_0 = 288.2  # in K
# Predefined variable
				alpha = 2.5
# Predefined variable
				a = 6.5e-3  # in K/m
# Density with altitude dependence
				rho = rho_0 * (1 - ((a * cannon.pos.y) / T_0)) ** alpha
				B = B * (rho/rho_0)
# Force of drag
				Fdrag = -B * mag(cannon.v) ** 2 * norm(cannon.v)  # in N
# Net force
				Fnet = Fgrav  + Fdrag # in N
				cannon.color = plot.color
# Updates momentum
				cannon.p = cannon.p + Fnet * dt  # in kg m/s
# Updates velocity
				cannon.v = (cannon.p / cannon.m)  # in m/s
# Updates position
				cannon.pos = cannon.pos + cannon.v * dt  # in m

				curve2.plot(pos=(cannon.pos.x / 1000, cannon.pos.y / 1000))
				llabel.color = curve2.color
				if i == 35:
					curve2.color=color.red
					llabel.pos=(45, 20)
				elif i == 45:
					curve2.color = color.orange
					llabel.pos=(45, 18)
		if m == "without":
			while True:
				rate(100000)
# Breaks loop when cannon hits floor
				if cannon.pos.y < 0.0:
					break
# Drag coefficient
				B = 4e-4  # in kg/m
# Force of drag
				Fdrag = -B * mag(cannon.v) ** 2 * norm(cannon.v)  # in N
# Net force
				Fnet = Fgrav + Fdrag  # in N
				cannon.color = plot.color
# Updates momentum
				cannon.p = cannon.p + Fnet * dt  # in kg m/s
# Updates velocity
				cannon.v = (cannon.p / cannon.m)  # in m/s
# Updates position
				cannon.pos = cannon.pos + cannon.v * dt  # in m
				curve2.plot(pos=(cannon.pos.x / 1000, cannon.pos.y / 1000))
				llabel.color = curve2.color
				if i == 35:
					curve2.color = color.yellow
					llabel.pos = (45, 16)
				elif i == 45:
					curve2.color = color.green
					llabel.pos = (45, 14)
