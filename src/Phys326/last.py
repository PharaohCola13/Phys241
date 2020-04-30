import matplotlib.pyplot as plt
from numpy import *
from scipy.optimize import curve_fit

data = loadtxt("./trimmed_exoplanet.csv", delimiter=",", usecols=(1,2), unpack=True)

x = log(array(data[0]))
y = log(array(data[1]))

print(x)
blue_coef = polyfit(x,y,1)
plt.scatter(x, y, color="blue", label="blue filters")

plt.plot(x, blue_coef[0]*x+blue_coef[1], '--r', label="y = {:.2f}x + {:.2f}".format(blue_coef[0], blue_coef[1]))
plt.legend()
plt.show()
