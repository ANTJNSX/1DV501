import random


def count_occurrences(lst):
    dict = {}

    for i in range(1, 11):
        dict[i] = lst.count(i)

    return dict


rand_lst = []
for i in range(100):
    rand_lst.append(random.randint(0, 10))

dict = count_occurrences(rand_lst)

print(dict, '\n')

for i in dict:
    # För lite finare presentation
    if i == 10:
        print(i, "    ", dict[i])
    else:
        print(i, "     ", dict[i])
