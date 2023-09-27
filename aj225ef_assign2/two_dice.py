
# loop over and generate dice
# loop again counting number of occurences
# print dice val and frequency

import random

n = []

for i in range(1, 10000):
    n.append(random.randint(1, 7)+random.randint(1, 7))


for j in range(2, 13):
    count = n.count(n[j])
    print(j, count)
