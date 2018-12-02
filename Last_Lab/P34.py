from __future__ import division, print_function
from visual import *
from visual.graph import *


gdx = gdisplay(x=0,y=600, width=500,
title='p_x')
p_Au_x_graph = gcurve(color=color.yellow)
p_Alpha_x_graph = gcurve(color=color.magenta)
## other gcurves if needed
gdy = gdisplay(x=500,y=600,width=500,title='p_y')
p_Au_y_graph = gcurve(color=color.yellow)
## other gcurves if needed

scene.width = 1024
scene.height = 600

q_e     = 1.6e-19
m_p     = 1.7e-27

oofpez  = 9e9

m_Au    = (79+118) * m_p
m_Alpha = (2+2) * m_p

qAu     = 79 * q_e
qAlpha  = 2 * q_e

Au          = sphere(make_trail=True)
Au.pos      = vector(0,0,0)
Au.radius   = 4e-15
Au.color    = color.yellow
Au.opacity  = 0.7

Alpha           = sphere(make_trail=True)
Alpha.pos       = vector(-1e-13,5e-15,0)
Alpha.radius    = 1e-15
Alpha.color     = color.magenta

Au.p    = m_Au*vector(0,0,0)
Alpha.p = vector(1.043e-19,0,0)

dt      = 1e-23
t       = 0

while t < 1.3e-20:
    rate(100)

    r       = Alpha.pos - Au.pos
    rmag    = mag(r)
    rhat    = norm(r)

    Felec = oofpez * (qAu * qAlpha)/rmag**2
    Fnet  = Felec * rhat

    Alpha.p   = Alpha.p + Fnet * dt
    Alpha.pos = Alpha.pos+(Alpha.p/m_Alpha) * dt

    Au.p      = Au.p - Fnet * dt
    Au.pos    = Au.pos + (Au.p/m_Au) * dt

    b = (oofpez*(qAu * qAlpha))/(0.5 * m_Alpha * mag(Alpha.p/m_Alpha)**2)
    print(b)
    p_Au_x_graph.plot(pos=(t, Au.p.x))
    p_Alpha_x_graph.plot(pos=(t, Alpha.p.x))

    p_Au_y_graph.plot(pos=(t, Au.p.y))
    #print(Au.pos)
    if rmag - Alpha.radius <= Au.radius:
        print("Collision")
        break

    t = t + dt

# Part a) The code will shoot a alpha particle at a gold nucleus.
# Part b)
# Part c) Yes, the gold atom moves. Yes it should move, this is because there is a mutal force being applied on both particles.
# Part d)