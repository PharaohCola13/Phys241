from numpy import *
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

data = loadtxt("./star_dist.csv", delimiter=",", skiprows=1, usecols=(0,1,2,3), unpack=True)
lab = loadtxt("./star_dist.csv", delimiter=",", dtype=str, skiprows=1, usecols=(4), unpack=True)

ra  = deg2rad(array(data[0]))
dec = deg2rad(array(data[1]))
mv = array(data[2])
Mv = array(data[3])

dp = deg2rad(27.1)
rp = deg2rad(192.9)
lp = deg2rad(122.9)

b = arcsin((sin(dp)*sin(dec)) + (cos(dp)*cos(dec)*cos(ra - rp)))
l = arctan((cos(dec)*cos(ra-rp))/((sin(dp)*sin(dec)) + (cos(dp)*cos(dec)*cos(ra-rp)))) - lp

plt.figure(1)
plt.scatter(rad2deg(l[0:23]),rad2deg(b[0:23]), marker="x", label="G Type", color="orange")
plt.scatter(rad2deg(l[23:]),rad2deg(b[23:]),marker="o", label="O Type", color="blue")
plt.xlabel("Galatic Latitude")
plt.ylabel("Galatic Longitude")
plt.legend()


plt.figure(2)
n, bins, patches = plt.hist(rad2deg(b), bins=20, rwidth=0.9, facecolor='blue', alpha=0.5)
plt.xlabel("Galatic Latitude")
plt.xlim(-90,90)
dist = 10.0 * 10.0**(0.2*(mv - Mv))

plt.figure(3)
d = dist * sin(b)
n, bins, patches = plt.hist([d[0:23],d[23:]], linspace(-3000,2000,60), label=["G Type","O Type"], alpha=0.5,color=["orange","blue"])
plt.xlabel("Vertical displacement from galatic plane")
plt.legend()
plt.show()
