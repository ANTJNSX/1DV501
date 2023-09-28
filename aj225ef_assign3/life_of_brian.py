import os


def get_words(path, file_name):
    word_lst = []

    with open(input_file, "r") as file:
        for line in file:
            crr_line = line.split(" ")
            for i in crr_line:
                if i != '\n':
                    word_lst.append(i)

    return word_lst

def save_words(path, output_file, words):
    return 0

# Main program
path = os.getcwd()
input_file = 'data/life_of_brian.txt'

words = get_words(path, input_file)

output_file = f'/data/brian_{len(words)}_words.txt'

#save_words(path, output_file, words)
print('Saved', len(words), 'words in the file', path + output_file)

#print(words)
