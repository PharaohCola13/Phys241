#Spencer Riley
from __future__ import division, print_function
from visual import *
from visual.graph import *

# Plots the angle with respect to time
gdx = gdisplay(x=0,y=600, width=1000, height=500, xtitle="Time [s]", ytitle="Theta [rads]",
title='Theta vs Time', foreground=color.black, background=color.white)

plot_theta = gcurve(color=color.magenta)

# PLots the magnitude of the angular velocity with respect to time
gdx1 = gdisplay(x=0,y=600, width=1000, height=500, xtitle="Time [s]", ytitle="Mag(Omega) [s^-1]",
title='Mag(Omega) vs Time', foreground=color.black, background=color.white)

plot_omega = gcurve(color=color.green)

# Plots energy and torque with respect to time
gdx2 = gdisplay(x=0,y=600, width=1000, height=500, xtitle="Time [s]", foreground=color.black, background=color.white)

label(display=gdx2.display, pos=(0.5, 0.15), text="Rotational Kinetic Energy [J]", color=color.red)
label(display=gdx2.display, pos=(1.5, 0.05), text="Torque [Nm]", color=color.blue)

plot_energy = gcurve(color=color.red)
plot_torque = gcurve(color=color.blue)


M       = 2 #Mass [kg]
Lrod    = 1 #Length of the rod [m]
R       = 0.1 #Radius of the rod [m]
Laxle   = 4*R #Length [m]
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

L = vector(0,0,0) # angular momentum [kg*m^2/s]

deltat = 0.0001 #for accuracy in later parts
t = 0 #Initial Time
theta = 0 #Initial Angle
dtheta = 0 #Change in angle

#torque = vector(0, 0, 2)  # constant torque
aor = axle.axis #Axis of Rotation
while t < 2:
	rate(10000)
# Apply Angular Momentum Principle
	torque = vector(0, 0, 3 * cos(5 * t)) # [Nm]
	#torque = vector(0, 0, 2)
	L = L + torque * deltat #[kg*m^2/s]
# Update angle and rod position
	omega = L/I #Angular Velocity [rads/s]
	omega_scalar = dot(omega, norm(aor))
	dtheta = omega_scalar * deltat # Updates the change in angle
	rod.rotate(angle=dtheta, axis=axle.axis, origin=axle.pos)

# Rotational Kinetic energy
	energy_rot = 0.5 * I * mag(omega)**2

	plot_theta.plot(pos=(t, theta))
	plot_omega.plot(pos=(t,mag(omega)))
	plot_energy.plot(pos=(t, energy_rot))
	plot_torque.plot(pos=(t, mag(torque)))

# Updates Time and Angle
	t = t + deltat
	theta = theta + dtheta

print("The final angle is {:1.4f} rads".format(theta))
print("The Final magnitude of the angular speed is {:1.4f} rads/s".format(mag(omega)))
print("The ratio between the final angular speed and the final angle is {:1.4f}".format(mag(omega)/theta))