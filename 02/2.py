

a = []

with open('input.txt') as f:
   for l in f:
      a.append((ord(l[0]) - ord('A') + 1, ord(l[2]) - ord('W')))

w = {1:3, 2:1, 3:2}
l = {1:2, 2:3, 3:1}

c = 0
for n in a:
   c += n[1] * 3 - 3
   if n[1] == 1:
      c += w[n[0]]
   elif n[1] == 2:
      c += n[0]
   elif n[1] == 3:
      c += l[n[0]]

print(c)
   



