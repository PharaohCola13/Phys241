from numpy import *
import matplotlib.pyplot as plt


G = 6.67e-11
M = 1898e24

m = [8.93e22,4.8e22,1.48e23,1.08e23]
r = [4.218e8,6.711e8,1.0704e9,1.8827e9]


xi = []
for i in range(len(r)):
    xi.append((4*pi**2)/(G*(M+m[i])))

x = log10(array(r))
y = log10(sqrt(xi*array(r)**3))

plt.scatter(x, y)
plt.title("Evaluation of Kepler's Third Law on the Galilean Moons")
plt.xlabel(r'log$_{10}$(a)')
# plt.ylabel(r'log$_{10}$(P)')
plt.ylim(-10,10)
plt.xlim(0,10)

slope, intercept = polyfit(x, y, 1)
plt.plot(linspace(0, 10), slope*linspace(0,10)+intercept)
print("Slope of best-fit: {:.2f}".format(slope))
print("Y-intercept of best fit: {:.2f}".format(intercept))

plt.show()
