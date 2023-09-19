print("Please provide three integers A,B,C. ")

s1 = input("Enter A: ")
s2 = input("Enter B: ")
s3 = input("Enter C: ")

if s1>s2 and  s1>s3:
    print("The largest number is:", s1)
elif s2>s1 and s2>s3:
    print("The largest number is:", s2)
elif s3>s1 and s3>s2:
    print("The largest number is:", s3)

