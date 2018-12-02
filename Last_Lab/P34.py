# Spencer Riley
from __future__ import division, print_function
from visual import *
from visual.graph import *
import aux

# For the most part, this code was collected from the book

# Creates plotting environments
gdx = gdisplay(x=0,y=600, width=1000, height=500, xtitle="time [s]", ytitle="Momentum [kg m/s]",
title='X Component of Momentum')
Au_px = gcurve(color=color.yellow)
Alpha_px = gcurve(color=color.magenta)
sum_p_x         = gcurve(color=color.cyan)

label(display=gdx.display, pos=(1.17e-21, -1e-20), text="Au.p.x", color=color.yellow)
label(display=gdx.display, pos=(1.5e-21, -4e-20), text="Alpha.p.x", color=color.magenta)
label(display=gdx.display, pos=(2.49e-21, -7e-20), text="Au.p.x + Alpha.p.x", color=color.cyan)


gdy = gdisplay(x=500,y=600,width=1000, height=500, xtitle="time [s]", ytitle="Momentum [kg m/s]",
               title='Y Component of Momentum')
Au_py           = gcurve(color=color.yellow)
Alpha_py        = gcurve(color=color.red)
sum_p_y         = gcurve(color=color.green)

label(display=gdy.display, pos=(1.17e-21, -1e-20), text="Au.p.y", color=color.yellow)
label(display=gdy.display, pos=(1.5e-21, -2e-20), text="Alpha.p.y", color=color.red)
label(display=gdy.display, pos=(2.49e-21, -3e-20), text="Au.p.y + Alpha.p.y", color=color.green)

# Scene dimensions
scene.width = 1024
scene.height = 600

# Constants
q_e     = 1.6e-19
m_p     = 1.7e-27
oofpez  = 9e9
# Masses
m_Au    = (79+118) * m_p
m_Alpha = (2+2) * m_p
# Charges
qAu     = 79 * q_e
qAlpha  = 2 * q_e

# Creates the gold nucleus
Au          = sphere(make_trail=True)
Au.pos      = vector(0,0,0)
Au.radius   = 4e-15
Au.color    = color.yellow
Au.opacity  = 0.7
# Initial momentum of gold nucleus
Au.p    = m_Au*vector(0,0,0)

# Creates the alpha particle
Alpha           = sphere(make_trail=True)
Alpha.pos       = vector(-1e-13,5e-15,0)
Alpha.radius    = 1e-15
Alpha.color     = color.magenta
# Initial momentum of alpha particle
Alpha.p = vector(1.043e-19,0,0)

# Initial time
t       = 0
# Time step
dt      = 1e-23

# Impact Parameter for the model
b = Alpha.pos.y - Au.pos.y
print("The impact parameter is {} meters.".format(b))

while t <= 1.3e-20:
	rate(1000)
# Calculates displacement
	r       = Alpha.pos - Au.pos
	rmag    = mag(r)
	rhat    = norm(r)
# Calculates the electric force
	Felec = oofpez * (qAu * qAlpha)/rmag**2
	Fnet  = Felec * rhat
# Updates Momentum of Alpha particle
	Alpha.p   = Alpha.p + Fnet * dt
# Updates Position of the Alpha Particle
	Alpha.pos = Alpha.pos+(Alpha.p/m_Alpha) * dt
# Updates momentum of the gold nucleus
	Au.p      = Au.p - Fnet * dt
# Updates position of the gold nucleus
	Au.pos    = Au.pos + (Au.p/m_Au) * dt

# Plots the x components of momentum
	Au_px.plot(pos=(t, Au.p.x))
	Alpha_px.plot(pos=(t, Alpha.p.x))
	sum_p_x.plot(pos=(t, Au.p.x + Alpha.p.x))

# Plots the y components of momentum
	Au_py.plot(pos=(t, Au.p.y))
	Alpha_py.plot(pos=(t, Alpha.p.y))
	sum_p_y.plot(pos=(t, Au.p.y + Alpha.p.y))

# If contact is made between the alpha particle and gold nucleus, the transcript of Star Trek's First Contact
# will be printed and the loop will break
	if rmag - Alpha.radius <= Au.radius:
		aux.printer(aux.contact)
		aux.trek1.close()
		break
# Updates time
	t = t + dt
# Angle of scattering
theta = acos(dot(Alpha.p, Au.p) / (mag(Alpha.p) * mag(Au.p)))
print("The angle of scattering is {} rads or {} degrees".format(round(theta, 2), round(degrees(theta), 2)))

# Calculates the impact parameter of the angles in angles.
angles = [90, 169, 38, 13]
for theta in angles:
	impact = (oofpez * qAlpha * qAu)/(m_Alpha * mag(Alpha.p/m_Alpha)**2) * (sqrt((1 + cos(radians(theta)))/(1 - cos(radians(theta)))))
	print("The impact parameter for {} rads in {:1.2E} meters".format(round(radians(theta), 2), impact))

# At the end of the script, the transcript of Star Trek's Final Frontier will be printed.
print("This is the end of the program, Happy Holiday's. \n {}".format(aux.printer(aux.frontier)))
aux.trek2.close()
