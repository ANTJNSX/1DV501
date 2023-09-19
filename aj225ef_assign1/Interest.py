s = int(input("Initial savings: "))
r = int(input("Interest rate (in percentages): "))
y = int(input("Number of years: "))

s = s*(1+(r/100))**y

print("The value of your savings after", y, "years is: ", round(s))
