'''
Pseudo code notes

define a graph (x, y)

set start coords and limit coords

loop over choices of [up down left or right]
change current position according to direction

check if current x or y is beyond the limit coords
if true add 1 to dead
    continue loop to next sailor/index
else keep looping

if its taken enough steps, continue loop
'''

import random


plank_size = int(input("Enter size: "))
steps = int(input("Enter the number of steps: "))
sailors = int(input("Enter the number of sailors: "))

dead_sailors = 0

x_min, x_max, y_min, y_max = -plank_size, plank_size, -plank_size, plank_size

for i in range(sailors):

    x, y = 0, 0

    for j in range(0, steps):
        step_dir = random.choice(['up', 'down', 'left', 'right'])

        match step_dir:
            case 'up':
                y += 1

            case 'down':
                y -= 1

            case 'left':
                x -= 1

            case 'right':
                x += 1

        if x < x_min or x > x_max or y < y_min or y > y_max:
            dead_sailors += 1
            break

print(f"Out of {sailors} drunk sailors, {dead_sailors}" +
      f"({round((dead_sailors / sailors)*100, 2)}%) fell into the water.")
