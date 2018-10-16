from __future__ import division, print_function
from visual import *
from visual.graph import *
import warnings
warnings.simplefilter("error", RuntimeWarning)
from visual.graph import *

# Creates the graphical display for position
gd1 = gdisplay(x=550,y=0,width=700,height=500,
        title='Not a graph of ball motion',
        xtitle='Time [s]',
        ytitle='Position [m]')
# Relaxed Length
L0  = 0.1 # in m
# Intial Length
s0  = 0.12 # in m
# Spring Constant 
k = 2e9 # in Nm

base                = box()
base.size           = vector(1, 0.01, 1)
base.pos            = vector(0,-0.1,0)
base.color          = color.green

ball                = sphere(make_trail=True)
ball.pos            = vector(s0, 0, 0)
ball.radius         = 0.025
ball.m              = 0.1 # in kg
ball.v              = vector(-1, 0, 0) # in m/s
ball.p              = ball.m * ball.v
ball.color          = color.cyan

rod                 = cylinder()
rod.pos             = vector(0,0,0)
rod.axis            = vector(0, -0.1, 0)
rod.radius          = 0.01

spring              = helix()
spring.pos          = vector(0,0,0)
spring.axis         = ball.pos + vector(0, 0, 0)
spring.thickness    = 0.003
spring.radius       = 0.01
spring.coils        = 10
spring.color        = color.orange

# Initial Time
t = 0
# Time Step
dt = 0.01

f1 = gcurve(gdisplay = gd1, color=color.white) # Define functions to plot

while t < 2000 * dt:
    try:
        rate(100)
# Spring Force
        s           = mag(ball.pos) - L0
        Fspring     = -(k * s**7) * norm(ball.pos)
        Fnet        = Fspring
# Updates Ball Momentum
        ball.p      = ball.p + Fnet * dt
# Updates Ball Velocity
        ball.v      = (ball.p)/(ball.m)
# Updates Ball Position
        ball.pos    = ball.pos + ball.v * dt

        spring.axis = ball.pos - rod.pos
# Plots Ball Position as a function of time
        f1.plot(pos=(t, ball.pos.x))
# Plots Ball Velocity as a function of time
#        f1.plot(pos=(t, ball.v.x))  # Plots position vs time
# Plots Strench as a function of time
 #       f1.plot(pos=(t, s), color=color.magenta)
# Updates Time
        t = t + dt
        print(t)
# Python did no-no stuff, these stopped the script from running the bad errors came.
    except OverflowError:
            print("Over Nope")
            break
    except RuntimeWarning:
            print("Running Nope")
            break
