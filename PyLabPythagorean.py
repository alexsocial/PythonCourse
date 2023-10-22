#Problem 2: pythagorean numbers
#Alex Chaban
#Prof. Ionut Cardei
#COP4045-001
#Due: 1/22/23

#imports
import pylab as pl
import math

def find_Pythagorean(n):
    n = int(n)
    #makes a,b,c and list
    combos = []
    a = 1
    b = 1
    c = 1
    #this took me 45 minutes to figure out an algorithm and it's just brute force with some tweaks
    print("List of Pythagorean Triples")
    while (a <= n+1):
        while (b <= n+1):
            while (c <= n+1):
                if a ** 2 + b ** 2 == c ** 2:
                    tempTuple = (a, b, c) #makes a tuple
                    combos.append(tempTuple) #appends it
                c += 1
            c = 1
            b += 1
        b = 1
        a += 1
    #print (type(combos[0])) #this is to check returns type tuple
    print (combos)

print("Press CTRL-Z or ENTER to exit the program.")
while True:
    n = input("Please enter n: ") #asks input
    if n == "": #two checks: one for the exit condition and a number condition
        exit()
    elif n.isnumeric() == False or int(n) == 0:
        print("Please enter a non-zero positive number.")
    else:
        find_Pythagorean(n)