
def positive_int(float_lst):
    lst = []

    for i in float_lst:
        if i > 0:
            lst.append(i)

    return lst


def largest_K(N):
    if N <= 0:
        return 0  # Handle invalid input

    sum = 0
    K = 1

    while sum + K <= N:
        sum += K
        K += 2

    return K - 2


print(largest_K(1))

print(positive_int([1.3, 2.67, -2.25, 4.88]))
