

a = []

with open('input.txt') as f:
   for l in f:
      a.append(l)

s = []
c = 0
for n in a:
   if n == '\n':
      s.append(c)
      c = 0
      continue
   c += int(n)

s.sort(reverse=True)
print(sum(s[:3]))

