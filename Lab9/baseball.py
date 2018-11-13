# Spencer Riley
from __future__ import division, print_function
from visual import *
from visual.graph import *

# Note in advance, for some parts of the question I commented items out to produce the results in the lab document

# Creates the graphical display for the trajectory of each scenario
graph1      = gdisplay(title="Wind Speed Trajectories", x=0, y=400, width=750, height=500, xtitle="Position in X [m]", ytitle="Position in Y [m]")
windzero    = gcurve(display= graph1, color=color.cyan)
#label(display=graph1.display, pos=(30,5),color=color.cyan, text="0 mph")
windhead    = gcurve(display= graph1, color=color.green)
#label(display=graph1.display, pos=(30,7),color=color.green, text="10 mph")
#windtail    = gcurve(display= graph1, color=color.red)
#label(display=graph1.display, pos=(30,3),color=color.red, text="-10 mph")

label(display=graph1.display, pos=(150, 25), color=color.cyan, text="No Drag")
label(display=graph1.display, pos=(50, 10), color=color.green, text="Drag")


plot2       = gdisplay(title="Varying Angle Trajectories", x=400, y=400, width=750, height=450, xtitle="Position in X [m]", ytitle="Position in Y [m]")
# Constant
g       = 9.81 # in m/s^2
wind    = [0, 4.4704, -4.4704] # in m/s
lots_of_angles  = linspace(10, 60, 11).tolist()

# Creates a X axis
x_axis          = arrow()
x_axis.pos      = vector(0,0,0)
x_axis.axis     = 5 *vector(1, 0, 0)
x_axis.color    = color.red

# Creates a Y axis
y_axis          = arrow()
y_axis.pos      = vector(0,0,0)
y_axis.axis     = 5 *vector(0, 1, 0)
y_axis.color    = color.blue

# Creates a Z axis
z_axis          = arrow()
z_axis.pos      = vector(0,0,0)
z_axis.axis     = 5 *vector(0, 0, 1)
z_axis.color    = color.yellow

for i in wind:
# Creates a ball of defined mass
	baseball        = sphere(make_trail=True)
	baseball.radius = 0.1
	baseball.pos    = vector(0, 1, 0)
# Mass of ball
	baseball.m      = 0.150  # in kg
# Part a) initial velocity had a magnitude of 50 m/s
	baseball.v = 50 * vector(cos(radians(45)), sin(radians(45)), cos(radians(90)))  # in m/s

# Part c) initial velocity had a magnitude of 49.1744 m/s or 110 mph
#    baseball.v = 49.1744 * vector(cos(radians(35)), sin(radians(35)), cos(radians(90)))  # in m/s

	baseball.p = baseball.m * baseball.v # in kg m/s

# Wind velocity in vector form
	windv = vector(i, 0, 0) # in m/s

# The force of gravity acting on the ball
	Fgrav = baseball.m * vector(0, -g, 0) # in N

# Coefficient of Drag B = 1/2 * c * rho * A
	B = 0.0039 + (0.0058)/(1 + exp((mag(baseball.v) - 35)/5)) # in kg/m

# Part b) force of air resistance
	Fdrag = -B * mag(baseball.v)**2 * norm(baseball.v) # in N

# Part c) force of Drag with respect to the wind
	#Fdrag = -B * (mag(baseball.v) - mag(windv))**2 * (norm(baseball.v) - norm(windv)) # in N

# Initial Time
	t = 0 # in s
# Time step
	dt = 0.01 # in s
	while i == wind[0]:
		rate(100)
# When the ball goes below zero it stops
		if baseball.pos.y <= 0:
			break
# Net Force
		Fnet = Fgrav  #+ Fdrag # in N
# Momentum update of ball
		baseball.p = baseball.p + Fnet * dt  # in kg m/s
# Velocity update of ball
		baseball.v = (baseball.p / baseball.m)  # in m/s
# Position Update of ball
		baseball.pos = baseball.pos + baseball.v * dt  # in m

		baseball.color  = color.cyan
# Plots the trajectory
		windzero.plot(pos=(baseball.pos.x,baseball.pos.y))
# Updates Time
		t = t + dt # in s
	while i == wind[1]:
		rate(100)
# When the ball goes below zero it stops
		if baseball.pos.y <= 0.0:
			break
# Net Force
		Fnet = Fgrav  + Fdrag # in N
# Momentum update of ball
		baseball.p = baseball.p + Fnet * dt  # in kg m/s
# Velocity update of ball
		baseball.v = (baseball.p / baseball.m)  # in m/s
# Position Update of ball
		baseball.pos = baseball.pos + baseball.v * dt  # in m

		baseball.color  = color.green
# Plots the trajectory
		windhead.plot(pos=(baseball.pos.x, baseball.pos.y))
# Updates Time
		t = t + dt # in s
	while i == wind[2]:
		rate(100)
# When the ball goes below zero it stops
		if baseball.pos.y <= 0:
			break
# Net Force
		Fnet = Fgrav  + Fdrag # in N
# Momentum update of ball
		baseball.p = baseball.p + Fnet * dt  # in kg m/s
# Velocity update of ball
		baseball.v = (baseball.p / baseball.m)  # in m/s
# Position Update of ball
		baseball.pos = baseball.pos + baseball.v * dt  # in m

		baseball.color  = color.red
# Plots the trajectory
	#	windtail.plot(pos=(baseball.pos.x, baseball.pos.y))
# Updates Time
		t = t + dt # in s

# This is for the second section of part b
for a in lots_of_angles:
	set = gcurve(display=plot2, color=color.green)
	label(display=plot2.display, pos=(17- (a**2 - 3 * a)/400, (a - 1)/4 - 2), color=color.green, text="{}".format(a), height=9)

# Creates a ball of defined mass
	baseball        = sphere(make_trail=True)
	baseball.radius = 1
	baseball.pos    = vector(0, 1, 0)
# Mass of ball
	baseball.m      = 0.150  # in kg
# Part a) initial velocity had a magnitude of 50 m/s
	baseball.v = 50 * vector(cos(radians(a)), sin(radians(a)), cos(radians(90)))  # in m/s
# Momentum update of ball
	baseball.p      = baseball.m * baseball.v # in kg m/s

# The force of gravity acting on the ball
	Fgrav = baseball.m * vector(0, -g, 0) # in N

# Coefficient of Drag B = 1/2 * c * rho * A
	B = 0.0039 + (0.0058)/(1 + exp((mag(baseball.v) - 35)/5)) # in kg/m

# Part b) force of air resistance
	Fdrag = -B * mag(baseball.v)**2 * norm(baseball.v) # in N

# Net Force
	Fnet            = Fgrav #+ Fdrag # in N
# Initial Time
	t = 0 # in s
# Time step
	dt = 0.01 # in s
	while True:
		rate(100)
# When the ball goes below zero it stops
		if baseball.pos.y <= 0.000:
			position = []
			position.append(baseball.pos.x)
			print("--- Angle: {} degrees, Maximum Range: {} m ---".format(a, position[-1]))
			position[:] = []
			break
# Net Force
		Fnet = Fgrav  + Fdrag # in N
# Momentum update of ball
		baseball.p = baseball.p + Fnet * dt  # in kg m/s
# Velocity update of ball
		baseball.v = (baseball.p / baseball.m)  # in m/s
# Position Update of ball
		baseball.pos = baseball.pos + baseball.v * dt  # in m

		baseball.color  = color.green
# Plots the trajectory
		set.plot(pos=(baseball.pos.x, baseball.pos.y))
		t = t + dt
