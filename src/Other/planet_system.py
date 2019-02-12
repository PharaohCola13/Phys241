from __future__ import division, print_function
from visual import *
from visual.graph import *
#from visual.materials import  *

scene = display()

g1 = gdisplay(x=1000, y=510, width=700, height=500)
g2 = gdisplay(x=550, y=510, width=700, height=500)
g3 = gdisplay(x=550, y=0, width=700, height=500)

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

star.v0          = vector(0,(-pi * AU)/YinS,0)
star.p           = star.m * star.v0

star2            = sphere(pps=10,trail_radius=1, make_trail = True)
star2.pos        = vector(0, 0, 1)
star2.radius     = 0.1
star2.m          = 0.5 * star.m
star2.color      = color.orange
star2.material  = materials.emissive

star2.v = vector(0, (pi * AU) / YinS, 0)
star2.p = star2.m * star2.v

star3            = sphere(pps=10,trail_radius=1, make_trail = True)
star3.pos        = vector(1, 0, 0)
star3.radius     = 0.1
star3.m          = 0.5 * star.m
star3.color      = color.red
star3.material  = materials.emissive

star3.v = vector(0,(-pi/2 * AU) / YinS , 0)
star3.p = star3.m * star3.v



t = 0
dt = YinS/100000
#dt = 1

f1 = gcurve(gdisplay = g1, color=star.color) # Define functions to plot
f2 = gcurve(gdisplay = g2, color=star2.color) # Define functions to plot
f3 = gcurve(gdisplay = g3, color=star3.color)

garrow1 = arrow()
garrow1.color = color.cyan

garrow2 = arrow()
garrow2.color = color.cyan

garrow3 = arrow()
garrow3.color = color.cyan



while True:
    rate(1e15)


    r1 = (star2.pos - star.pos) * AU
    r11 = (star.pos - star3.pos) * AU

    r2 = (star2.pos - star.pos) * AU
    r22 = (star2.pos - star3.pos) * AU

    r3 = (star3.pos - star.pos) * AU
    r33 = (star3.pos - star2.pos) * AU

    rmag1 = mag(r1)
    rhat1 = norm(r1)

    rmag2 = mag(r2)
    rhat2 = norm(r2)

    rmag3 = mag(r3)
    rhat3 = norm(r3)

    rmag11 = mag(r11)
    rhat11 = norm(r11)

    rmag22 = mag(r22)
    rhat22 = norm(r22)

    rmag33 = mag(r33)
    rhat33 = norm(r33)

    Fmag1 = (G * (star.m * star2.m) / rmag1**2) + (G * (star.m * star3.m)/ rmag11**2)
    Fmag2 = (G * (star2.m * star.m) / rmag2**2) + (G * (star2.m * star3.m)/rmag22**2)
    Fmag3 = (G * (star3.m * star.m) / rmag3**2) + (G * (star3.m * star2.m)/rmag33**2)

    Fnet1 = -Fmag1 * (rhat11 - rhat1)

    Fnet2 = -Fmag2 * (rhat22 - rhat2)

    Fnet3 = -Fmag3 * (rhat33 - rhat3)


    star3.p = star3.p + Fnet3 * dt
    star3.pos = star3.pos + (star3.p/star3.m/AU) * dt


    star2.p = star2.p + Fnet2 * dt
    star2.pos = star2.pos + (star2.p/star2.m/AU) * dt

    star.p = star.p + Fnet1 * dt
    star.pos = star.pos + (star.p/star.m/AU) * dt


    #star2.m = star2.m + 0.01*star.m
    f1.plot(pos=(t/YinS, star.pos.y))
    f2.plot(pos=(t/YinS, star2.pos.y))
    f3.plot(pos=(t/YinS, star3.pos.y))

    garrow1.pos = star.pos
    garrow1.axis = 5e-29 * Fnet1

    garrow2.pos = star2.pos
    garrow2.axis = 5e-29 * Fnet2

    garrow3.pos = star3.pos
    garrow3.axis = 5e-29 * Fnet3

    t= t + dt
