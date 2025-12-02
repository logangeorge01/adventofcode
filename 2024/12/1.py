# from collections import defaultdict

a = []

with open('input.txt') as f:
    for l in f:
        a.append([x for x in l.strip()])

# print(a)
# print(a[0][0])

# area = defaultdict(int)
# per = defaultdict(int)

r = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# per, area
def cal(i, j, l):
    # print(i, j, l)
    if i == -1 or i == len(a) or j == -1 or j == len(a[0]) or a[i][j].upper() != l:
        return (1, 0)
    if a[i][j].islower():
        return (0, 0)
    # print(a)
    a[i][j] = a[i][j].lower()
    t = [cal(i + rr[0], j + rr[1], l) for rr in r]
    # return sum([cal(i + rr[0], j + rr[1], l) for rr in r])

    return (sum([x[0] for x in t]), sum([x[1] for x in t]) + 1)

s = 0
aa = len(a)
bb = len(a[0])
# aa = 1
# bb = 1
for i in range(aa):
    for j in range(bb):
        # area[a[i][j]] += 1
        # print(i, j)
        # print(a[i])
        # print('here')
        re = cal(i, j, a[i][j])
        # print()
        s += re[0] * re[1]
        # print(re, s, i, j, a[i][j])
        # print(a[i][j], p, a)

print(s)

# print(area)
# print(per)

# s = 0
# for key, value in area.items():
    # s += value * per[key]

# print(s)



# 
