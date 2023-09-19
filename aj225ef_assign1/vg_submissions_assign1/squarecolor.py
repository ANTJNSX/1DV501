space = input("Enter a chess square identifier (e.g. e5): ")

if not ord(space[0]) % 2:

    if int(space[1]) % 2:
        print(space,"is white")
    else: 
        print(space,"is black")

else:
    
    if int(space[1]) % 2:
        print(space,"is black")
    else:
        print(space,"is white")

