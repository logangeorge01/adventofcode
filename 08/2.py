

import itertools as it


az = 'abcdefg'
p = list(it.permutations([0,1,2,3,4,5,6]))
p = [''.join([az[j] for j in i]) for i in p]
base = [[0, 1, 2, 3, 4, 6], [0, 1], [0, 2, 3, 5, 6], [0, 1, 2, 3, 5], [0, 1, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [0, 1, 3], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5]]
p = [[''.join(sorted([i[k] for k in j])) for j in base] for i in p]

a = []
data = []

c = 0
with open('input.txt') as f:
   for l in f:
      ls = [x.split() for x in l.strip().split(' | ')]

      for x in p:
         found = True
         for n in ls[0]:
            if ''.join(sorted(n)) not in x:
               found = False
               break
         if found:
            a = x
            break

      s = ''
      for n in ls[1]:
         s += str(a.index(''.join(sorted(n))))
      c += int(s)

print(c)





