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

L0  = 0.1 #m
s0  = 0.12
k = 2e9

base                = box()
base.size           = vector(1, 0.01, 1)
base.pos            = vector(0,-0.1,0)
base.color          = color.green

ball                = sphere(make_trail=True)
ball.pos            = vector(s0, 0, 0)
ball.radius         = 0.025
ball.m              = 0.1
ball.v              = vector(-1, 0, 0)
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

t = 0
dt = 0.01

f1 = gcurve(gdisplay = gd1, color=color.white) # Define functions to plot

while t < 2000 * dt:
    try:
        rate(100)
        s           = mag(ball.pos) - L0
        Fspring     = -(k * s**7) * norm(ball.pos)
        Fnet        = Fspring

        ball.p      = ball.p + Fnet * dt
        ball.v      = (ball.p)/(ball.m)
        ball.pos    = ball.pos + ball.v * dt

        spring.axis = ball.pos - rod.pos
        f1.plot(pos=(t, ball.pos.x))
#        f1.plot(pos=(t, ball.v.x))  # Plots position vs time
 #       f1.plot(pos=(t, s), color=color.magenta)
        
        t = t + dt
        print(t)

    except OverflowError:
            print("Over Nope")
            break
    except RuntimeWarning:
            print("Running Nope")
            break
