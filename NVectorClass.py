"""
Alex Chaban
Due 02-19-2023
Prof. Ionut Cardei
COP4045
Problem 1: Vector Class
"""

class NVector:
    number_sequence = []
    def __init__(self, *numbers):
        if len(numbers) == 1:
            self.number_sequence = list(numbers[0])
        else:
            for i in numbers:
                self.number_sequence.append(i)

    def __str__(self):
        f_string = "List of items in this object: "
        f_string += str(self.number_sequence)
        return f_string
    
    """
    Name: Length function [len(NVector)]
    Conditions: Requires one NVector object.
    Returns the length of the number sequence of the NVector object.
    """
    def __len__(self):
        return len(self.number_sequence)
    """
    Name: Get item function [NVector(n)]
    Conditions: Requires one NVector object and a numerical value.
    Returns the item located at n in the number sequence of the NVector object.
    """    
    def __getitem__(self, index):
        index = abs(index)
        try:
            return self.number_sequence[index]
        except IndexError:
            return "Index out of range."
    """
    Name: Set item function [a = NVector(n)]
    Conditions: Requires one NVector object and a numerical value.
    Changes the item located at n in the number sequence of the NVector object.
    """        
    def __setitem__(self, index, value):
        index = abs(index)
        try:
            self.number_sequence[index] = value
        except IndexError:
            return "Index out of range."
    """
    Name: Equal operator [N1 == N2]
    Conditions: Requires two NVector objects.
    Returns whether the two NVectors number sequence's match.
    """        
    def __eq__(self, other):
        return self.number_sequence == other.number_sequence
    """
    Name: Not Equal operator [N1 == N2]
    Conditions: Requires two NVector objects.
    Returns whether the two NVectors number sequence's do not match.
    """    
    def __ne__(self, other):
        return self.number_sequence != other.number_sequence
    """
    Name: Add operator [N1 + N2]
    Conditions: Requires two NVector objects.
    Returns an NVector of the added number sequences.
    """    
    def __add__(self, other):
        z = []
        for i in range(0, len(self.number_sequence)):
            z.append(self.number_sequence[i] + other.number_sequence[i])
        n1 = NVector(z)
        return n1.number_sequence
    """
    Name: Reverse Add operator [N2 + N1]
    Conditions: Requires two NVector objects.
    Returns an NVector of the added number sequences.
    """
    def __radd__(self, other):
        z = []
        for i in range(0, len(other.number_sequence)):
            z.append(self.number_sequence[i] + other.number_sequence[i])
        n1 = NVector(z)
        return n1.number_sequence
    """
    Name: Multiply operator [N1 * N2]
    Conditions: Requires two NVector objects or an NVector and a constant number.
    Returns an NVector of the multiplied number sequences.
    """
    def __mul__(self, other):
        z = []
        if type(other) is int:
            for i in range(0, len(self.number_sequence)):
                z.append(self.number_sequence[i] * other)
        elif type(other) is NVector:
            for i in range(0, len(self.number_sequence)):
                z.append(self.number_sequence[i] * other.number_sequence[i])
        else:
            return "Not a proper type"
        n1 = NVector(z)
        return n1.number_sequence
    """
    Name: Multiply operator [N2 * N1]
    Conditions: Requires two NVector objects or an NVector and a constant number.
    Returns an NVector of the multiplied number sequences.
    """    
    def __rmul__(self,other):
        z = []
        if type(self) is int:
            for i in range(0, len(other.number_sequence)):
                z.append(other.number_sequence[i] * self)
        elif type(self) is NVector:
            for i in range(0, len(other.number_sequence)):
                z.append(self.number_sequence[i] * other.number_sequence[i])
        else:
            return "Not a proper type"
        n1 = NVector(z)
        return n1.number_sequence
    """
    Name: Zeros function [zeros(N1)]
    Conditions: Requires an NVector object and a constant number.
    Returns an NVector with a number sequence of zeros of n length.
    """    
    def zeros(self, n):
        z = []
        for i in range(0, n):
            z.append(0)
        n1 = NVector(z)
        return n1
    
def testif(b, testname, msgOK="", msgFailed=""):
    """Function used for testing. 
    param b: boolean, normally a tested condition: true if test passed, false otherwise
    param testname: the test name
    param msgOK: string to be printed if param b==True  ( test condition true)
    param msgFailed: string to be printed if param b==False
    returns b
        """
    if b:
        print("Success: "+ testname + "; " + msgOK)
    else:
        print("Failed: "+ testname + "; " + msgFailed)
    return b



obj1 = NVector([1,2,3,4,5,6,7,8,9])
obj2 = NVector(9,8,7,6,5,4,3,2,1)
obj1[3] = 10
testif(obj1[3] == 10, "setitem works", "setitem failed")
obj3 = obj1+obj2
testif(obj3 == obj1+obj2, "add works", "add failed")
obj3 = obj1*obj2
testif(obj3 == obj1*obj2, "mul works", "mul failed")
obj4 = obj1.zeros(9)
testif(obj4 == obj1.zeros(9), "zeros works", "zeros failed")
