############################################################
# Physics 241 - Dr. Morales-Juberias                       #
#                                                          #
# Orbital motion ---                                       #
#    1. Circular and Elliptical Orbits                     #
#    2. Labels                                             #
#    3. Arrows for Momentum and Force                      #
#    4. Review of concept of center of mass                #
#                                                          # 
# September 24, 2018                                       #
############################################################

from __future__ import print_function,division
from visual import *
from visual.graph import *

#Example of motion under non-constant forces
#Gravity - Large scales
#Motion of the earth around the sun
##########################################################

scene = display(x=0,y=0,
                width=600,height=600,
                title='Earth around the Sun',
                background=color.white,
                foreground=color.black)

gd1 = gdisplay(x=650,y=0,
               width=600,height=600,
               title = 'periodic orbital motion',
               xtitle = 'time [Yrs]',ytitle='earth.pos.x [AU]',
                background=color.white,
                foreground=color.black)

#Declare constants

G    = 6.7e-11 #Nm2/kg2
YinS = 365.*24.*60.*60 #seconds in a year
AU2m = 1.5e11 #meters in an AU

#Create objects
sun   = sphere(pos=vector(0,0,0),radius=0.1, color=color.red,make_trail=True)
earth = sphere(pos=vector(1,0,0),radius=0.05,color=color.blue,make_trail=True)

sun.m   = 2e30 #kg
earth.m = 6e24 #kg

#Set up initial conditions

sun.v0   = vector(0,0,0) #Assumption <<<<<<< 

#earth.v0 = vector(0,2*pi*AU2m/YinS,0) #meters/second
earth.v0 = 0.5*vector(0,sqrt(G*sun.m/(mag(earth.pos)*AU2m)),0) #meters/second

#sun.v0 = -(earth.m/sun.m)*earth.v0

sun.p   = sun.m*sun.v0
earth.p = earth.m*earth.v0

##Pscale = 2.5e-30
##Fscale = 5e-24

#Arrowes to represewnt the force and momentum on the erth

##earthF = arrow(pos=earth.pos,axis=vector(0,0,0),color=color.cyan)
##earthP = arrow(pos=earth.pos,axis=Pscale*earth.p,color=color.orange)


#Add timestamp label
timestamp = label(pos=vector(0,0.5,0),color=color.red,text='Time in years: ')

#While loop somewhere in here
t  = 0
dt = YinS/1000

scene.mouse.getclick()

while t <= 5*YinS:
    rate(1000)

    timestamp.text ='Time in years: {:6.2f}'.format(t/YinS)


    r = (earth.pos-sun.pos)*AU2m
    r_mag = mag(r)
    r_hat = norm(r)
    Fmag = G*sun.m*earth.m/r_mag**2
    Fnet = -Fmag*r_hat

    #update our position
    #earth.pos = earth.pos + (earth.p/earth.m/AU2m) * dt
    #update our momentum
    earth.p = earth.p + Fnet * dt
    sun.p   = sun.p + (-Fnet) * dt
    #update our position
    earth.pos = earth.pos + (earth.p/earth.m/AU2m) * dt
    sun.pos   = sun.pos + (sun.p/sun.m/AU2m) * dt 
    #update my time
##    earthP.pos  = earth.pos
##    earthP.axis = Pscale*earth.p
##    earthF.pos  = earth.pos
##    earthF.axis = Fscale*Fnet
    
    t = t + dt
    
    







