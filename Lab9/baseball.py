# Spencer Riley
from __future__ import division, print_function
from visual import *
from visual.graph import *

# Creates the graphical display for Energy
graph1 = gdisplay(title="Spring Energies", x=0, y=400, width=800, height=400, xtitle="Time [t]", ytitle="Energy [J]")
windzero = gcurve(display= graph1, color=color.blue)
windhead = gcurve(display= graph1, color=color.green)
windtail = gcurve(display= graph1, color=color.red)

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
    cannon = sphere()
    cannon.radius = 1
    cannon.pos = vector(0, 1, 0)
    cannon.m = 0.150  # in kg
    cannon.v = 50 * vector(cos(radians(45)), sin(radians(45)), cos(radians(90)))  # in m/s

    windv = vector(i, 0, 0)
    cannon.p = cannon.v * cannon.m
    Fgrav = cannon.m * vector(0, -g, 0)

    B = 0.0039 + (0.0058)/(1 + exp((mag(cannon.v) - 35)/5))
   # Fdrag = -B * mag(cannon.v)**2 * norm(cannon.v)

    Fdrag = -B * (mag(cannon.v) - mag(windv))**2 * (norm(cannon.v) - norm(windv))

    Fnet = Fgrav + Fdrag

    t = 0
    dt = 0.1
    while i == wind[0]:
        rate(10)

        if cannon.pos.y < 0.0:
            break

        cannon.p = cannon.p + Fnet * dt
        cannon.v = (cannon.p/cannon.m)
        cannon.pos = cannon.pos + cannon.v * dt

        # Plot Kinetic Energy as a function of the displacement
        windzero.plot(pos=(t,cannon.pos.x))

        t = t + dt
    while i == wind[1]:
        rate(10)

        if cannon.pos.y < 0.0:
            break

        cannon.p = cannon.p + Fnet * dt
        cannon.v = (cannon.p / cannon.m)
        cannon.pos = cannon.pos + cannon.v * dt

        # Plot Kinetic Energy as a function of the displacement
        windhead.plot(pos=(t, cannon.pos.x))

        t = t + dt
    while i == wind[2]:
        rate(10)

        if cannon.pos.y < 0.0:
            break

        cannon.p = cannon.p + Fnet * dt
        cannon.v = (cannon.p / cannon.m)
        cannon.pos = cannon.pos + cannon.v * dt

        # Plot Kinetic Energy as a function of the displacement
        windtail.plot(pos=(t, cannon.pos.x))

        t = t + dt