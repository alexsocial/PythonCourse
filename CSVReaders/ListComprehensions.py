"""
Alex Chaban
Due 02-09-2023
Prof. Ionut Cardei
COP4045
Problem 2
"""

"""
All of the following functions are using list comprehension
"""

"""
Returns all tuples where a^2 + b^2 = c^2
Conditions: 1 <= a,b,c <= 100
"""
def intTuple():
    li = []
    for a in range(1, 100):
        for b in range(1, 100):
            for c in range(1, 100):
                if (a**2 + b**2 == c**2):
                    li.append([a, b, c])
    print(li)

"""
Returns tuples from a list of strings
Tuple format is [length of item, element capitalized name]
"""
def stringTuple(strings):
    li = []
    for s in strings:
        li.append([len(s), s.upper()])
    print(li)

"""
Returns a list of strings of last name, first name
Conditions: a list of strings
"""
def nameTuple(names):
    a,b = '', ''
    li = []
    for i in names:
        a,b = i.split(" ", 1)
        name = b + ', ' + a
        li.append(name)
    print(li)

"""
Returns a concatenated version of all given strings
Conditions: a separator, and then any n number of strings
"""
def concatenate(separator, *string):
    """
    algorithm:
    use list comprehension to add to big string
    remove the last separator via string slicing
    """
    big_string = ''
    for s in string:
        big_string = big_string + s + separator
    big_string = big_string[:-len(separator)]
    print(big_string)

def main():
    print ('PART A:')
    intTuple()
    print ('\nPART B:')
    b = ['one', 'seven', 'three', 'two', 'ten']
    stringTuple(b)
    print ('\nPART C:')
    c = ["Jules Verne", "Alexandre Dumas", "Maurice Druon"]
    nameTuple(c)
    print ('\nPART D:')
    concatenate(':', 'Jules', 'Verne', 'Alexandre', 'Dumas')

main()