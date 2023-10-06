'''
It has been a lot of programming in this course. But how many lines of Python code have you actually written?
Write a program count_lines.py containing a function def count_py_lines(dir_path)
returning a count (an integer) of all the non-empty lines in all Python files (ending with .py)
in the directory specified by dir_path and all its subdirectories (transitively).
'''

import os

dir_path = os.getcwd()
total_lines = 0
count = 0

def count_py_lines(dir_path):
    global total_lines
    global count
    line_count = 0

    # Start working through the directories
    for path in os.listdir(dir_path):
        if os.path.isdir(os.path.join(dir_path, path)):
            count_py_lines(os.path.join(dir_path, path))

        # check for files that end with .py
        if path.endswith('.py'):
            # Get the line count
            with open(os.path.join(dir_path, path), "r") as file:
                li = file.readlines()
            count += 1
            total_lines += len(li)


    return total_lines


print("Number of lines:", count_py_lines(dir_path))
print("Across:", count, "Files")

