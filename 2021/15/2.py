import heapq


data = []
le = 0
#produce 5x5 subsections of original input
for _ in range(5):
   with open('input.txt') as f:
      for l in f:
         le = len(l.strip())
         data.append([int(x) for x in l.strip()] * 5)

#increment and roll over 9->1
for i in range(len(data)):
   for j in range(len(data[0])):
      data[i][j] += (i // le) + (j // le)
      data[i][j] = (data[i][j] // 10) + (data[i][j] % 10)

#use 10000 as infinity to represent not having touched
g = [[10000] * len(data[0]) for _ in range(len(data))]
g[0][0] = 0

#optimization by factor of ~2 - only consider middle 2 diagonal subsections of size le^2
c = 0
for i in range(len(data)):
   for j in range(len(data[0])):
      if abs((i // le) - (j // le)) >= 2:
         g[i][j] = 10001
         c += 1

#dictionary {(x, y): curMinCost, ...}
# and heap [(curMinCost, (x, y)), ...]
dd = {(0, 0): 0}
#update neighbor with new min and update corresponding val in dictionary/heap
def mark(i, j, cur):
   if 0 <= i < len(data) and 0 <= j < len(data[0]) and g[i][j] < 10001:
      g[i][j] = min(g[i][j], cur + data[i][j])
      dd[(i, j)] = g[i][j]

while True:
   #pop min from heap (have to convert from dict to heap and back after)
   dd = [tuple(reversed(x)) for x in dd.items()]
   heapq.heapify(dd)
   i, j = heapq.heappop(dd)[1]
   dd = {x[1]: x[0] for x in dd}

   #reached bottom right
   if i == len(data)-1 and j == len(data[0])-1:
      print(g[i][j])
      break

   curv = g[i][j]
   #no longer need visited value in graph, set to 10001 (meaning visited) to prevent adding back to heap as neighbor
   g[i][j] = 10001
   c += 1
   gg = 100 * c / (len(data) * len(data[0]))
   if gg%1 == 0: print(f'{int(gg)}%')

   mark(i-1, j, curv)
   mark(i+1, j, curv)
   mark(i, j-1, curv)
   mark(i, j+1, curv)



