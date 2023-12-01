

a = []

with open('input.txt') as f:
   for l in f:
      a.append((ord(l[0]) - ord('A') + 1, ord(l[2]) - ord('W')))

w = {1:3, 2:1, 3:2}

c = 0
for n in a:
   c += n[1]
   if n[0] == n[1]:
      c += 3
   elif w[n[1]] == n[0]:
      c += 6 

print(c)
   



