
n = int(input("Enter a large positive integer: "))

zero=0
odd=0
even=0

crr=0
while n>0:
    crr = int(n%10)
    n = int(n/10)

    if crr==0:
        zero+=1
    elif crr%2==0:
        even+=1
    elif crr%2==1:
        odd+=1

print(f"\nZero: {zero} \nOdd: {odd} \nEven: {even}")
