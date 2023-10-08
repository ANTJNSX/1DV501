import os
import string

lowercase_letters = set(string.ascii_lowercase)
path = os.getcwd()
input_file = r'aj225ef_assign3\data\brian_13419_words.txt'


def get_letters(path, file_name):
    letter_dict = {}

    with open(input_file, "r", encoding="utf-8") as file:
        # nested loops to get to the characters for each line in the document
        for line in file:
            for chr in line:

                chr = chr.lower()
                if chr in lowercase_letters:
                    if chr in letter_dict:
                        # increase count
                        letter_dict[chr] += 1
                        pass
                    else:
                        # add to dict
                        letter_dict[chr] = 1
                        pass
    return letter_dict


# Main program
ldict = dict(sorted(get_letters(path, input_file).items(), key=lambda item: item[0]))

print("Reading text from the file: .../life_of_brian.txt")
print("Total number of letters:", sum(ldict.values()))

histogram = 200
histogram_lowcase = 20
print("Histogram amount :", "\nI =", histogram_lowcase, "\n| =", histogram)

for item in ldict:
    if ldict[item] >= 200:
        print(item, ":", int(ldict[item]/histogram)*"|")
    else:
        print(item, ":", int(ldict[item]/histogram_lowcase)*"I")
