

data = []
with open('input.txt') as f:
   for l in f:
      data = [int(x) for x in l.split(',')]

import math
mean = math.floor(sum(data) / len(data))

s = 0
for n in data:
   a = abs(mean - n)
   s += (a * (a + 1) // 2)

print(s)


