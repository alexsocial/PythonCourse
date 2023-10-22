#Problem 4: function visualization
#Alex Chaban
#Prof. Ionut Cardei
#COP4045-001
#Due: 1/22/23

#imports
import matplotlib.pyplot as plt
import math

def plot_function(fun_str, domain, ns): #string, tuple, and sample number
    ns = int(ns)
    xs = []
    ys = [] #list
    x0 = int(domain[0]) #lower
    x1 = int(domain[1]) #upper
    x = x0
    dx = (x1 - x0) / ns
    while x <= x1: 
        xs.append(x)
        y = eval(fun_str)
        ys.append(y)
        x += dx
    #print func
    print("\t\tx\t\ty\n-----------------------------------------")
    for i in range(0,len(xs)):
        print(("{:+.5f}\t\t{:+.5f}").format(xs[i],ys[i]))

    plt.plot(xs, ys, "bo-") #graph initialization
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(fun_str)

    plt.show()


fun_str = input("Enter function with variable x: ")
ns = input("Enter number of samples: ")
xmin = input("Enter xmin: ")
xmax = input("Enter xmax: ")
domain = (xmin, xmax)
plot_function(fun_str, domain, ns)