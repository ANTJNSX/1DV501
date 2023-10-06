
def nr_triangle(length):
    if length > 9:
        print("Error: Input above set limit")
        return False

    number = "1"
    spaces = length*2

    for i in range(length):
        print(spaces*" " + number)
        spaces -= 2
        number += " " + str(i+2)


length = int(input("Number of rows in the triangle in range 1-9: "))
nr_triangle(length)
