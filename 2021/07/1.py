

data = []
with open('input.txt') as f:
   for l in f:
      data = [int(x) for x in l.split(',')]


data.sort()

med = data[(len(data) // 2)]

print(med)

s = 0
for n in data:
   s += abs(n - med)

print(s)




