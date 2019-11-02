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
a = 1.
V0 = 1

def super_dope_plotting_function_with_a_really_really_long_name():
    print("SPN4-4, 2019 | " + title)
    print("====== ======= =========")
    x, dx = linspace(0.0001, a, 1001, retstep=True)
# Initializations
    wave = 0
    fig = plt.figure()

    sigma = ((-2 * V0)/a) * (1./sin((pi*x/a))) * (8.85e-12)
    plt.plot(x, sigma)
    plt.xlabel('$y/a$', fontsize=16)
    plt.ylabel('$V/V_0$', fontsize=16)
    plt.suptitle(suptitle, fontsize=16)
    plt.title(title, fontsize=12)
   # plt.savefig('SPN4-04.png')
    plt.show()

super_dope_plotting_function_with_a_really_really_long_name()
