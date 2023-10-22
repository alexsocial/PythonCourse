"""
Alex Chaban
Due 03-19-2023
Prof. Ionut Cardei
COP4045
Problem 2: Miscellaneous functions
"""

import turtle as t

"""
Name: Turtle Graph Generator
Desc: Creates a new Turtle Graph where it generates a leaf and stem.
Uses recursion to generate a 'stem', then adds leaf nodes.

Conditions:
Must be recursive. Integers should not be negative.

Algorithm: Use turtle.penup() or turtle.pendown() to STOP/START the drawing
Use turtle.goto(x,y) to work recursively. Use turtle.left(60) and turtle.right(120) 
to keep drawing upright. Use forward() and back() to draw.
Hard problem. Most likely giving up on this one.
"""
#couldn't figure this one out; go to TA or look at solution to figure it out.

"""
Name: Base X Converter
Desc: Takes a integer and a digit n between 2 and 26.
Converts the integer to another from base 10 to base n.

Conditions: 
Must be recursive. The integer must not be negative.

Algorithm: Have the base case be when the number is 0 or lower
Have the recursive case be when the number is above 0,
and split the problem into each number. Find a condition for letter conversion (i.e. base 11+)
Make sure it's all in strings.

Base conversion formula is logb c = a, or getting the remainder of n from base.
"""
def strB(n, base=10):
    #make the digits from base 2 - 26
    if base > 26 or base < 2:
        return ('invalid number')
    base_change = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E' \
                   'F','G','H','I','K','L','M','N','O','P']
    if(n <= 0): #base
        return str("")
    else: #recursive
        re = n % base
        n = int(n/base)
        return str(strB(n, base) + str(base_change[re]))
"""
Name: Binomial Coefficients
Desc: Calculates the binomial coefficients based on two provided values.

Conditions: 
Must be recursive AND must be memoized.

Algorithm: have the base cases and recursively call the function, with memoization beforehand
"""
def cnk_m(n,k):
    #call the function with an accumulator argument to memoize it
    d = {}
    return run_cmk(n,k,d)

def run_cmk(n,k,d):
    if k > n: #base cases
        return 0
    elif k == 0 or n == 0:
        return 1
    temp = str(n) + str(k) #memo check, MUST be a string to avoid duplicates
    if temp in d:
        return d[temp]
    d[temp] = run_cmk(n-1,k-1,d) + run_cmk(n-1,k,d) #recursive call
    return d[temp]
    
"""
Name: Pair Generator
Desc: Takes two lists, returns a list that matches indices of numbers.
i.e. input ([1,2,3], [4,5]) returns [(1,4), (2,5)]

Conditions: 
Must be recursive, use an accumulator argument.

Algorithm: 
Have a helper function as an accumulator storage system, and simply match the pairs.
Make the base cases when a max length is reached, or if a list is empty.
"""
def make_pairs(seq1, seq2):
    fin_list = []
    return pair_up(seq1,seq2,fin_list,0)

def pair_up(seq1,seq2,l,pos): #helper function
    if pos == len(seq1) or pos == len(seq2): #base cases
        return l
    if seq1 == [] or seq2 == []:
        l = []
        return l
    l.append((seq1[pos],seq2[pos]))
    return pair_up(seq1,seq2,l,pos+1)

"""
TESTIF FUNCTION PROVIDED BY PROFESSOR
"""
def testif(b, testname, msgOK="", msgFailed=""):
    """Function used for testing.
    param b: boolean, normally a tested condition: true if test passed, false
    otherwise
    param testname: the test name
    param msgOK: string to be printed if param b==True ( test condition true)
    param msgFailed: string to be printed if param b==False
    returns b
    """
    if b:
        print("Success: "+ testname + "; " + msgOK)
    else:
        print("Failed: "+ testname + "; " + msgFailed)
    return b

"""
MAIN FUNCTION
"""
def main():
    #part b
    c1 = strB(495625, base=26)
    testif(c1 == '1254D', 'base 26 test', "success on base conversion from 26", "fail on base conversion from 26")
    c2 = strB(495625, base=16) 
    testif(c2 == '79009', 'base 16 test', "success on base conversion from 16", "fail on base conversion from 16")
    c3 = strB(495625, base=8)
    testif(c3 == '1710011', 'base 8 test', "success on base conversion from 8", "fail on base conversion from 8")
    c4 = strB(495625, base=2)
    testif(c4 == '1111001000000001001', 'base 2 test', "success on base conversion from 2", "fail on base conversion from 2")
    c5 = strB(495625, base=27)
    testif(c5 == 'P4ND', 'out of bounds base test', "failure on error detection from base", "success on error detection from base")

    #part c
    c6 = cnk_m(5,3)
    testif(c6 == 10, 'cnk test 1', "success on 5,3", "fail on 5,3")
    c7 = cnk_m(15,15)
    testif(c7 == 1, 'cnk test 2', "success on 15,15", "fail on 15,15")
    c8 = cnk_m(20,5)
    testif(c8 == 15504, 'cnk test 3', "success on 20,5", "fail on 20,5")
    c9 = cnk_m(100,3)
    testif(c9 == 161700, 'cnk test 4', "success on 100,3", "fail on 100,3")
    c10 = cnk_m(6,2) 
    testif(c10 == 15, 'cnk test 5', "success on 6,2", "fail on 6,2")

    #part d
    c11 = make_pairs([1,2,3],[4,5,6])
    testif(c11 == [(1,4),(2,5),(3,6)], 'pair test 1', "success on matched lengths", "fail on matched lengths")
    c12 = make_pairs([1,2,3],[4,5])
    testif(c12 == [(1,4),(2,5)], 'pair test 2', "success on shorter set 2", "fail on shorter set 2")
    c13 = make_pairs([1,2],[4,5,6])
    testif(c13 == [(1,4),(2,5)], 'pair test 3', "success on shorter set 1", "fail on shorter set 1")
    c14 = make_pairs([1,2,3],[])
    testif(c14 == [], 'pair test 4', "success on empty set 2", "fail on empty set 2")
    c15 = make_pairs([],[4,5,6])
    testif(c15 == [], 'pair test 5', "success on empty set 1", "fail on empty set 1")

main()