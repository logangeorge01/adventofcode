
s = set()

with open('input.txt') as f:
    for l in f:
        ll = l.strip()
        if ll == '': continue
        if '-' in ll:
            t = tuple([int(i) for i in ll.split('-')])
            for _ in range(2):
                for tt in s:
                    if tt[0] <= t[1] and t[0] <= tt[1]:
                        t = (min(t[0], tt[0]), max(t[1], tt[1]))
                        s.remove(tt)
                        break
            s.add(t)

print(sum(map(lambda x: x[1]-x[0]+1, s)))

