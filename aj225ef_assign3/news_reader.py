import os

# Tecken som inte är ord och ska försvinna från listan
# Det kan även göras på ett lite finare sett då man kollar ifall "ordet"
# korrekta symboler => alphabetet, och bara appendar till listan med de ordet
delimiters = [",", ".", "!", "?", "&", ";", ":",
              "[", "]", "(", ")", "•", '"', '”', "½", "0", "1", "2",
              "3", "4", "5", "6", "7", "8", "9", "\n", "- ", " -"]


# Functionen för att extrahera orden ur varje linje av filen
def get_words(path, file_name):
    word_lst = []

    # öppna filen
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:

            # Loopa över varje symbol och ta bort dom om de finns
            for delimiter in delimiters:
                line = " ".join(line.split(delimiter))

            # ta sen tar vi bort newlines och sätt in den i listan
            crr_line = line.replace("\n", "").split()

            # Ploppa in all värden i lista in i huvud listan
            word_lst.extend(crr_line)

    return word_lst


# Writes the words one by one to the file
def save_words(path, output_file, words):
    with open(output_file, "w", encoding="utf-8") as file:
        for word in words:
            file.write("%s\n" % word)


# Main program
path = os.getcwd()
input_file = r'aj225ef_assign3\data\swe_news.txt'

words = get_words(path, input_file)

output_file = f'aj225ef_assign3/data/SWE_News_{len(words)}_words.txt'

save_words(path, output_file, words)
print('Saved', len(words), 'words in the file', path + output_file)
