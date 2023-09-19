s = int(input("Give a number of seconds:"))

s = s%(24 * 3600)
h = s//3600
s %= 3600
m = s//60
s %= 60

print("This corresponds to:",h,"hours,",m,"minutes and",s)
