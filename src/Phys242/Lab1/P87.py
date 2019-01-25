from __future__ import division, print_function
from visual import *
from visual.graph import *

M       = 2
Lrod    = 1
R       = 0.1
Laxle   = 4*R
I       = (1/12)*M*Lrod**2 + (1/4)*M*R**2

rod         = cylinder()
rod.pos     = vector(-1,0,0)
rod.radius  = R
rod.color   = color.orange
rod.axis    = vector(Lrod,0,0)

axle        = cylinder()
axle.pos    = vector(-1+Lrod/2,0,-Laxle/2)
axle.radius = R/6
axle.color  = color.red
axle.axis   = vector(0,0,4*R)

L = vector(0,0,0) # angular momentum

deltat = 0.0001
# for accuracy in later parts
t = 0
theta = 0
dtheta = 0

Fnet = (0.1, 0, 0)
aor = axle.axis
while t < 7:
	rate(10000)
# Apply Angular Momentum Principle
	torque = cross(axle.axis, Fnet)
	print(torque)
	L = L + torque * deltat
# Update angle and rod position
	omega = L/I
	omega_scalar = dot(omega, norm(aor))
	dtheta = omega_scalar * deltat
	rod.rotate(angle=dtheta, axis=axle.axis, origin=axle.pos)

	t = t + deltat
	theta = theta + dtheta

print(theta)
print(mag(omega))

print(mag(omega)/theta)



