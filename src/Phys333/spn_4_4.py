####
### Title: 	SPN-4-4
### Author: Spencer Riley
### Python Version: 2.7.13
####
import matplotlib.pyplot as plt
from numpy import *

idstr = 'By R. Sonnenfeld, New Mexico Tech Physics (Sept. 2017) -- Free for educational use only.'
suptitle = 'Griffith''s Figure 3.19'
## Oh look, it's me.
title = 'by: Spencer Riley'

# Some kind-of neat constants
a = 1.0
V0 = 1

def super_dope_plotting_function_with_a_really_really_long_name():
    print("SPN4-4, 2019 | " + title)
    print("====== ======= =========")
    x, dx = linspace(0, a, 1001, retstep=True)
# Initializations
    wave = 0
    fig = plt.figure()
## Since the instances of n is even will not be computed since the iteration is over odd
## integers as seen in Eq. 3.36 I made some changes.
    special_ns = [1, 5, 11, 101]  # These are the 4 special n's that Griffiths plots
    label_ns = [1, 5, 10, 100] # These are the labels for the 4 special n's
## The for loop ony iterates over odd integers
    for n in range(1, 102, 2):
## The equation for the nth term is based on Eq. 3.36. The exponential term has been omitted
## due to the infinite sum of e^-1 is equal to one. (This results in a screwed up plot).
        nth_term = ((4 * V0)/(pi*n)) * sin((n*pi*x)/a) # nth term in the sum
        wave = wave + nth_term # Neat sum
# plotting filter
        if n in special_ns:
            if n in label_ns:
                plt.plot(x, wave, label='Sum of ' + str(n) + ' terms')
            else:
                plt.plot(x, wave, label='Sum of ' + str(n-1) + ' terms')
# Plot stuff
    plt.xlabel('$y/a$', fontsize=16)
    plt.ylabel('$V/V_0$', fontsize=16)
    plt.suptitle(suptitle, fontsize=16)
    plt.title(title, fontsize=12)
    plt.legend(loc='best')
   # plt.savefig('SPN4-04.png')
    plt.show()

super_dope_plotting_function_with_a_really_really_long_name()
