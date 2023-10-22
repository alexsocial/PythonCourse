"""
Alex Chaban
Due 03-31-2023
Prof. Ionut Cardei
COP4045
Problem 2: Functional Programming
"""

from itertools import islice, filterfalse
import functools

"""
Boilerplate Generator taken from Problem 1
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
Part A: Infinite tuple generator
Description: Generates a random sequence of tuples (a, b)
where a and b are integers generated from rnd_gen(1, -1)
Conditions: 0 <_ a <_ b < m. m must be a number.
Must use a yield generator.
"""
def gen_rndtup(m):
    temp_gen = iter(rnd_gen(1, -1))

    while True:
        a, b = (next(temp_gen) % m), (next(temp_gen) % m)

        if b >= a:
            yield((a,b))

"""
MAIN FUNCTION
"""
def main():
    print('Part A (remains unprinted as it is infinite):')
    #print([i for i in gen_rndtup(10)])

    print('Part B:')
    first_eight = islice(gen_rndtup(10), 8)
    print(list(filterfalse(lambda x : x[0] + x[1] >= 6, first_eight)))

    print('Part C:')
    piece_one = iter(rnd_gen(1, -1))
    piece_two = iter(rnd_gen(2, -1))
    l_a = []
    l_b = [] #two generators, two maps to zip
    for i in range(0,8):
        a, b = (next(piece_one) % 100), (next(piece_two) % 100)
        l_a.append(a)
        l_b.append(b)
    l = zip(l_a, l_b)
    print(list(filterfalse(lambda x : x[0] > x[1], l))) #filters out any case of a > b

    print('Part D:')
    d_gen = islice(rnd_gen(1, -1), 10)
    l = list(i for i in d_gen)
    l = map(lambda x : x % 100, l)
    l = filter(lambda x : x % 13 == 0, l)
    print(list(l))

    print('Part E:') #fix
    e_gen = islice(gen_rndtup(10), 10)
    l = filter(lambda x : x[0] + x[1] >= 5, e_gen)
    l = map(lambda x : x[0] + x[1], l)
    l = functools.reduce(lambda a, b : a + b, l)
    print(l)

main()
