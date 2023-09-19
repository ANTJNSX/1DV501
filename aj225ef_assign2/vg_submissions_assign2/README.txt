
abcd.py:
This program is very simple, i looped through each one of a, b, c, and d 9 times to get 1-9 values.
and each loop it checks the char sum of the values to that sum times 4, and if they are even, return those numbers for a, b, c and d.


drunken_sailor.py:
This program is a bit more complicated, it starts with defining a 2d graph that will be used to track the sailors location.
then the inputs will determine the amount of sailors, the size of the graph(plank) and the amount of steps they will take.

Then the main loop will start and it will loop over every sailor and inside that it will loop over every step each one will take,
for every step a random direction is chosen and the sailor will walk into that direction, effecting the x or y direction. 
After every step it will check their palce on the graph(plank) and then see if they are out of the graphs(planks) bounds or not.
if so then the sailor is dead and will be counted for within the amount of sailors that died, after being counted the loop will then
continue the next sailor. If a sailor survives the loop will simply continue to the next one.

Then after all the sailors have gone we print out he results of the procentages of sailors that died and the amount that survived.

All it was was to loop through an amount and see if after a certain amount of steps if they went out of bounds or not and then 
keep track of how many fell, then printing out the resulting data.


pi_approx.py:
This one was also pretty tricky, the basic idea is to calculate an approximation of pi using coordinates and its distance to the origin.
then if this distance falls below or equal to 1, then the point is inside the unit circle. If it does fall out of the unit circles bounds
then we dont count it into the approximation. In the end it will give an approximation of pi with 3 different amounts the random numbers used,
ranging from 100 to 1_000_000.

To solve this one i needed quite a bit of explaining of how it actually worked,
but in the end i kind of understood it wrote a working but possibly unoptimized answer.


salary_revision.py:
This one was very easy, i needed to return three statistics from a salary list. 

1. Median, there is a library for it but the self calculating method is just to return the middle value of the sorted list, or if its even
    return the sum of the two middle values.

2. Average, just add the values together with a loop or with the sum() function and then print that value divided by the length of the list

3. Gap, or more specifically the gap between the max and the min values of the list.
