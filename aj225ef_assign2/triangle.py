
am = int(input("Enter an odd positive integer: "))

iso=am

print("\nRight-Angled Triangle:")
count=0

while am != 0: 
    print(count*' ' + am*'*')
    count+=1
    am-=1

print("\nIsosceles Triangle:")
count=1
while iso != 0:
    print(round(iso/2)*' ' + count*'*' +  round(iso/2)*' ')
    count+=2
    iso-=2

