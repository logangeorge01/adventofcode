

a = []

with open('input.txt') as f:
   for l in f:
      a.append(l)
a = a[0][:-1]

s = a[0]
for i in range(1, len(a)):
   if a[i] not in s:
      s += a[i]
      if len(s) == 14:
         print(i+1)
         break
      continue
   while a[i] in s:
      s = s[1:]
   s += a[i]



