

a = []

with open('input.txt') as f:
   for l in f:
      a.append((l[:len(l)//2], l[len(l)//2:]))

al = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

c = 0
for n in a:
   for x in n[0]:
      if x in n[1]:
         c += al.index(x) + 1
         break


print(c)

