

data = []
with open('input.txt') as f:
   for l in f:
      data.append(l.strip())


nums = [int(x) for x in data[0].split(',')]
data = data[2:]

bingo = []
cur = []
for l in data:
   if len(cur) == 5:
      bingo.append(cur)
      cur = []
      continue
   cur.append([int(i) for i in l.split()])
bingo.append(cur)

WIN = [-1, -1, -1, -1, -1]

for n in nums:
   for bind in range(len(bingo)):
      b = bingo[bind]
      for i in range(5):
         bingo[bind][i] = [(x if x != n else -1) for x in b[i]]

      found = False
      for i in range(5):
         found |= (b[i] == WIN) or ([x[i] for x in b] == WIN)

      if found:
         ans = 0
         for r in b:
            for c in r:
               ans += max(0, c)
         ans *= n
         print(ans)
         exit()

