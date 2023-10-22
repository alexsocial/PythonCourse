"""
Alex Chaban
Due 03-31-2023
Prof. Ionut Cardei
COP4045
Problem 1: Random Number Generation
"""

import random as rand #import random just in case it is needed

"""
For reference in formula:
X(n + 1) = (a * Xn + c) % m
Where X0 is the seed, a is the multiplier (0 < a < m)
c is the increment (0 <_ c < m), m is the modulus, and 0 <_ X0 < m.
In this case, 
m = 2^32
a = 22695477
c = 1
"""

"""
Part A: Random Sequence Class
Desc: Generates a random sequence of numbers based on the LCG formula.
Conditions: A seed x0, and a number of generations n.
"""
class RndSeq:
    #initialization where n is number of generations, x0 is seed value
    #if n < 0, generate infinite sequence. must comply with iteration interface
    def __init__(self, x0, n):
        self.i = 0
        self.m = 2**32
        self.a = 22695477
        self.c = 1
        if n < 0:
            self.n = -1
        else:
            self.n = n
        self.x0 = x0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n == self.i: #iteration kill, in the case of -1, it's impossible...
            raise StopIteration ("Iteration has ended.")
        self.x0 = ((self.a*self.x0 + self.c) % self.m) #follows formula listed above, sets new value
        self.i = self.i + 1
        return self.x0

"""
Part B: Generator
Description: Generates a random sequence of numbers based on the LCG formula.
Conditions: A seed x0, and a number of generations n.
Must use a yield generator.
"""
def rnd_gen(x0, n):
    it = 0
    m = 2**32
    a = 22695477
    c = 1
    while it != n:
        x0 = ((a*x0 + c) % m)
        yield x0
        it += 1


"""
MAIN FUNCTION
"""
def main():
    """ #THIS IS THE INFINITE TEST CASE, UNCOMMENT TO TEST IT
    rnd = RndSeq(1,-1)
    while (True):
        try:
            a = next(rnd)
            print(a)
        except StopIteration:
            'iteration stopped'
    """
    #list indentation with for support
    print('Printing iterator of 10 with seed 1:')
    rnd2 = RndSeq(1,10)
    ab = [i for i in rnd2]
    print(ab)

    #will cause the fail on the third call
    print('Printing iterator of 2 with seed 1 one by one:')
    rnd3 = RndSeq(1,2)
    it = iter(rnd3)
    a = next(it)
    print(a)
    a = next(it)
    print(a)
    #a = next(it)
    #print(a)

    print('Printing generator of 10 with seed 2:')
    rng = [i for i in rnd_gen(2,10)]
    print(rng)

    print('Printing generator of 3 with seed 1 with list initialization:')
    ab = list(rnd_gen(1,3))
    print(ab)
    #rng_cursed = [i for i in rnd_gen(1,-1)] #this is the infinite case
    #print(rng_cursed) 

main()