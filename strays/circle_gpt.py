# gen by chat gpt

import math

def print_circle(radius):
    for i in range(2 * radius + 1):
        for j in range(2 * radius + 1):
            # Calculate the distance from the center of the circle
            distance = math.sqrt((i - radius)**2 + (j - radius)**2)

            # If the distance is approximately equal to the radius, print an asterisk, else print a space
            if math.isclose(distance, radius, abs_tol=0.5):
                print('*', end='')
            else:
                print(' ', end='')
        print()  # Move to the next line after each row

# Example usage
print_circle(10)

