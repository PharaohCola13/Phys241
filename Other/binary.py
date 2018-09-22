from __future__ import division, print_function
from visual import *
from visual.graph import *
#from visual.materials import  *

scene = display()

g1 = gdisplay(x=1000, y=510, width=700, height=500)
g2 = gdisplay(x=550, y=510, width=700, height=500)

G       = 6.7e-11 # Nm^2/kg^2
YinS    = 365.*24.*60.*60 # s
AU      = 1.5e11 # m

# # X-axis
# x_axis          = arrow()
# x_axis.pos      = vector(0,0,0)
# x_axis.axis     = 1 * vector(1, 0, 0)
# x_axis.color    = color.red
#
# # Y-axis
# y_axis          = arrow()
# y_axis.pos      = vector(0,0,0)
# y_axis.axis     = 1 * vector(0, 1, 0)
# y_axis.color    = color.blue
#
# # Z-axis
# z_axis          = arrow()
# z_axis.pos      = vector(0,0,0)
# z_axis.axis     = 1  * vector(0, 0, 1)
# z_axis.color    = color.green

star             = sphere()
star.pos         = vector(0,0,0)
star.radius      = 0.1
star.m           = 2e30
star.color       = color.yellow
star.opacity     = 1
star.material    = materials.emissive

star.v0          = vector(0,(-pi/2 * AU)/YinS,0)
star.p           = star.m * star.v0

star2            = sphere(pps=10,trail_radius=1, make_trail = True)
star2.pos        = vector(0, 0, 1)
star2.radius     = 0.1
star2.m          = 0.5 * star.m
star2.color      = color.orange
star2.material  = materials.emissive

star2.v = vector(0, (pi * AU) / YinS, 0)
star2.p = star2.m * star2.v


t = 0
dt = YinS/10000
#dt = 1

f1 = gcurve(gdisplay = g1, color=star.color) # Define functions to plot
f2 = gcurve(gdisplay = g2, color=star2.color) # Define functions to plot

while True:
    rate(1e15)
    r = (star2.pos - star.pos)*AU
    rmag = mag(r)
    rhat = norm(r)
    Fmag = G*(star.m * star2.m)/rmag**2
    Fnet = -Fmag * rhat

    rsun = (star.pos - star2.pos) * AU
    rsun_mag = mag(rsun)
    rsun_hat = norm(rsun)
    Fsun = G * (star.m * star2.m) / rsun_mag**2
    Fsun_net = -Fsun * rsun_hat

    star2.p = star2.p + Fnet * dt
    star2.pos = star2.pos + (star2.p/star2.m/AU) * dt

    star.p = star.p + Fsun_net * dt
    star.pos = star.pos + (star.p/star.m/AU) * dt

    f1.plot(pos=(t/YinS, star.pos.y))
    f2.plot(pos=(t/YinS, star2.pos.y))

    t= t + dt
