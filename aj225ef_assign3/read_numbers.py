import os
import math

ten_k_a = os.getcwd() + r'\file_10k_integers_A.txt'
ten_k_b = os.getcwd() + r'\file_10k_integers_B.txt'

# Create list with the integers from splitting each line and converting to int
lst_a = []
with open(ten_k_a, "r", encoding="utf-8") as file:
    for line in file:
        for i in line.split(","):
            lst_a.append(int(i))


# Create list with the integers from splitting each line and converting to int
lst_b = []
with open(ten_k_b, "r", encoding="utf-8") as file:
    for line in file:
        for i in line.split(":"):
            lst_b.append(int(i))


def mean(lst):
    return round((sum(lst) / 10_000), 1)


def std(lst):
    variant_lst = []
    # fix list and add variants to list, then return variant mean
    for i in lst:
        variant_lst.append((mean(lst)-i)**2)

    return round(math.sqrt((sum(variant_lst) / 10_000)), 1)


print("Results for file A:")
print(f'mean = {mean(lst_a)}, standard deviation = {std(lst_a)}')

print("\nResults for file B:")
print(f'mean = {mean(lst_b)}, standard deviation = {std(lst_b)}')
