import os

dir_path = os.getcwd()


def print_sub(dir_path):
    for path in os.listdir(dir_path):
        print(path)
        if os.path.isdir(os.path.join(dir_path, path)):
            print_sub(os.path.join(dir_path, path))


print_sub(dir_path)

