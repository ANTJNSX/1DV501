import random

n =[]

print("The Lotto numbers this week:")

for i in range(1,8):

    s=random.randint(1,35)
    while s in n:
        s=random.randint(1,35)

    n.append(s)

n.sort()
print(*n)
