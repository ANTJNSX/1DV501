l = []

while True:
    n = int(input("Integer: "))
    if n<0:
        break 
    l.append(n)

print("\nNumber of positive integers:", len(l))
print("Positive numbers:",l)
