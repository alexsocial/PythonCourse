#Problem 1: quadratic equations
#Alex Chaban
#Prof. Ionut Cardei
#COP4045-001
#Due: 1/22/23

#imports
import pylab as pl
import math

#repeater, takes in inputs
def main():
    a=0
    b=0
    c=0
    a = input("Enter a: ")
    if a == "": #force exit if needed
        exit()
    b = input("Enter b: ")
    c = input("Enter c: ")
    #convert inputs to floats, note: unsure if i can just do float(input(text))
    a = float(a)
    b = float(b)
    c = float(c)
    #run equation
    quadratic(a, b, c)

#the problem solver, returns the graph and solution
def quadratic(a, b, c):
    expression = math.pow(b,2) - (4 * a * c)
    x1 = 0.0
    x2 = 0.0
    n = 150
    if expression < 0:
        print("no real solutions")
        #using xopt formula provided, between x1 and x2 for 150 points
        x1 = (-b) / (2 * a)
        x2 = x1
        x = pl.linspace(x1 - 2, x2 + 2, n)
    elif expression == 0:
        x1 = ((-b) + math.sqrt(expression))/(2*a)
        x2 = x1
        print("one solution: " + str(x1))
        #graphing between x1 and x2 for 150 points
        pl.plot(x1, 0, "bo")
        x = pl.linspace(x1 - 4, x2 * -1 + 2, n)
    else:
        x1 = ((-b) + math.sqrt(expression))/(2*a)
        x2 = ((-b) - math.sqrt(expression))/(2*a)
        print("two solutions: x1 = " + str(x1) + ", x2 = " + str(x2))
        #graphing between x1 and x2 for 150 points
        #pl.plot(x2, x2, "b")
        pl.plot(x1, 0, "bo")
        pl.plot(x2, 0, "bo")
        x = pl.linspace(x1 + 2, x2 - 2, n)
    
    dx = (x1 - x2) / (n - 1) #delta
    x+=dx
    #plug in quadratic formula for y
    #can't use math.pow b/c throws error. using ** instead
    y = a*x**2 + b * x + c

    #plotting points
    pl.plot(x, y, "r") #doesn't immediately show
    pl.show()
#program activate
print("Welcome to the quadratic solver. Press CTRL-Z at any time to quit, or press ENTER when entering a.")
while(True):
    main()