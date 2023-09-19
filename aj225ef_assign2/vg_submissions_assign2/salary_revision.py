
salaries = [21700, 28200, 26300, 25100, 22600, 22800, 19900]

salaries.sort()

# besides using the median function i could have
# checked the length if its even or odd
# if odd, return the middle value
# if even, return the middle values added together and divided by 2.
# Getting them by dividing the length by 2 rounding it with ceiling()
#
# and getting the value next to it with taking the same value -1


if len(salaries) % 2 == 0:
    mid_val1 = salaries[(int(len(salaries) / 2))]
    mid_val2 = salaries[int((len(salaries) / 2) + 1)]

    median = mid_val1 + mid_val2

    print(int(median / 2))
else:
    print(salaries[round(len(salaries) / 2)])


# or to make it easier:
#
# from statistics import median
# print("Median:", median(salaries))

# add together every value in the list together
s = sum(salaries)

print("Average:", round(s/len(salaries)))

# Round the result of subtracting the max and min value in the list
print("Gap:", round(max(salaries)-min(salaries)))
