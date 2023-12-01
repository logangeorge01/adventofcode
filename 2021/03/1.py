

a = [[0, 0] for _ in range(12)]

with open('input.txt') as f:
   for l in f:
      for i in range(12):
         a[i][int(l[i])] += 1

n = ''
for i in range(12):
   n += (str(a[i].index(max(a[i]))))


print(n)

# print(int(n, 2) * (~(int(n, 2) & 0xFF)))


