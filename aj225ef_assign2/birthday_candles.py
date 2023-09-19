
# loop over age 
    # see if age is less than amount of candles already have 
    # if u need more than one box, add more to box and add 24+ to the candles already have
    # remove age from candle amount

age=100 
boxes=0 
candles=0
maxboxes=0
for i in range(1,age+1):
    boxes=0
    while i>candles:
        boxes+=1
        maxboxes+=1
        candles+=24
    candles-=i

    print(f"Before birthday {i}, buy {boxes} box(es), you have {candles} candles")

print(f"\nTotal number of boxes: {maxboxes}, Remaining candles: {candles}")
