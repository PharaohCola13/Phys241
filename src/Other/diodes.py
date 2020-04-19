import matplotlib.pyplot as plt
from numpy import *
from scipy.optimize import curve_fit

def Part1():
    plt.figure(0)
    R = 56
    def silicon(R):
        V_r = [0, 1.1, 6.4, 12.8, 16.0, 46.3, 98.7, 162.2, 192.5, 241.4, 310.6,
              361, 417, 503, 566, 649, 705, 765, 822, 902, 977]
        V_d = [-2.9, 425, 504, 535, 546, 595, 631, 655, 663, 674, 687, 695, 703,
               713, 719, 727, 731, 736, 740, 746, 750]
        return array(V_r)/R, array(V_d)

    I_1, V_r1 = silicon(R)
    plt.plot(V_r1/1000.,(I_1)/1000., color='black', label="Silicon")

    def func(x,a,b):
        return a*(exp(x/b) - 1)

    # yn = (I_1)/1000. + 0.05*random.normal(size=len(V_r1/1000.))

    # popt, pcov = curve_fit(func, V_r1/1000., yn)
    popt = [4.495e-07, 7.325e-02]

    plt.plot(V_r1/1000., func(V_r1/1000.,*popt), color="purple", linestyle="--", label=r"$I = {:.2E}*(e^\frac{{V_d}}{{{:.2E}}} - 1)$".format(float(popt[0]), popt[1]))
# plt.xlabel(r'$test \frac{{1}}{{{}}}$'.format(g))
    def red(R):
        V_d = [0.1, 1.9, 19.9, 25.4, 65.4]
        V_r = [1516, 1657, 1778, 1796, 1885]
        return array(V_d)/R, array(V_r)

    I_2, V_r2 = red(R)
    plt.plot(V_r2/1000.,(I_2)/1000.,  color='red', label="Red LED")

    def blue(R):
        V_r = [2325, 2405, 2552, 2610, 2710]
        V_d = [0.1, 1.0, 21.3, 42.7, 90.5]
        return array(V_d)/R, array(V_r)

    I_3, V_r3 = blue(R)
    plt.plot(V_r3/1000., array(I_3)/1000., color='blue', label="Blue LED")
    plt.scatter(1642/1000., (0.2/R)/1000., color="green", label="Green LED")
    plt.scatter(1687/1000., (1.4/R)/1000., color="gold", label="Yellow LED")
    plt.title("Current-Voltage Relationship of Measured Diodes")
    plt.ylabel("Current [A]")
    plt.xlabel("Voltage [V]")
    plt.legend()

    plt.figure(1)
    def threshold():
        h = 6.63e-34
        c = 3e8
        l = array([6.5e-7, 475e-9, 500e-9, 580e-9])
        E = ((6.626e-34)*(3e8))/l
        plt.scatter(1.516, E[0], color="red")
        plt.errorbar(1.516,E[0], yerr=(-(h*c)/l[0]**2)*(50e-9), color="red")

        plt.scatter(2.325, E[1], color='blue')
        plt.errorbar(2.325,E[1], yerr=(-(h*c)/l[1]**2)*(50e-9), color="blue")

        plt.scatter(1.642, E[2], color='green')
        plt.errorbar(1.642,E[2], yerr=(-(h*c)/l[2]**2)*(50e-9), color="green")

        plt.scatter(1.687, E[3], color='gold')
        plt.errorbar(1.687,E[3], yerr=(-(h*c)/l[3]**2)*(50e-9), color="gold")

        plt.xlabel("Threshold voltage [V]")
        plt.ylabel("Photon Energy [J]")
        plt.title("Threshold Voltage and Energy Relation for LEDs")
    threshold()

    plt.show()
def Part2():
    def N914():
        plt.figure(0)
        V1 = [2.7e-3, 0.556, 1.068, 1.551, 2.086, 2.575, 2.999, 3.526, 4.07, 4.55, 5.04, 5.49, 6.01, 6.53, 7.02, 7.54]
        V2 = [0,0,0,0, 0.3e-3, 0.7e-3, 1.3e-3, 3e-3, 13.3e-3, 72.6e-3, 0.235, 0.465, 0.778, 1.126, 1.469, 1.840]

        V2_l = [0, 1.1e-3, 6.4e-3, 12.8e-3, 16.0e-3, 46.3e-3, 98.7e-3, 162.2e-3, 192.5e-3, 241.4e-3, 310.6e-3,
              361e-3, 417e-3, 503e-3, 566e-3, 649e-3, 705e-3, 765e-3, 822e-3, 902e-3, 977e-3]
        V1_l = [-2.9e-3, 425e-3, 504e-3, 535e-3, 546e-3, 595e-3, 631e-3, 655e-3, 663e-3, 674e-3, 687e-3, 695e-3, 703e-3,
               713e-3, 719e-3, 727e-3, 731e-3, 736e-3, 740e-3, 746e-3, 750e-3]
        R = 56
        I = array(V2)/R
        I_l = array(V2_l)/R
        plt.title("Current-Voltage relationship for 1N914 Diode")
        plt.scatter(V1, I, label="Part 2 data")
        plt.scatter(V1_l, I_l, label="Part 1 data")
        plt.ylabel("Current [A]")
        plt.xlabel("Voltage [V]")
        plt.legend()

    def pv_mod():
        plt.figure(1)
        R = [2.729e3, 56.6, 1.0, 30.57e3, 10e3, 401.1]
        V1 = [4.70, 4.71, 4.71, 4.69, 4.70, 4.70]
        V2 = [1.2e-3, 0.0, 0.0, 14.3e-3, 4.6e-3, 0.1e-3]
        I = array(V2)/array(R)
        plt.scatter(V1, I)
        plt.scatter(4.70, 0)
        plt.scatter(0, 7.35e-3)
        plt.title("Current-Voltage relationship for Photovoltaic Module")
        plt.xlabel("Voltage [V]")
        plt.ylabel("Current [A]")
    N914()
    pv_mod()
    plt.show()
Part2()
