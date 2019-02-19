# Spencer Riley
from numpy import *
import unicodedata

xi = -2
xf = 2
dx = array([1, 0.5, 0.1, 0.01])

print(unicodedata.lookup("GREEK CAPITAL LETTER DELTA")+ "x" + "\t\t" + "Results" + "\t\t" + "Error")
for i in dx:
    x = arange(xi, xf + i, i)
    y = x**4 - 2*x + 1

    # Integration
    Int = 0
    for j in range(len(x)):
        try:
            Int = Int + i/3 * (y[j] + 4*y[j+1] + y[j+2])
        except IndexError:
            continue
    error = abs(Int - 28)
    print("{}".format(i) + "\t\t" + "{:1.3f}".format(Int) + "\t\t" + "{:1.3f}".format(error))
