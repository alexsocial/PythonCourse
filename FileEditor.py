"""
Alex Chaban
Due 03-19-2023
Prof. Ionut Cardei
COP4045
Problem 1: Editor
"""

"""
Name: Read and Snip
Desc: Reads a file, then returns the string between indexs [fro, to). Inclusively
has fro.

Conditions: 
All files are under the UTF-8 Encoding by assumption.
If to == -1 (default), all content starting at index fro is returned.
If to > file length, return an error message prompted by an IndexError.

Algorithm: Loop through the file lines, and slice based on line position, scouting for line breaks.
Then, slice the string for fro-to.
"""
def ed_read(filename, fro=0, to=-1): #from is a keyword, can't use it
    try:
        #print("Attempting to open file: " + filename)
        with open(filename, 'r', encoding='utf8') as f:
            lines = f.readlines()
            file_str = ""
            for l in lines:
                if "\n" in l:
                    file_str += l[:-1]
                else:
                    file_str += l
            if to < 0:
                return file_str[fro:len(file_str)]
            else:
                return file_str[fro:to]
    except FileNotFoundError:
        return("File not found. Maybe check the spelling?")
    except IndexError:
        return("Error, parameter to exceeds file length. Please try again.")
    except IOError:
        return("IO Error. Please try again.")
    f.close()

"""
Name: Search
Desc: Reads a file and searches for a case sensitive keyword. Returns
a list of starting indices where the phrase is located. Will return []
if empty.

Conditions: 
All files are under the UTF-8 Encoding by assumption.
A valid string is usable.

Algorithm: Reuse open and read code (as a boilerplate) and limit search to search length
subtracted by max length, slice accordingly.
"""
def ed_find(filename, search_str):
    found = []
    try:
        #print("Attempting to open file: " + filename)
        with open(filename, 'r', encoding='utf8') as f:
            lines = f.readlines()
            file_str = ""
            for l in lines:
                if "\n" in l:
                    file_str += l[:-1]
                else:
                    file_str += l
            for i in range(0, (len(file_str) - len(search_str))):
                if (file_str[i:(i+len(search_str))]) == search_str:
                    found.append(i)
            return found
    except FileNotFoundError:
        return("File not found. Maybe check the spelling?")
    except IOError:
        return("IO Error. Please try again.")


"""
Name: Replace Search
Desc: Reads a file and searches for a case sensitive keyword. Replaces
all instances of keyword with a new one if occurence = -1. If it isn't
-1, then it replaces the nst+1 occurence of it. Returns the amount
of times the string was replaced.

Conditions: 
All files are under the UTF-8 Encoding by assumption.
Valid strings are usable.

Algorithm: Reuse open and read code (as a boilerplate) and reuse search to search length
subtracted by max length, slice accordingly.
If occurence is not -1, run the ed_find function, and replace specifically the instance
at that index.
"""
def ed_replace(filename, search_str, replace_with, occurence=-1):
    try:
        #print("Attempting to open file: " + filename)
        with open(filename, 'r', encoding='utf8') as f:
            lines = f.readlines()
            file_str = ""
            for l in lines:
                if "\n" in l:
                    file_str += l[:-1]
                else:
                    file_str += l
        found = ed_find(filename, search_str)
        if occurence == -1:
            file_str = file_str.replace(search_str, replace_with)
            #print(file_str)
            return len(found)
        elif occurence < -1 or occurence >= len(found):
            return ("Not a valid number. Please try again.")
        else:
            #print(f"Replaced instance {occurence+1} at index {found[occurence]}")
            new_file_str = file_str[0:found[occurence]] + replace_with\
                + file_str[found[occurence]+len(search_str):len(file_str)]
            #print(new_file_str)
            return(1)
    except FileNotFoundError:
        return("File not found. Maybe check the spelling?")
    except IOError:
        return("IO Error. Please try again.")


"""
Name: Append
Desc: Reads a file and adds a string to the end of it.
If the file doesn't exist, creates a new one under the same name provided.

Conditions: 
All files are under the UTF-8 Encoding by assumption.
Valid strings are usable.

Algorithm: Reuse open and read code (as a boilerplate) and open as an 'a' file
Get it to copy the file string and add the new string to the end of it.
If the file doesn't exist, creates a new one under the same name provided since
'a' will do that.
"""
def ed_append(filename, string):
    try:
        #print("Attempting to open file: " + filename)
        with open(filename, 'a', encoding='utf8') as f:
            f.write(string)
            f.close()
            return len(string)
    except IOError:
        return("IO Error. Please try again.")

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

def main():
    fn = "test_file.txt"
    print(ed_read(fn, 0, -1))
    t0 = ed_find(fn, 'lor')
    t1 = ed_replace(fn, 'lor', 'I AM REPLACED', -1)
    t2 = ed_replace(fn, 'lor', 'BUT ONLY ONCE', 2)
    testif(t0 == [14,105,250,304], 'find function','find works', 'find failed')
    testif(t1 == 4, 'replace all instances','replace all works', 'replace all failed')
    testif(t2 == 1, 'replace one instance','replace one works', 'replace one failed')
    ed_append('i_am_a_file.txt', "hello world!")
    ed_append(fn, "this is my custom addition!")

main()