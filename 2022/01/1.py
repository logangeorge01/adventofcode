

a = []

with open('input.txt') as f:
   for l in f:
      a.append(l)

m = 0
c = 0
for n in a:
   if n == '\n':
      m = max(m, c)
      c = 0
      continue
   c += int(n)

print(m)

