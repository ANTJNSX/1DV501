
inp = int(input("Enter a positive integer: "))
res1 = []
res2 = []

for i in range(0,inp):
    if i % 2:
        res1.append(i)

print("Odd numbers using for:", *res1)

j=0
while j in range(0,inp):
    if j % 2:
        res2.append(j)
    j+=1

print("Odd numbers using while:", *res2)
