
d = 0
h = 0

with open('input.txt') as f:
   for l in f:
      i = l.split()
      if i[0][0] == 'f':
         h += int(i[1])
      elif i[0][0] == 'd':
         d += int(i[1])
      else:
         d -= int(i[1])


print(d * h)


