# The function read_file(file_path) should read the text file
# specified by file_path and return a list of strings containing
# each line in the file.

import os


file_path = str(os.getcwd() + r"\mamma_mia.txt")
print(file_path)
s_lst = []


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            s_lst.append(line)

    return s_lst


def write_file(lines, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(lines)


# for l in s_lst:
#     print(l)

print(file_path)
print(*read_file(file_path))

print("---------------------------------------")

file_path = os.getcwd() + r"/text_writefile.txt"
write_file("Test write_file #2", file_path)
print(*read_file(file_path))
