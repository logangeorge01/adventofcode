


data = []
with open('input.txt') as f:
   for l in f:
      data.append([int(x) for x in l.strip()])


g = [[10000] * len(data[0]) for _ in range(len(data))]
g[0][0] = 0

def mark(i, j, cur):
   if 0 <= i < len(data) and 0 <= j < len(data[0]) and g[i][j] < 10001:
      g[i][j] = min(g[i][j], cur + data[i][j])

c = 0
while True:
   i, j = 0, 0
   for x in range(len(data)):
      for y in range(len(data[0])):
         if data[x][y] < 10000 and g[x][y] < g[i][j]:
            i, j = x, y


   if i == len(data)-1 and j == len(data[0])-1:
      print(g[i][j])
      break

   curv = g[i][j]
   g[i][j] = 10001
   c += 1
   gg = 100 * c / (len(data) * len(data[0]))
   if gg % 5 == 0:
      print(f'{int(gg)}%')

   mark(i-1, j, curv)
   mark(i+1, j, curv)
   mark(i, j-1, curv)
   mark(i, j+1, curv)




   

