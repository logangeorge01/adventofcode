# from collections import defaultdict

a = []

with open('input3.txt') as f:
    for l in f:
        a.append([x for x in l.strip()])

# print(a)
# print(a[0][0])

# area = defaultdict(int)
# per = defaultdict(int)
per = dict()

r = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# per, area
def cal(i, j, l):
    # print(i, j, l)
    if i == -1 or i == len(a) or j == -1 or j == len(a[0]) or a[i][j].upper() != l:
        # counted = False
        # for rr in r:
            # if (i + rr[0], j + rr[1]) in per:
                # counted = True
                # break
        ret = (0, 0)
        # if not counted:
            # print(i, j)
            # print(per)
            # ret = (1, 0)
        per[(i, j)] = 0
        return ret
    if a[i][j].islower():
        return (0, 0)
    # print(a)
    a[i][j] = a[i][j].lower()
    t = [cal(i + rr[0], j + rr[1], l) for rr in r]
    # return sum([cal(i + rr[0], j + rr[1], l) for rr in r])

    return (sum([x[0] for x in t]), sum([x[1] for x in t]) + 1)

# def cc(i, j, )

s = 0
# aa = len(a)
# bb = len(a[0])
aa = 1
bb = 1
for i in range(aa):
    for j in range(bb):
        # print(a[i][j])
        per = dict()
        # area[a[i][j]] += 1
        # print(i, j)
        # print(a[i])
        # print('here')
        re = cal(i, j, a[i][j])

        perr = 0
        for xx, vall in per.items():
            if vall == 0:
                print(xx)
                perr += 1
            for rr in r:
                nnx = xx[0] + rr[0]
                nny = xx[1] + rr[1]
                while (nnx, nny) in per:
                    per[(nnx, nny)] = 1
                    nnx += rr[0]
                    nny += rr[1]
            # print(per)
                    

            # if xx[2] == 0:
                # perr += 1
                # print(xx)
            # ad = True
            # for rr in r:
                # if (xx[0] + rr[0], xx[1] + rr[1]) in per:
                    # ad = False
                    # break
            # if ad:
                # perr += 1
                # print(xx)
        print('perr: ', perr, 'area: ', re[1])

        # print()
        # print(re[0], re[1])
        # print()
        # s += re[0] * re[1]
        s += perr * re[1]

        # print(re, s, i, j, a[i][j])
        # print(a[i][j], p, a)

print()
print(s)

# print(area)
# print(per)

# s = 0
# for key, value in area.items():
    # s += value * per[key]

# print(s)



# 1452678
