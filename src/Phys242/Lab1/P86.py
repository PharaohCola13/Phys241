from __future__ import division, print_function
from visual import *
from visual.graph import *

gdx = gdisplay(x=0,y=600, width=1000, height=500, xtitle="Time [s]", ytitle="Theta (rads)",
title='Theta vs Time')

plot_theta = gcurve(color=color.magenta)

gdx1 = gdisplay(x=0,y=600, width=1000, height=500, xtitle="Mag(Omega) [s^-1]", ytitle="Theta (rads)",
title='Theta vs Mag(Omega)')

plot_omega = gcurve(color=color.cyan)


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

#torque = vector(0, 0, 2)  # constant torque
aor = axle.axis
while t < 2:
	rate(10000)
# Apply Angular Momentum Principle
	torque = vector(0, 0, 3 * cos(5 * t))
	L = L + torque * deltat
# Update angle and rod position
	omega = L/I
	omega_scalar = dot(omega, norm(aor))
	dtheta = omega_scalar * deltat
	rod.rotate(angle=dtheta, axis=axle.axis, origin=axle.pos)

	plot_theta.plot(pos=(t, theta))
	plot_omega.plot(pos=(mag(omega), theta))

	t = t + deltat
	theta = theta + dtheta

print(theta)
print(mag(omega))

print(mag(omega)/theta)


# Part C, No it is not consistent. This is because the torque is changing as time progresses.



