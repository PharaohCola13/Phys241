import matplotlib.pyplot as plt
from numpy import *

t = linspace(-100e-6, 100e-6,100)
sg10 = 1.91 * cos(1.1e5 * t)
cg10 = 1.34 * cos(1.1e5 * t + deg2rad(75.3))

plt.figure(1)
plt.plot(t,sg10)
plt.plot(t,cg10)
plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))

sg25 = 2 * cos(1.58e5 * t)
cg25 = 0.28 * cos(1.58e5 * t - deg2rad(85.3))
plt.figure(2)
plt.plot(t,sg25)
plt.plot(t,cg25)
plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
plt.show()
