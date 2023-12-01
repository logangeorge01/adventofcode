

data = []
with open('input.txt') as f:
   for l in f:
      data.append([int(x) for x in l.strip()])


def dfs(i, j):
   if not (0 <= i < len(data)) or not (0 <= j < len(data[0])) or data[i][j] == 9:
      return 0
   data[i][j] = 9
   return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)

ans = []
for i in range(len(data)):
   for j in range(len(data[0])):
      h = data[i][j]
      if h == 9:
         continue
      data[i][j] = 9
      s = 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)
      ans.append(s)

ans = sorted(ans)[-3:]
print(ans[0]*ans[1]*ans[2])


