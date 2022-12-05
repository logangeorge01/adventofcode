

a = []
c = 0
with open('input.txt') as f:
   for l in f:
      x = [[int(c) for c in b.split('-')] for b in l.split(',')]
      if (x[1][0] >= x[0][0] and x[1][1] <= x[0][1]) or (x[0][0] >= x[1][0] and x[0][1] <= x[1][1]):
         c += 1

print(c)



   


