

data = []
with open('input.txt') as f:
   for l in f:
      data.append(l.strip())
      
t = {')': 3, ']': 57, '}': 1197, '>': 25137}
d = {')': '(', '}': '{', ']': '[', '>': '<'}
ans = 0

for l in data:
   s = ''
   for c in l:
      if c not in d:
         s += c
      elif s[-1] == d[c]:
         s = s[:-1]
      else:
         ans += t[c]
         break

print(ans)


