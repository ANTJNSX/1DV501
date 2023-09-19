# create a circle with ascii


# 2 variables for left and right
# increase one and reduce the other 
l = 20
spL = int(l/2)
spR = int(l/2)
spM = 0

for i in range(int(l/2)):
    print(spL*' ' + '*' + spM*' ' + '*' + spR*' ')
    spL-=1
    spR-=1
    spM+=2


for j in range(int(l/2)+1):
    print(spL*' ' + '*' + spM*' ' + '*' + spR*' ')
    spL+=1
    spR+=1
    spM-=2
