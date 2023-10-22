"""
Alex Chaban
Due 02-09-2023
Prof. Ionut Cardei
COP4045
Problem 1
"""

"""
This is a program to print the lines of a file, along with line numbers.
It takes the name of the file as an argument and a text variant.
If the user provides no text variant, it will substitute the filename as a .txt file.
"""
def line_number(filename, filename_txt=None):
    file_string = ''
    index = 1
    if filename_txt is None:
        filename_txt = filename + '.txt'
    try:
        print("Attempting to open file: " + filename)
        with open (filename, 'rt') as f:
            lines = f.readlines()
        for l in lines:
            file_string += str(index) + '. ' + str(l)
            index += 1
        print("Attempting to open file: " + filename_txt)
        with open (filename_txt, 'wt') as g:
            g.write(file_string)
    except FileNotFoundError:
        print('File not found. Did you check the name of the file?')
        return
    except IOError:
        print('I/O error')
        return
    except Exception as e:
        print(f'Something went wrong, {e}')
        return
    f.close()
    g.close()

"""
This is a function to print functions without comments in a tuple.
It takes the name of the file as the argument.
The tuples will be in an alphabetical list as follows:
[function name, line number, function body without comments]
"""
def parse_functions(filename):
    items = []
    line_number = 1
    function_name = ''
    function_body = ''
    index = 0
    try:
        print("Attempting to open file: " + filename)
        with open (filename, 'rt') as f:
            lines = f.readlines()
        """
        Loops through lines multiple times.
        Adds to index once a function is found, and subtracts to get the full length of the function body.
        Breaks when either the end of the file is reached or an out of bounds index is found.
        """
        while index < len(lines):
            if 'def' in lines[index]:
                function_name = lines[index].split('(')[0]
                line_number = index + 1
                index += 1
                while 'def' not in lines[index]:
                    lines[index] = lines[index].replace('\t', '\\t')
                    if '#' in lines[index]:
                        temp_string = lines[index].split('#')[0]
                        function_body += temp_string
                    else:
                        function_body += lines[index]
                    index += 1
                    if index >= len(lines):
                        break
                items.append([function_name, line_number, function_body])
                function_body = ''
                index -= 1    
            index += 1
    except FileNotFoundError:
        print('File not found. Did you check the name of the file?')
        return
    except IOError:
        print('I/O error')
        return
    except Exception as e:
        print(f'Something went wrong, {e}')
        return

    f.close()
    items.sort()
    print(tuple(items))

def main():
    #line_number('test.py')
    parse_functions('test.py')

main()