# Spencer Riley
from numpy import *
import matplotlib
from matplotlib import pyplot as plt


xi = 0
xf = 2
dx = array([1, 0.5, 0.1, 0.01])

print("Delta x" + "\t\t" + "Results" + "\t\t" + "Error")
for i in dx:
    #print("i = {}".format(i))
    x = arange(xi, xf + i, i)

    y = x**4 - 2*x + 1

    # Integration

    Int = 0
    for j in range(1, len(x)):
        Int = Int + 0.5*i * (y[j] + y[j-1])
    error = abs(Int - 28)
    print("{}".format(i) + "\t\t" + "{:1.3f}".format(Int) + "\t\t" + "{:1.3f}".format(error))