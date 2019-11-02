####
### Title: 	SPN-5-1
### Author: Spencer Riley
### Python Version: 2.7.13
####
import matplotlib.pyplot as plt
from numpy import *
## Initial Values
a = [50.]; c = [50.]; e = [50.]
b = [25.]; d = [25.]; f = [25.]; g = [25.]

phi = 100.
rng = range(0,10)
## Adds value of next iteration to previously defined list
for i in rng:
    a.append(int(0.25 * (phi + b[i] + c[i] + a[i])))
    b.append(int(0.25 * (a[i] + b[i] + d[i])))
    c.append(int(0.25 * (phi + a[i] + d[i] + e[i])))
    d.append(int(0.25 * (c[i] + f[i] + b[i])))
    e.append(int(0.25 * ((2.*c[i]) + (2.*f[i]))))
    f.append(int(0.25 * (d[i] + e[i] + g[i])))
    g.append(int(0.25 * (2.*f[i])))

## Prints out a pretty table
print("\t| " + "an" + " | " + "bn" + " | " + "cn" + " | " + "dn" + " | " + "en" + " | " + "fn" + " | " + "gn")
print("---"*15)
for i in range(len(a)):
    print(str(i) + "\t| " + str(int(a[i])) + " | " + str(int(b[i])) + " | " + str(int(c[i])) + " | " + str(int(d[i])) + " | " + str(int(e[i])) + " | " + str(int(f[i])) + " | " + str(int(g[i])))
## Plots iteration against Potential
plt.plot(rng, a[min(rng):max(rng)+1], label=r"$a_n$")
plt.plot(rng, b[min(rng): max(rng)+1], label=r"$b_n$")
plt.plot(rng, c[min(rng): max(rng)+1], label=r"$c_n$")
plt.plot(rng, d[min(rng): max(rng)+1], label=r"$d_n$")
plt.plot(rng, e[min(rng): max(rng)+1], label=r"$e_n$")
plt.plot(rng, f[min(rng): max(rng)+1], label=r"$f_n$")
plt.plot(rng, g[min(rng): max(rng)+1], label=r"$g_n$")
plt.legend()
plt.xlabel(r"$n$ (Iternation)")
plt.ylabel("Potential")
plt.title(r"Relaxation Method for $\phi$ = {}".format(phi))
plt.show()