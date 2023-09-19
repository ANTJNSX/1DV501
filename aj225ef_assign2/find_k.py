
def find_smallest_k(n):
    if n <= 0:
        raise ValueError("Please enter a positive integer.")

    sum_odd = 0
    k = 1

    while sum_odd <= n:
        sum_odd += k
        k += 2

    return k - 2


def find_largest_k(n):
    if n <= 0:
        raise ValueError("Please enter a positive integer.")

    sum_even = 0
    k = 0

    while sum_even < n:
        sum_even += k
        k += 2

    return k - 4


try:
    n = int(input("Enter a positive integer: "))
    smallest_k = find_smallest_k(n)
    largest_k = find_largest_k(n)

    print(f"{smallest_k} is the smallest k such that 1+3+5+...+k > {n}")
    print(f"{largest_k} is the largest k such that 0+2+4+6+...+k < {n}")

except ValueError as e:
    print(e)

