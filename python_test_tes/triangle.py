
size = int(input("Provide a positive integer: "))
spaces, dots = size-1, 1

for i in range(size):
    print(spaces*' ' + dots*'*')
    spaces -= 1
    dots += 1
