#Problem 3: duplicated substrings
#Alex Chaban
#Prof. Ionut Cardei
#COP4045-001
#Due: 1/22/23

#func 1, s is string, n is length, do NOT use str
def find_dup_str(s, n):
    if len(s) <= n or n >= 4:
        return ""
    l = len(s) - n #length of string - required characters to prevent out of bounds
    m = 0 #marker to start to prevent dupe
    """
    algorithm:
    take a slice of n characters
    loop until slice is found again
    if not, take next slice
    repeat until there are no more possible slices
    """
    while (m != l):
        slice = s[m:m+n]
        for i in range(m + 1, l + 1):
            temp = s[i:i+n]
            if temp == slice:
                return slice
        m+=1
    return ""

def find_max_dup(s): #part b: takes the maximum
    sizeTwo = find_dup_str(s,2)
    sizeThree = find_dup_str(s,3)
    """
    algorithm:
    use the previous function to get lower sizes 2 and 3
    check if it has a size 3
    if not check size 2
    if not return blank
    """
    if sizeThree != "":
        return sizeThree
    elif sizeTwo != "":
        return sizeTwo
    else:
        return "\"\""

#final call
t = input("Enter string to find substring: ")
print(find_max_dup(t))