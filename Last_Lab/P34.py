from __future__ import division, print_function
from visual import *
from visual.graph import *
#import aux


gdx = gdisplay(x=0,y=600, width=1000, height=500,
title='X Component of Momentum')
Au_px = gcurve(color=color.yellow)
Alpha_px = gcurve(color=color.magenta)
sum_p_x         = gcurve(color=color.cyan)
## other gcurves if needed
gdy = gdisplay(x=500,y=600,width=1000, height=500, title='Y Component of Momentum')
Au_py           = gcurve(color=color.yellow)
Alpha_py        = gcurve(color=color.red)
sum_p_y         = gcurve(color=color.green)

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

# Impact Parameter
b = Alpha.pos.y - Au.pos.y
print("The impact parameter is {} meters.".format(b))

while t <= 1.3e-20:
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

	Au_px.plot(pos=(t, Au.p.x))
	Alpha_px.plot(pos=(t, Alpha.p.x))
	sum_p_x.plot(pos=(t, Au.p.x + Alpha.p.x))
	label(display=gdx.display, pos=(1.17e-21, -1e-20), text="Au.p.x", color=color.yellow)
	label(display=gdx.display, pos=(1.5e-21, -4e-20), text="Alpha.p.x", color=color.magenta)
	label(display=gdx.display, pos=(2.49e-21, -7e-20), text="Au.p.x + Alpha.p.x", color=color.cyan)

	Au_py.plot(pos=(t, Au.p.y))
	Alpha_py.plot(pos=(t, Alpha.p.y))
	sum_p_y.plot(pos=(t, Au.p.y + Alpha.p.y))
	label(display=gdy.display, pos=(1.17e-21, -1e-20), text="Au.p.y", color=color.yellow)
	label(display=gdy.display, pos=(1.5e-21, -2e-20), text="Alpha.p.y", color=color.red)
	label(display=gdy.display, pos=(2.49e-21, -3e-20), text="Au.p.y + Alpha.p.y", color=color.green)

	if rmag - Alpha.radius <= Au.radius:
		aux.printer(aux.contact)
		aux.trek1.close()
		break

	t = t + dt
print()
theta = acos(dot(Alpha.p, Au.p) / (mag(Alpha.p) * mag(Au.p)))
print("The angle of scattering is {} rads or {} degrees".format(round(theta, 2), round(degrees(theta), 2)))
angles = [90, 169, 38, 13]
for theta in angles:
	impact = (oofpez * qAlpha * qAu)/(m_Alpha * mag(Alpha.p/m_Alpha)**2) * (sqrt((1 + cos(radians(theta)))/(1 - cos(radians(theta)))))
	print("The impact parameter for {} rads in {:1.2E} meters".format(round(radians(theta), 2), impact))
print("This is the end of the program. \n {}".format(aux.printer(aux.frontier)))
aux.trek2.close()

# 35
# Is momentum conserved? Yes, this can be seen by the plots that the sum of both the x and y component of momentum do not change of the time interval.
# What should be changed if not?
#If the momentum doesn't appear to be conserved than there may be a miscalculation associated with the Electric force that is propagated to the momentum calculation.
