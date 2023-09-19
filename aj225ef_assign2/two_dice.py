
# loop over and generate dice
# loop again counting number of occurences
    # add to a tuple, number, frequency
    # print list sorted by frequency???

# sort_tuples = [(3, 7), (2, 12), (5, 10), (9, 0)]
# sort_tuples.sort(key=lambda x: x[1])

import random
n = []

for i in range(1,10000):
    n.append(random.randint(1,7)+random.randint(1,7))


for j in range(2,13): 
    count = n.count(n[j])
    print(j,count)
