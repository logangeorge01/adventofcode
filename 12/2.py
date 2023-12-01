import collections

d = collections.defaultdict(list)
with open('input.txt') as f:
   for l in f:
      s = l.strip().split('-')
      d[s[0]].append(s[1])
      d[s[1]].append(s[0])


paths = 0
def dfs(c, p):
   if c == 'end':
      global paths
      paths += 1
      return
   for x in d[c]:
      if x == 'start':
         continue
      used = None
      for y in p.split(','):
         if y.islower() and p.count(y) == 2:
            used = y
      if not used or x.isupper() or p.count(x) == 0:
         dfs(x, f'{p},{x}')


dfs('start', 'start')

print(paths)


