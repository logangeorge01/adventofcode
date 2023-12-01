


data = []
ix = []
with open('input.txt') as f:
   for l in f:
      if l == '\n':
         continue
      if l[0] == 'f':
         n = int(l.split('=')[1])
         if l.split('=')[0][-1:] == 'x':
            n *= -1
         ix.append(n)
         continue
      data.append(list(reversed([int(x) for x in l.strip().split(',')])))


for i in range(len(ix)):
   xy = 1 if ix[i] < 0 else 0
   v = abs(ix[i])
   for j in range(len(data)):
      if data[j][xy] > v:
         data[j][xy] = v - (data[j][xy] - v)


g = [[' '] * 39 for _ in range(6)]
for i in data:
   g[i[0]][i[1]] = '|'
print()
for r in g:
   print(''.join(r))
print()

   


