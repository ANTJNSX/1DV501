i = int(input("please provide monthly income: "))
lt = 38000*0.30

if i<38000:
    print("Corresponding income tax:",lt)
elif i<50000:
    print("Corresponding income tax:",lt+(i-38000)*0.35)
elif i>50000:
    print("Corresponding income tax:", (lt+(50000-38000)*0.35)+(i-50000)*0.40)
