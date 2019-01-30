from __future__ import division, print_function
from visual import *
from visual.graph import *

can_of_meter        = cylinder()
can_of_meter.pos 	= vector(0,0,0)
can_of_meter.axis	= vector(0, -1, 0)
can_of_meter.radius = 0.1
can_of_meter.color	= color.yellow

axle        = cylinder()
axle.pos    = vector(0,0,0)
axle.radius = 0.01
axle.color  = color.red
axle.axis   = vector(0,0,0.01)

t = 0
dt = 0.001

theta = 0
dtheta = 0

I 	= 1
L   = vector(0,0,0)
g   = 9.81
r   = mag(can_of_meter.axis)
m   = 1

aor = axle.pos

while t < 10:
	rate(100)
	# Apply Angular Momentum Principle
	Fnet = vector(0,-m*g,0)
	torque = cross(can_of_meter.pos, Fnet)
	L = L + torque * dt
	# Update angle and rod position
	omega = sqrt((m*g*r)/I)
	dtheta = omega * dt

	can_of_meter.axis = 1
#	can_of_meter.rotate(angle=dtheta, axis=axle.axis, origin=axle.pos)

	t = t + dt
	theta = theta + dtheta
