# Spencer Riley
from __future__ import division, print_function
from visual import *
from visual.graph import *

# Creates the graphical display for Energy
graph1 = gdisplay(title="Wind Speed Trajectories", x=0, y=400, width=800, height=400, xtitle="Time [t]", ytitle="Position [m]")
windzero = gcurve(display= graph1, color=color.blue)
label(display=graph1.display, pos=(0,0),color=color.blue, text="0 mph")
windhead = gcurve(display= graph1, color=color.green)
label(display=graph1.display, pos=(0,2),color=color.green, text="10 mph")
windtail = gcurve(display= graph1, color=color.red)
label(display=graph1.display, pos=(0,-2),color=color.red, text="-10 mph")
g = 9.81
x_axis = arrow()
x_axis.pos = vector(0,0,0)
x_axis.axis = 50 *vector(1, 0, 0)
x_axis.color = color.red

y_axis = arrow()
y_axis.pos = vector(0,0,0)
y_axis.axis = 50 *vector(0, 1, 0)
y_axis.color = color.blue

z_axis = arrow()
z_axis.pos = vector(0,0,0)
z_axis.axis = 50 *vector(0, 0, 1)
z_axis.color = color.yellow


wind = [0, 4.4704, -4.4704]

for i in wind:
    baseball = sphere()
    baseball.radius = 1
    baseball.pos = vector(0, 1, 0)
    baseball.m = 0.150  # in kg
#    baseball.v = 50 * vector(cos(radians(45)), sin(radians(45)), cos(radians(90)))  # in m/s
    baseball.v = 110 * vector(cos(radians(35)), sin(radians(35)), cos(radians(90)))  # in m/s

    windv = vector(i, 0, 0)
    baseball.p = baseball.v * baseball.m
    Fgrav = baseball.m * vector(0, -g, 0)

    B = 0.0039 + (0.0058)/(1 + exp((mag(baseball.v) - 35)/5))
   # Fdrag = -B * mag(baseball.v)**2 * norm(baseball.v)

    Fdrag = -B * (mag(baseball.v) - mag(windv))**2 * (norm(baseball.v) - norm(windv))

    Fnet = Fgrav + Fdrag

    t = 0
    dt = 0.1
    while i == wind[0]:
        rate(10)

        if baseball.pos.y < 0.0:
            break

        baseball.p = baseball.p + Fnet * dt
        baseball.v = (baseball.p/baseball.m)
        baseball.pos = baseball.pos + baseball.v * dt

        # Plot Kinetic Energy as a function of the displacement
        windzero.plot(pos=(t,baseball.pos.y))

        t = t + dt
    while i == wind[1]:
        rate(10)

        if baseball.pos.y < 0.0:
            break

        baseball.p = baseball.p + Fnet * dt
        baseball.v = (baseball.p / baseball.m)
        baseball.pos = baseball.pos + baseball.v * dt

        # Plot Kinetic Energy as a function of the displacement
        windhead.plot(pos=(t, baseball.pos.y))

        t = t + dt
    while i == wind[2]:
        rate(10)

        if baseball.pos.y < 0.0:
            break

        baseball.p = baseball.p + Fnet * dt
        baseball.v = (baseball.p / baseball.m)
        baseball.pos = baseball.pos + baseball.v * dt

        # Plot Kinetic Energy as a function of the displacement
        windtail.plot(pos=(t, baseball.pos.y))

        t = t + dt