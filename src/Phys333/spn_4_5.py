####
### Title: 	SPN-4-5
### Author: Spencer Riley
### Python Version: 2.7.13
####
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import *

idstr = 'By R. Sonnenfeld, New Mexico Tech Physics (Sept. 2017) -- Free for educational use only.'
suptitle = 'Griffith''s Figure 3.18'
## Oh look, it's me.
title = 'by: Spencer Riley'

# Some kind-of neat constants
a = 1.0
V0 = 1

def main():
    print("SPN4-5, 2019: " + title)
    print("=======  ======= =========")
    x = arange(0.0001, 1, 0.025)
    X, Y = meshgrid(x, x)
## This is Eq 3.37. I felt that it was easier to work with the result rather than the sum of terms
    VV = ((2*V0)/pi) * arctan((sin((pi*Y)/a))/(sinh((pi*X)/a)))

# plot stuff
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.view_init(10, -53)
    surf = ax.plot_wireframe(X, Y, VV)
# plot labels
    plt.ylabel('$y/a$', fontsize=16)
    plt.xlabel('$x/a$', fontsize=16)
    ax.set_zlabel('$V/V_0$')
# plot titles
    plt.suptitle(suptitle, fontsize=16)
    plt.title(title, fontsize=12)
# axis limits
    plt.ylim(0, 1)
    plt.xlim(0, 1)
    ax.set_zlim(0, 1)
# save and show
    plt.savefig('SPN4-5mesh.png')
    plt.show()

main()


