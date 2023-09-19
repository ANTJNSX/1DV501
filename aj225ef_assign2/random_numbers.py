import random

n = int(input("input amount of random numbers: "))

lst = []
sum = 0

while n > len(lst):
    rand = random.randint(1,100)
    lst.append(rand)
    sum+=rand

min = min(lst) 
max = max(lst) 

avr = rand/len(lst)

print("\nGenerated values:", *lst)
print("Average, min, and max are",avr,min,max)
