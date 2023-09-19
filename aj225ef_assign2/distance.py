import math

def distance(x1, y1, x2, y2):
    return math.sqrt( ((x1-x2)**2) + ((y1-y2)**2) )


xinp1 = int(input("Enter x1: "))
yinp1 = int(input("Enter y1: "))
xinp2 = int(input("Enter x2: "))
yinp2 = int(input("Enter y2: "))


print(round(distance(xinp1, yinp1, xinp2, yinp2), 3))
