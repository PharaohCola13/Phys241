# Spencer Riley
from __future__ import division, print_function
from visual import *
from visual.graph import *

#Plots the angle with respect to time
gdx = gdisplay(x=0,y=600, width=1000, height=500, xtitle="Time [s]",
title='Theta vs Time', foreground=color.black, background=color.white)

plot_theta 	= gcurve(color=color.magenta)
plot_z		= gcurve(color=color.blue)

label(display=gdx.display, pos=(0, 4.5), text="Theta [rads]", color=color.magenta)
label(display=gdx.display, pos=(0, 1.5), text='Omega.z [rads/s]', color=color.blue)


theta = pi/6 #Initial Angle [rads]

can_of_meter        = cylinder()
can_of_meter.pos 	= vector(0,0,0)
can_of_meter.axis	= vector(cos(theta), -sin(theta), 0)
can_of_meter.radius = 0.1
can_of_meter.color	= color.yellow

axle        = cylinder()
axle.pos    = vector(0,0,0)
axle.radius = 0.01
axle.color  = color.red
axle.axis   = vector(0,0,0.01)

t  = 0	  	#Initial Time
dt = 0.001	#Change in time

dtheta = 0	#Change in angle

L   = vector(0,0,0) 	#Initial angular momentum [kg*m^2/s]
g   = 9.81		#Accerlation due to gravity [m/s^2]
r   = 1			#Radius [m]
m   = 0.5		#Mass [kg]
I   = (1./3.) * m * r**2 #Moment of Inertia [kg*m^2]

aor = axle.axis #Axis of Rotation

while t < 5:
	rate(1000)
	# Apply Angular Momentum Principle
	Fnet 	= vector(0,-m*g,0) 		 #Net force (gravity) [N]
	torque 	= cross(can_of_meter.axis, Fnet) #Torque [Nm]
	L 	= L + torque * dt		 #Update Angular Momentum [kg*m^2/s]
	# Update angle and rod position
	omega 		= L/I 			#Angular Velocity [rads/s]
	omega_scalar 	= dot(omega, norm(aor))
	dtheta 		= omega_scalar * dt	#Updates the change in angle
	can_of_meter.rotate(angle=dtheta, axis=axle.axis, origin=axle.pos)
# PLots the angle with repsect to time
	plot_theta.plot(pos=(t, theta))
#Plots the z-component of the angular velocity with respect to time
	plot_z.plot(pos=(t,omega.z))
# Updates the time and angle
	t = t + dt
	theta = theta + dtheta
