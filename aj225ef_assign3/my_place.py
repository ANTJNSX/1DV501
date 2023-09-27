
import os

dir_path = r'C:\Users\antom\Documents\UNI\1DV501\aj225ef_assign3'
print(f"I am right now at: {dir_path}")


def count_directories(dir_path):  # Returns the number of directories
    count = 0
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1

    return count


def count_files(dir_path):  # Returns the number of files
    count = 0
    for path in os.listdir(dir_path):
        if os.path.isdir(os.path.join(dir_path, path)):
            count += 1

    return count


print(f"Below me I have {count_directories(dir_path)} directories/folders")

print(f"This directory contains {count_files(dir_path)} files")
