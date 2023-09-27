import os

ten_k_a = r'/home/ant/UNI/1DV501/aj225ef_assign3/file_10k_integers_A.txt'
ten_k_b = r'/home/ant/UNI/1DV501/aj225ef_assign3/file_10k_integers_B.txt'

# Create list with the integers from splitting each line and converting to int
lst_a = []
with open(ten_k_a, "r") as file:
    for line in file:
        for i in line.split(","):
            lst_a.append(int(i))


# Create list with the integers from splitting each line and converting to int
lst_b = []
with open(ten_k_b, "r") as file:
    for line in file:
        for i in line.split(","):
            lst_b.append(int(i))

variant_lst = []

def mean(lst):
    return round((sum(lst) / 10_000), 1)


def std(lst):
    # fix list and add variants to list, then return variant mean 

    return 0


print(mean(lst_a))

