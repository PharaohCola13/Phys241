# Spencer Riley
from __future__ import division, print_function
from visual import *
from visual.graph import *

M       = 2 #Mass [kg]
Lrod    = 1 # Length of the rod [m]
R       = 0.1 # Radius [m]
Laxle   = 4*R # length [m]
I       = (1/12)*M*Lrod**2 + (1/4)*M*R**2 #Moment of Inertia [kg*m^2]

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

L = vector(0,0,0) # angular momentum [kg*m^2]

deltat = 0.0001 #for accuracy in later parts
t = 0 #Initial time
theta = 0 #Initial Angle
dtheta = 0 #Change in angle

Fnet = vector(0.1,0,0)
aor = axle.axis
while t < 7:
	rate(10000)
# Apply Angular Momentum Principle
	torque = cross(axle.axis, Fnet) #in [Nm]
	L = L + torque * deltat #[kg*m^2/s]
# Update angle and rod position
	omega = L/I # Angular velocity [rads/s]
	omega_scalar = dot(omega, norm(aor))
	dtheta = omega_scalar * deltat #Updates the change in angle
	rod.rotate(angle=dtheta, axis=axle.axis, origin=axle.pos)

# Updates the time and angle
	t = t + deltat
	theta = theta + dtheta



