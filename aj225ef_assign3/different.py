import random


def different(lst):
    return list(sorted(set(lst)))


rand_lst = random.sample(range(0, 200), 100)
print(rand_lst, '\n')
print(different(rand_lst))
