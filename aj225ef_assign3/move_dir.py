import os

inp = ""
new_dir = r''
base_path = r'C:\Users\antom\Documents\UNI\1DV501'
dir_list = []
file_list = []
break_program = False


# Returns a list of strings with the names of the files
def list_files(dir_path):
    count = 0
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
            print(count, ".", path)
    print()


def change_dir():
    new_dir = input("Name of directory to enter: ")
    global base_path
    base_path = base_path + r"\\" + new_dir


# Returns a list of strings with the names of the directories
def list_dir(dir_path):
    count = 0
    for path in os.listdir(dir_path):
        if os.path.isdir(os.path.join(dir_path, path)):
            count += 1
            print(count, ".", path)
    print()


def quit():
    global break_program
    break_program = True


while break_program is not True:

    print("1. List directories \n2. Change directory \n3. List files \n4. Quit")

    inp = int(input("\n==> "))

    match inp:
        case 1:
            list_dir(base_path)

        case 2:
            change_dir()

        case 3:
            list_files(base_path)

        case 4:
            quit()
