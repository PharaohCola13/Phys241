# # Dirac Delta function approximations

import numpy as np
import matplotlib.pyplot as plt

#Vicki Kelsey
#Phys321
#5-31

w_0 = 2 * np.pi#global to each, so making a shortcut to help coding
#w_1 = np.sqrt((w_0)**2 - B**2)

def overdamp(t,B):#Beta > natural frequency
    global w_0
    m = np.sqrt(B**2 - w_0**2)#in rad/s, makes it easier to code x(t)
    n = np.sqrt(B**2 + w_0**2)#in rad/s, makes it easier to code x(t)
    over = ((B + m)/2*B)*np.exp(-(B - m)*t) + ((B - m)/2*B)*np.exp(-(B + n)*t)#in m
    #x(t) after c1 and c2 have been determined
    return over #passes along the function

def neutral(t,B):#Beta = natural frequency
    m = np.sqrt(B**2 - w_0**2)#in rad/s, makes it easier to code x(t)
    n = np.sqrt(B**2 + w_0**2)#in rad/s, makes it easier to code x(t)
    none = np.exp(-B*t) + B*t*np.exp(-B*t)#in m
    #x(t) after C1 determined to be 1 and C2 determined to be Beta
    return none #passes along function

def underdamp(t,B):#Beta < natural frequency
    i = np.sqrt(w_0**2 - B**2)#in rad/s, makes it easier to code x(t)
    j = np.sqrt(w_0**2 + B**2)#in rad/s, makes it easier to code x(t)
    d = np.arctan(B/i)#in radians
    under = ((w_0)/i)*np.exp(-B*t)*np.cos(i*t - d)#in m
    #x(t) after A and dirac delta function determined
    return under #passes along function

def plotoverdamp():#defining overdamp plot separate from others
    t = np.linspace(0,2,200)#interval
    t1 = overdamp(t,0)#at B=0
    t2 = overdamp(t,1)#at B=0
    t3 = overdamp(t,2)#at B=0
    t4 = overdamp(t,4)#at B=0
    t5 = overdamp(t,6)#at B=0
    t6 = overdamp(t,2*np.pi)#at B=0
    t7 = overdamp(t,10)#at B=0
    t8 = overdamp(t,20)#at B=0
    plt.plot(t, t1, t, t2, t, t3, t, t4, t, t5, t, t6, t, t7, t, t8)#plot functions
    plt.legend(("$beta=0$",#identify on plot
                '$beta=1$',#identify on plot
                '$beta=2$',#identify on plot
                '$beta=4$',#identify on plot
                '$beta=6$',#identify on plot
                '$beta=2pi$',#identify on plot
                '$beta=10$',#identify on plot
                '$beta=10$'))#identify on plot
    plt.xlabel('time in seconds');#labeling of horizontal axis
    plt.ylabel('x(t) in m')#labeling of vertical axis
    plt.title('Overdamped Harmonic Oscillator, V. Kelsey')#every plot needs a title
    plt.show()
plotoverdamp()

def plotneutral():#defining overdamp plot separate from others
    t = np.linspace(0,2,200)#interval
    t1 = neutral(t,0)#at B=0
    t2 = neutral(t,1)#at B=0
    t3 = neutral(t,2)#at B=0
    t4 = neutral(t,4)#at B=0
    t5 = neutral(t,6)#at B=0
    t6 = neutral(t,2*np.pi)#at B=0
    t7 = neutral(t,10)#at B=0
    t8 = neutral(t,20)#at B=0
    plt.plot(t, t1, t, t2, t, t3, t, t4, t, t5, t, t6, t, t7, t, t8)#plot functions
    plt.legend(("$beta=0$",#identify on plot
                '$beta=1$',#identify on plot
                '$beta=2$',#identify on plot
                '$beta=4$',#identify on plot
                '$beta=6$',#identify on plot
                '$beta=2pi$',#identify on plot
                '$beta=10$',#identify on plot
                '$beta=10$'))#identify on plot
    plt.xlabel('time in seconds');#labeling of horizontal axis
    plt.ylabel('x(t) in m')#labeling of vertical axis
    plt.title('Neutral Harmonic Oscillator, V. Kelsey')#every plot needs a title
    plt.show()
#plotneutral()

def plotunderdamp():#defining overdamp plot separate from others
    t = np.linspace(0,2,200)#interval
    t1 = underdamp(t,0)#at B=0
    t2 = underdamp(t,1)#at B=0
    t3 = underdamp(t,2)#at B=0
    t4 = underdamp(t,4)#at B=0
    t5 = underdamp(t,6)#at B=0
    t6 = underdamp(t,2*np.pi)#at B=0
    t7 = underdamp(t,10)#at B=0
    t8 = underdamp(t,20)#at B=0
    plt.plot(t, t1, t, t2, t, t3, t, t4, t, t5, t, t6, t, t7, t, t8)#plot functions
    plt.legend(("$beta=0$",#identify on plot
                '$beta=1$',#identify on plot
                '$beta=2$',#identify on plot
                '$beta=4$',#identify on plot
                '$beta=6$',#identify on plot
                '$beta=2pi$',#identify on plot
                '$beta=10$',#identify on plot
                '$beta=10$'))#identify on plot
    plt.xlabel('time in seconds');#labeling of horizontal axis
    plt.ylabel('x(t) in m')#labeling of vertical axis
    plt.title('Underdamped Harmonic Oscillator, V. Kelsey')#every plot needs a title
    plt.show()
plotunderdamp()
##    t1 = overdamp(t,0)#at B=0
##    t1 = overdamp(t,0)#at B=0
##    t1 = overdamp(t,0)#at B=0