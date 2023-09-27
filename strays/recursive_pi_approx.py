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


def rec_pi_approx(n):
    inside_count = 0
    x, y = 0.00, 0.00

    x, y = round(random.uniform(-1, 1), 2), round(random.uniform(-1, 1), 2)

    distance = (x ** 2 + y ** 2) ** 0.5

    if distance <= 1:
        inside_count += 1

    pi_approx = (inside_count / n) * 4

    return pi_approx


def main():

    print(pi_approx_calc(10000))


if __name__ == "__main__":
    main()
