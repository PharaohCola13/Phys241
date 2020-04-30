from numpy import *
import matplotlib.pyplot as plt

A = loadtxt("./data/A_Sirius.txt", unpack=True)
B = loadtxt("./data/B_Rigel.txt", unpack=True)
F = loadtxt("./data/F_Procyon.txt", unpack=True)
G = loadtxt("./data/G_Capella.txt", unpack=True)
planet = loadtxt("./data/Jupiter.txt", unpack=True)
K = loadtxt("./data/K_Aldebaran.txt", unpack=True)
M = loadtxt("./data/M_Betelgeuse.txt", unpack=True)
nebula = loadtxt("./data/M42.txt", unpack=True)
OB = loadtxt("./data/OB_Spica.txt", unpack=True)

fig, ax = plt.subplots(7, sharex='col',
                        gridspec_kw={'hspace': 0, 'wspace': 0})
ax[0].scatter(OB[1], OB[2], s=0.5, label="OB Spica")
ax[0].axvline(4363, color="red")
ax[0].axvline(4861, color="red")
ax[0].axvline(6563, color="red")
ax[0].legend()
ax[1].scatter(B[1], B[2], s=0.5, label="B Rigel")
ax[1].legend()
ax[2].scatter(A[1], A[2], s=0.5, label="A Sirius")
ax[2].axvline(4110, color="red")
ax[2].axvline(4340, color="red")
ax[2].axvline(4865, color="red")
ax[2].axvline(6563, color="red") # HIa
ax[2].legend()
ax[3].scatter(F[1], F[2], s=0.5, label="F Procyon")
ax[3].axvline(4350, color="red")
ax[3].axvline(4858, color="red")
ax[3].axvline(6563, color="red") # HIa
ax[3].legend()
ax[4].scatter(G[1], G[2], s=0.5, label="G Capella")
ax[4].axvline(4861, color="red")
ax[4].axvline(5876, color="red")
ax[4].axvline(6563, color="red") # HIa
ax[4].legend()
ax[5].scatter(K[1], K[2], s=0.5, label="K Aldebaran")
ax[5].axvline(5217, color="red")
ax[5].axvline(5876, color="red")
ax[5].axvline(6260, color="red")
ax[5].legend()
ax[6].scatter(M[1], M[2], s=0.5, label="M Betelgeuse")
ax[6].axvline(5217, color="red")
# ax[1].axvline(5577, color="red")
ax[6].axvline(5876, color="red")
ax[6].axvline(6260, color="red")
ax[6].legend()


fig, ax = plt.subplots(2, sharex='col',
                        gridspec_kw={'hspace': 0, 'wspace': 0})

ax[0].scatter(nebula[1], nebula[2], s=0.5, label="M42")
ax[0].axvline(5007, color="red")
ax[0].axvline(6583, color="red")
ax[0].legend()

ax[1].scatter(planet[1], planet[2], s=0.5, label="Jupiter")
ax[1].axvline(4861, color="red")
ax[1].axvline(5210, color="red")
ax[1].axvline(5876, color="red")
ax[1].axvline(6200, color="red")
ax[1].axvline(6494, color="red")
ax[1].legend()
plt.show()
