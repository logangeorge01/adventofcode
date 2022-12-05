

a = []

with open('input.txt') as f:
   for l in f:
      a.append(l)

al = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

c = 0
for i in range(len(a)):
   if i % 3 == 2:
      for j in a[i]:
         if j in a[i-1] and j in a[i-2]:
            c += al.index(j) + 1
            break

print(c)

