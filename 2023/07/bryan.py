

a = []

with open('input1.txt') as f:
   for l in f:
      a.append(l.strip().split(' '))

s = [[0x0, 0] for n in range(len(a))]

def checkHand(h):
   mout = 0x100000
   for i in range(len(h)):
      m = h.replace('1', h[i])
      if m.count(m[i]) == 5:
         mout = max(mout, 0x700000)
      if m.count(m[i]) == 4:
         mout = max(mout, 0x600000)
      if m.count(m[i]) == 3:
         for j in range(len(m)):
            if m[j] != m[i] and m.count(m[j]) == 2:
               mout = max(mout, 0x500000)
         mout = max(mout, 0x400000)
   for i in range(len(h)):
      m = h.replace('1', h[i])
      if m.count(m[i]) == 2:
         for j in range(len(m)):
            if m[j] != m[i] and m.count(m[j]) == 2:
               mout = max(mout, 0x300000)
   for i in range(len(h)):
      m = h.replace('1', h[i])
      if m.count(m[i]) == 2:
         mout = max(mout, 0x200000)
   return mout
   

for i in range(len(a)):
   h = a[i][0].replace('T', 'a').replace('J', '1').replace('Q', 'c').replace('K', 'd').replace('A', 'e')
   s[i][1] = i
   s[i][0] += checkHand(h)
   s[i][0] += int(h[0], 16) * 0x10000
   s[i][0] += int(h[1], 16) * 0x1000
   s[i][0] += int(h[2], 16) * 0x100
   s[i][0] += int(h[3], 16) * 0x10
   s[i][0] += int(h[4], 16)

s.sort(key=lambda x: x[0])

#added this
for x in s:
   print(a[x[1]])

c = 0
for i in range(len(s)):
   c += (i + 1) * int(a[s[i][1]][1])

print(c)

