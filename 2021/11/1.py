

data = []
with open('input.txt') as f:
   for l in f:
      data.append([int(x) for x in l.strip()])

def inb(i, j):
   return 0 <= i < len(data) and 0 <= j < len(data[0])

flashes = 0
def flash(x, y):
   global flashes
   flashes += 1

   data[x][y] = 1000

   for i in range(-1, 2):
      for j in range(-1, 2):
         if not (i == 0 and j == 0) and inb(x+i, y+j):
            data[x+i][y+j] += 1
            if 10 <= data[x+i][y+j] < 1000:
               flash(x+i, y+j)


for x in range(100):
   for i in range(len(data)):
      for j in range(len(data[0])):
         data[i][j] += 1
         if 10 <= data[i][j] < 1000:
            flash(i, j)

   for i in range(len(data)):
      for j in range(len(data[0])):
         if data[i][j] >= 1000:
            data[i][j] = 0


print(flashes)


