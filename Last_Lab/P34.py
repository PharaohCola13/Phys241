from __future__ import division, print_function
from visual import *
from visual.graph import *
scene.width = 1024
scene.height = 600
q_e = 1.6e-19
m_p = 1.7e-27
oofpez = 9e9
m_Au = (79+118) * m_p
m_Alpha = (2+2) * m_p
qAu = 79 * q_e
qAlpha = 2 * q_e
deltat = 1e-23

Au = sphere(pos=vector(0,0,0), radius=4e-15,
color=color.yellow, make_trail=True)

Alpha = sphere(pos=vector(-1e-13,5e-15,0),
radius=1e-15, color=color.magenta,
make_trail=True)

p_Au = m_Au*vector(0,0,0)
p_Alpha = vector(1.043e-19,0,0)

t = 0
while t<1.3e-20:
    rate(100)
    Alpha.pos = Alpha.pos+(p_Alpha/m_Alpha) * deltat
    t = t + deltat