from __future__ import division, print_function
from visual import *

#Declaration of constants

G    = 6.67e-11 #N*m2/Kg2
Yins = 1.*365.*24.*60.*60. #1 year in seconds

AU2m = 1.5e11 #1 AU in meters

#Create the objects in our program
sun   = sphere()
sun.pos=vector(0,0,0)
sun.radius=   0.1
sun.color=color.yellow

earth = sphere(make_trail=True)
earth.pos=vector(1,0,0)
earth.radius= 0.025
earth.color=color.blue
#For graphical purposes we can leave the distances in AU

#Define the masses of our objects
sun.m   = 2e30 #Kg
earth.m = 6e24 #Kg

#We assume the sun is initially not moving
sun.v0   = vector(0,0,0)
#For the earth we know it takes one year to go around one orbit
Period  = 1.*Yins #1 year in seconds
CircOrb = 2*pi*AU2m
earth.v0 = vector(0,CircOrb/Period,0)

#Create the momentum vectors
sun.p   =     sun.m*sun.v0
earth.p = earth.m*earth.v0

t  = 0
dt = Period/1000

while t <= 5*Period:
    rate(1000)

    r = (earth.pos - sun.pos)*AU2m
    rmag = mag(r)
    rhat = norm(r)

    Fmag = G*earth.m*sun.m/rmag**2
    Fnet   = -Fmag * rhat

    earth.p = earth.p + Fnet * dt
    earth.pos = earth.pos + (earth.p/earth.m/AU2m) * dt

    #Update the time
    t = t + dt
