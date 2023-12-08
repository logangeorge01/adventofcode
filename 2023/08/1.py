

a = {}
lr = ''

with open('input.txt') as f:
   lr = f.readline().strip()
   f.readline()
   for l in f:
      a[l[:3]] = (l[7:10], l[12:15])

lr *= 100

e = 'AAA'

i = 0
while True:
   if e == 'ZZZ':
      break
   if lr[i] == 'L':
      e = a[e][0]
   else:
      e = a[e][1]
   i += 1

print(i)


