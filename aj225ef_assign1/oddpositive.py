import random

r = random.randint(-10,10)


if r%2:
    if r>0:
        print(r,"is odd and positive")
    else:
        print(r,"is odd and negative")
else:
    if r>0:
        print(r,"is even and positive")
    else:
        print(r,"is even and negative")
