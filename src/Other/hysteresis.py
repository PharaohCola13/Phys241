from numpy import *
import matplotlib.pyplot as plt

time = arange(0.5,20.5,0.5)
temp = array([24.4,24.3,24.3,24.4,24.4,24.4,24.5,24.5,24.6,24.7,24.7,24.8,24.8,
              24.9,24.9,24.9,25.0,25.1,25.1,25.2,25.2,25.2,25.3,25.4,25.4,25.4,
              25.5,25.5,25.6,25.6,25.7,25.7,25.7,25.7,25.8,25.8,25.9,25.9,26.0,
              26.0])
plt.scatter(time,temp)
plt.xlabel("Time [min]")
plt.ylabel(r"Temperature [$^\circ$C]")
plt.show()
print(time)
