

a = []

with open('input.txt') as f:
   for l in f:
      a.append(l.strip().split(' '))

s = [[0x0, 0] for n in range(len(a))]

def checkHand(h):
   for i in range(len(h)):
      if h.count(h[i]) == 5:
         return 0x700000
      if h.count(h[i]) == 4:
         return 0x600000
      if h.count(h[i]) == 3:
         for j in range(len(h)):
            if h[j] != h[i] and h.count(h[j]) == 2:
               return 0x500000
         return 0x400000
   for i in range(len(h)):
      if h.count(h[i]) == 2:
         for j in range(len(h)):
            if h[j] != h[i] and h.count(h[j]) == 2:
               return 0x300000
   for i in range(len(h)):
      if h.count(h[i]) == 2:
         return 0x200000
   return 0x100000
   

for i in range(len(a)):
   h = a[i][0].replace('T', 'a').replace('J', 'b').replace('Q', 'c').replace('K', 'd').replace('A', 'e')
   s[i][1] = i
   s[i][0] += checkHand(h)
   s[i][0] += int(h[0], 16) * 0x10000
   s[i][0] += int(h[1], 16) * 0x1000
   s[i][0] += int(h[2], 16) * 0x100
   s[i][0] += int(h[3], 16) * 0x10
   s[i][0] += int(h[4], 16)

s.sort(key=lambda x: x[0])

c = 0
for i in range(len(s)):
   c += (i + 1) * int(a[s[i][1]][1])

print(c)



