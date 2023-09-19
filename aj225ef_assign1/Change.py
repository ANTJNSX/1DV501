price = round(float(input("Price: ")))
payment = int(input("Payment: "))
change = payment-price 

tusenlapp,femhlapp,tvahlapp,hlapp,femtiolapp,tjugolapp,tiokr,femkr,tvakr,enkr = 0,0,0,0,0,0,0,0,0,0

print("\nChange", change)
while change>0:
    if change>1000:
        change-=1000
        tusenlapp+=1
    elif change>500: 
        change-=500
        femhlapp+=1
    elif change>200:
        change-=200
        tvahlapp+=1
    elif change>100:
        change-=100
        hlapp+=1
    elif change>50:
        change-=50
        femtiolapp+=1
    elif change>20:
        change-=20
        tjugolapp+=1
    elif change>10:
        change-=10
        tiokr+=1
    elif change>5:
        change-=5
        femkr+=1
    elif change>2:
        change-=2
        tvakr+=1
    elif change==1:
        change-=1
        enkr+=1
    if change == 0:
        break


print("1000kr bills: ", tusenlapp)
print("500kr bills: ", femhlapp)
print("200kr bills: ", tvahlapp)
print("100kr bills: ", hlapp)
print("50kr bills: ", femtiolapp)
print("20kr bills: ", tjugolapp)
print("10kr bills: ", tiokr)
print("5kr bills: ", femkr)
print("2kr bills: ", tvakr)
print("1kr bills: ", enkr)
