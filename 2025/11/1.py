from collections import defaultdict

d = defaultdict(list)

with open('input.txt') as f:
    for l in f:
        ll = l.strip().split(' ')
        d[ll[0][:-1]] += ll[1:]

def recur(key):
    if key == 'out': return 1
    return sum([recur(k) for k in d[key]])

print(recur('you'))

