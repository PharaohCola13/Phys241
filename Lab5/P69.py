from __future__ import division, print_function
from visual import *
from visual.graph import *

# Creates the graphical display for position
gd1 = gdisplay(x=550,y=0,width=700,height=500,
               title='Position of block',
               xtitle='Time [s]',
               ytitle='Position [m]')


k   = 8 # in N/m
# k = 16
L0  = 0.20 # in m
g   = 9.81

base                = box()
base.size           = vector(0.2, 0.01, 0.2)
base.pos            = vector(0,0,0)
base.color          = color.green

block               = box()
block.pos           = vector(0, 0.1, 0)
block.size          = (0.1, 0.1, 0.1)
block.m             = 0.06
#block.m             = 0.12
block.p             = block.m * vector(0,0,0)
block.color         = color.orange

spring              = helix()
spring.pos          = base.pos
spring.axis         = block.pos - base.pos
spring.thickness    = 0.003
spring.radius       = 0.05
spring.coils        = 40

fgrav = block.m * g * vector(0,-1,0)

t   = 0
dt  = 0.001

f1 = gcurve(gdisplay = gd1, color=color.white) # Define functions to plot


while t < 600*dt:
    rate(100)

    s           = mag(block.pos) - L0
    Fspring     = -k * s * norm(block.pos)
    Fnet        = -fgrav + Fspring

    block.p     = block.p + Fnet*dt
    block.pos   = block.pos + block.p/block.m * dt

    spring.axis = block.pos - base.pos
    f1.plot(pos=(t, block.pos.y))  # Plots position vs time

    t = t + dt