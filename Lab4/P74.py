from __future__ import division, print_function
from visual import *
from visual.graph import *
#from visual.materials import  *

scene = display()

g1 = gdisplay(x=1000, y=510, width=700, height=500)
g2 = gdisplay(x=550, y=510, width=700, height=500)
g3 = gdisplay(x=0, y=1000, width=700, height=500)

G       = 6.7e-11 # Nm^2/kg^2
YinS    = 365.*24.*60.*60 # s
AU      = 1.5e11 # m

star             = sphere()
star.pos         = vector(0,0,0)
star.radius      = 0.1
star.m           = 2e30
star.color       = color.yellow
star.opacity     = 1
star.material    = materials.emissive

star.v          = vector(0,0,0)
star.p           = star.m * star.v

star2            = sphere(make_trail = True)
star2.pos        = vector(0, 0, 1)
star2.radius     = 0.1
star2.m          = 0.5 * star.m
star2.color      = color.orange
star2.material   = materials.emissive

star2.v          = vector(0, sqrt(G * star.m/(mag(star2.pos) * AU)), 0)
star2.p          = star2.m * star2.v

star3            = sphere(make_trail=True)
star3.pos        = vector(0, 0, -1)
star3.radius     = 0.1
star3.m          = 0.5 * star.m
star3.color      = color.red
star.material    = materials.emissive

star3.v          = vector(0, sqrt(G * star.m/(mag(star3.pos) * AU)), 0)
star3.p          = star3.m * star3.v

t = 0
dt = YinS/10000
#dt = 1

f1 = gcurve(gdisplay = g1, color=star.color) # Define functions to plot
f2 = gcurve(gdisplay = g2, color=star2.color) # Define functions to plot
f3 = gcurve(gdisplay = g3, color=star3.color)

while t < dt * 100000:
    rate(1e15)

    r = (star2.pos - star.pos)*AU
    rmag = mag(r)
    rhat = norm(r)

    r2 = (star3.pos - star.pos) * AU
    rmag2 = mag(r2)
    rhat2 = norm(r2)

    Fmag = G*(star.m * star2.m)/rmag**2
    Fnet = -Fmag * rhat

    Fmag2 = G * (star.m * star3.m)/rmag2**2
    Fnet2 = -Fmag2 * rhat2

    star3.p = star3.p + (Fnet2) * dt
    star3.pos = star3.pos + (star3.p/star3.m/AU) * dt

    star2.p = star2.p + Fnet * dt
    star2.pos = star2.pos + (star2.p/star2.m/AU) * dt

    star.p = star.p + (-Fnet) * dt
    star.pos = star.pos + (star.p/star.m/AU) * dt

    f1.plot(pos=(t/YinS, star.pos.y))
    f2.plot(pos=(t/YinS, star2.pos.y))
    f3.plot(pos=(t/YinS, star3.pos.y))
    t= t + dt
