'''
Exercise description:

Assume a unit circle centred around origin inside a
square with sides 2 like in the figure above.
Assume also that we randomly generate N points (x,y) where
both x and y are within the range [- 1,1].
The proportion of points inside the circle should then approximately
be the same as the ratio between the circle area pi * R^2 (which equals
pi since R=1) and the square area 4.
This relation can be used to compute an approximation of pi.
Write a program pi_approx.py that computes (and prints) a pi approximation
for N=100, N=10000, and N=1000000.
Print also the error (i.e. the absolut value of pi_actual - pi_approx).
'''

import random


def pi_approx_calc(n):
    inside_count = 0
    x, y = 0.00, 0.00

    for i in range(n):

        x, y = round(random.uniform(-1, 1), 2), round(random.uniform(-1, 1), 2)

        distance = (x ** 2 + y ** 2) ** 0.5

        if distance <= 1:
            inside_count += 1

        pi_approx = (inside_count / n) * 4

    return pi_approx


n = 100
for j in range(3):
    if j == 1:
        n = 10000
    elif j == 2:
        n = 1000000

    print("n =", n)

    print(f"Approximation of pi: {pi_approx_calc(n)}")

    error = abs(pi_approx_calc(n) - 3.14159265359)

    print(f"Error: {error}\n")
