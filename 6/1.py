

data = []
with open('input.txt') as f:
   for l in f:
      data = [int(x) for x in l.split(',')]

for n in range(80):
   for i in range(len(data)):
      if data[i] == 0:
         data[i] = 6
         data.append(8)
      else:
         data[i] -= 1

print(len(data))



