from __future__ import division, print_function
from visual import *
from visual.graph import *
from random import *

#theta           = radians(15)
# X-axis
x_axis          = arrow()
x_axis.pos      = vector(0,0,0)
x_axis.axis     = 100 * vector(1, 0, 0)
x_axis.color    = color.red

# Y-axis
y_axis          = arrow()
y_axis.pos      = vector(0,0,0)
y_axis.axis     = 100 * vector(0, 1, 0)
y_axis.color    = color.blue

# Z-axis
z_axis          = arrow()
z_axis.pos      = vector(0,0,0)
z_axis.axis     = 100 * vector(0, 0, 1)
z_axis.color    = color.green


rand_color = vector(randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255)

# Tennis Ball
tennis_ball         = sphere(make_trail=True)
tennis_ball.pos     = (0, 0, 0) # Initial position
tennis_ball.m       = 0.055 # Mass of tennis ball in kg
tennis_ball.v       = vector((31.75)*cos(pi/3), (31.75)*sin(pi/3), 0) # Velocity with magnitude of 55 m/s
tennis_ball.radius  = 5 # in meters
tennis_ball.p       = tennis_ball.m * tennis_ball.v # momentum
tennis_ball.color   = rand_color
mag(tennis_ball.v) # magnitude of velocity

t = 0 # Initial time
dt = 0.1 # Time step

while t < 100 * dt:
    rate(50)
    F_grav          = tennis_ball.m * vector(0, -9.81, 0) # Force of gravity in Newtons
    tennis_ball.p   = tennis_ball.p + F_grav * dt # Update tennis ball's momentum
    tennis_ball.pos = tennis_ball.pos + (tennis_ball.p/tennis_ball.m) * dt # Update tennis ball's position

    if tennis_ball.pos.y < 0: # Break the loop if the y position of the tennis ball is negative
        break

    t = t + dt # Update time