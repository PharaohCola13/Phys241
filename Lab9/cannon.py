# Spencer Riley
from __future__ import division, print_function
from visual import *
from visual.graph import *

# Creates the graphical display for the trajectory of each scenario
graph1 = gdisplay(title="Trajectories", x=0, y=400, width=800, height=400, xtitle="Positon in X [km]", ytitle="Position in Y [km]")
angle30 = gcurve(display= graph1, color=color.orange)
angle35 = gcurve(display= graph1, color=color.green)
angle40 = gcurve(display= graph1, color=color.blue)
angle45 = gcurve(display= graph1, color=color.magenta)
angle50 = gcurve(display= graph1, color=color.cyan)
angle55 = gcurve(display= graph1, color=color.red)

# Constants
g 	= 9.81 # in m/s^2
# List of angles
angles 	= [30, 35, 40, 45, 50, 55] # in degrees

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


for i in angles:
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
# Density of Air at sea level
	rho_0  = 1.225 #in kg/m^3
# Predefined variable
	y_0    = 1e4 # in m
# Absolute Temperature at sea level
	T_0    = 288.2 # in K
# Predefined variable
	alpha  = 2.5
# Predefined variable
	a      = 6.5e-3 # in K/m
# Density with altitude dependance
	rho    = rho_0 * (1 - ((a*cannon.pos.y)/T_0))**alpha
# Drag coefficient
	B = 4e-4 # in kg/m
# Drag coefficient with density dependence
	#B = B * (rho/rho_0) # in kg/m
# Force of drag
	Fdrag = -B * mag(cannon.v)**2 * norm(cannon.v) # in N
# Net force
	Fnet = Fgrav #+ Fdrag # in N
# Initial Time
	t = 0 # in s
# Time step
	dt = 0.1 # in s
	while True:
		rate(1000)
# Breaks loop when cannon hits floor
		if cannon.pos.y < 0.0:
			break
		if i == 30:
			cannon.color = color.orange
# Plots trajectory plot
			angle30.plot(pos=(cannon.pos.x/1000, cannon.pos.y/1000))
		elif i == 35:
			cannon.color = color.green
# Plots trajectory plot
			angle35.plot(pos=(cannon.pos.x/1000, cannon.pos.y/1000))
		elif i == 40:
			cannon.color = color.blue
# Plots trajectory plot
			angle40.plot(pos=(cannon.pos.x/1000, cannon.pos.y/1000))
		elif i == 45:
			cannon.color = color.magenta
# Plots trajectory plot
			angle45.plot(pos=(cannon.pos.x/1000, cannon.pos.y/1000))
		elif i == 50:
			cannon.color = color.cyan
# Plots trajectory plot
			angle50.plot(pos=(cannon.pos.x/1000, cannon.pos.y/1000))
		elif i == 55:
			cannon.color = color.red
# Plots trajectory plot
			angle55.plot(pos=(cannon.pos.x/1000, cannon.pos.y/1000))
# Updates momentum
		cannon.p = cannon.p + Fnet * dt # in kg m/s
# Updates velocity
		cannon.v = (cannon.p/cannon.m) # in m/s
# Updates position
		cannon.pos = cannon.pos + cannon.v * dt # in m
# Updates Time
		t = t + dt # in s

	t = t + dt
