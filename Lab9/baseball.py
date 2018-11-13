# Spencer Riley
from __future__ import division, print_function
from visual import *
from visual.graph import *
from numpy import *

# Creates the graphical display for the trajectory of each scenario
graph1      = gdisplay(title="Wind Speed Trajectories", x=0, y=400, width=800, height=400, xtitle="Position in X [m]", ytitle="Position in Y [m]")
windzero    = gcurve(display= graph1, color=color.cyan)
label(display=graph1.display, pos=(-75,5),color=color.cyan, text="0 mph")
windhead    = gcurve(display= graph1, color=color.green)
label(display=graph1.display, pos=(-75,7.5),color=color.green, text="10 mph")
windtail    = gcurve(display= graph1, color=color.red)
label(display=graph1.display, pos=(-75,2.5),color=color.red, text="-10 mph")

# Constant
g       = 9.81 # in m/s^2
wind    = [0, 4.4704, -4.4704] # in m/s
angles  = linspace(10, 60, 5)

lots_of_angles = angles.tolist()

# Creates a X axis
x_axis          = arrow()
x_axis.pos      = vector(0,0,0)
x_axis.axis     = 50 *vector(1, 0, 0)
x_axis.color    = color.red

# Creates a Y axis
y_axis          = arrow()
y_axis.pos      = vector(0,0,0)
y_axis.axis     = 50 *vector(0, 1, 0)
y_axis.color    = color.blue

# Creates a Z axis
z_axis          = arrow()
z_axis.pos      = vector(0,0,0)
z_axis.axis     = 50 *vector(0, 0, 1)
z_axis.color    = color.yellow

for i in wind:
# Creates a ball of defined mass
    baseball        = sphere(make_trail=True)
    baseball.radius = 1
    baseball.pos    = vector(0, 1, 0)
# Mass of ball
    baseball.m      = 0.150  # in kg
# Part a) initial velocity had a magnitude of 50 m/s
    baseball.v = 50 * vector(cos(radians(45)), sin(radians(45)), cos(radians(90)))  # in m/s

# Part c) initial velocity had a magnitude of 49.1744 m/s or 110 mph
#    baseball.v = 49.1744 * vector(cos(radians(35)), sin(radians(35)), cos(radians(90)))  # in m/s
    
# Wind velocity in vector form
    windv = vector(i, 0, 0) # in m/s
    
# The force of gravity acting on the ball
    Fgrav = baseball.m * vector(0, -g, 0) # in N
    
# Coefficient of Drag B = 1/2 * c * rho * A
    B = 0.0039 + (0.0058)/(1 + exp((mag(baseball.v) - 35)/5)) # in kg/m
    
# Part b) force of air resistance
   # Fdrag = -B * mag(baseball.v)**2 * norm(baseball.v) # in N
    
# Part c) force of Drag with respect to the wind
   # Fdrag = -B * (mag(baseball.v) - mag(windv))**2 * (norm(baseball.v) - norm(windv)) # in N
    
# Net Force
    Fnet            = Fgrav #+ Fdrag # in N
    # Momentum update of ball
    baseball.p      = baseball.p + Fnet * dt # in kg m/s
# Velocity update of ball
    baseball.v      = (baseball.p/baseball.m) # in m/s
# Position Update of ball
    baseball.pos    = baseball.pos + baseball.v * dt # in m

# Initial Time
    t = 0 # in s
# Time step
    dt = 0.1 # in s
    while i == wind[0]:
        rate(10)
# When the ball goes below zero it stops
        if baseball.pos.y < 0.0:
            break
        baseball.color  = color.cyan
# Plots the trajectory
        windzero.plot(pos=(baseball.pos.x,baseball.pos.y))
# Updates Time
        t = t + dt # in s
    while i == wind[1]:
        rate(10)
# When the ball goes below zero it stops
        if baseball.pos.y < 0.0:
            break
        baseball.color  = color.green
# Plots the trajectory
        windhead.plot(pos=(baseball.pos.x, baseball.pos.y))
# Updates Time
        t = t + dt # in s
    while i == wind[2]:
        rate(10)
# When the ball goes below zero it stops
        if baseball.pos.y < 0.0:
            break
        baseball.color  = color.red
# Plots the trajectory
        windtail.plot(pos=(baseball.pos.x, baseball.pos.y))
# Updates Time
        t = t + dt # in s

for i in lots_of_angles:
    # Creates a ball of defined mass
    baseball        = sphere(make_trail=True)
    baseball.radius = 1
    baseball.pos    = vector(0, 1, 0)
# Mass of ball
    baseball.m      = 0.150  # in kg
# Part a) initial velocity had a magnitude of 50 m/s
    baseball.v = 50 * vector(cos(radians(i)), sin(radians(i)), cos(radians(90)))  # in m/s

# The force of gravity acting on the ball
    Fgrav = baseball.m * vector(0, -g, 0) # in N
    
# Coefficient of Drag B = 1/2 * c * rho * A
    B = 0.0039 + (0.0058)/(1 + exp((mag(baseball.v) - 35)/5)) # in kg/m
    
# Part b) force of air resistance
    Fdrag = -B * mag(baseball.v)**2 * norm(baseball.v) # in N
    
# Net Force
    Fnet            = Fgrav #+ Fdrag # in N
    # Momentum update of ball
    baseball.p      = baseball.p + Fnet * dt # in kg m/s
# Velocity update of ball
    baseball.v      = (baseball.p/baseball.m) # in m/s
# Position Update of ball
    baseball.pos    = baseball.pos + baseball.v * dt # in m

# Initial Time
    t = 0 # in s
# Time step
    dt = 0.1 # in s
    while True:
        rate(100)
        print("--- {} radians ---".format(radians(i)))
        # When the ball goes below zero it stops
        if baseball.pos.y < 0.0:
            break
        baseball.color  = color.green
# Plots the trajectory
        windhead.plot(pos=(baseball.pos.x, baseball.pos.y))
