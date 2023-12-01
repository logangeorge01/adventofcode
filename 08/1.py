

a = []
with open('i.txt') as f:
   for l in f:
      t = []
      for m in l.strip():
         t.append(int(m))
      a.append(t)

v = [['x'] * len(a) for _ in range(len(a))]
c = 0

#this code sucks i hate myself
for i in range(1, len(a)-1):
   m = a[i][0]
   for j in range(1, len(a)-1):
      if a[i][j] > m:
         print('l', i, j, a[i][j])
         if v[i][j] == 'x':
            v[i][j] = 'v'
            c += 1
      m = max(m, a[i][j])
for i in range(1, len(a)-1):
   m = a[0][i]
   for j in range(1, len(a)-1):
      if a[i][j] > m:
         print('t', m, i, j, a[i][j])
         if v[i][j] == 'x':
            v[i][j] = 'v'
            c += 1
      m = max(m, a[i][j])
for i in range(len(a)-2, 0, -1):
   m = a[-1][i]
   for j in range(len(a)-2, 0, -1):
      if a[i][j] > m:
         print('r', i, j, a[i][j])
         if v[i][j] == 'x':
            v[i][j] = 'v'
            c += 1
      m = max(m, a[i][j])
for i in range(len(a)-2, 0, -1):
   m = a[i][-1]
   for j in range(len(a)-2, 0, -1):
      if a[i][j] > m:
         print('b', i, j, a[i][j])
         if v[i][j] == 'x':
            v[i][j] = 'v'
            c += 1
      m = max(m, a[i][j])

c += len(a) * 4 - 4
print(c)

   




