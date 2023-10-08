import os

dir_path = os.getcwd()
depth = 0


def pretty_print_sub(dir_path, depth):
    for path in os.listdir(dir_path):
        print(depth*'   ', path)
        if os.path.isdir(os.path.join(dir_path, path)):
            depth += 1
            pretty_print_sub(os.path.join(dir_path, path), depth)
            depth -= 1


pretty_print_sub(dir_path, depth)
