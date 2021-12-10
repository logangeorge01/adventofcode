

data = []
with open('input.txt') as f:
   for l in f:
      data.append(l.strip())
      
t = ['(', '[', '{', '<']
tl = lambda x: t.index(x) + 1

d = {')': '(', '}': '{', ']': '[', '>': '<'}
ans = []

for l in data:
   s = ''
   for c in l:
      if c not in d:
         s += c
      elif s[-1] == d[c]:
         s = s[:-1]
      else:
         s = '$'
         break
   if s == '$':
      continue
   cl = 0
   for i in range(len(s) - 1, -1, -1):
      cl *= 5
      cl += tl(s[i])
   ans.append(cl)

ans.sort()
print(ans[len(ans)//2])


