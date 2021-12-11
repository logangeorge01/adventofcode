

data = []
with open('input.txt') as f:
   for l in f:
      data.append([int(x) for x in l.strip()])


def low(i, j, h):
   return not (0 <= i < len(data)) or not (0 <= j < len(data[0])) or h < data[i][j]

s = 0

for i in range(len(data)):
   for j in range(len(data[0])):
      h = data[i][j]
      if low(i, j-1, h) and low(i, j+1, h) and low(i-1, j, h) and low(i+1, j, h):
         s += h + 1

print(s)


