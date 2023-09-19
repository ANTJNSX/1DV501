import random

ans = random.randint(1,100)
count=0

while True:
    count+=1
    try:
        n = int(input(f'Guess {count}: '))
        if n==ans:
            print(f'The answer was {ans}')
            break
        elif n>ans:
            print("Clue: lower")
        else:
            print("Clue: higher")
   
    except ValueError:
       print("Error enter a positive number between 1-100")
