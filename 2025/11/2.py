from collections import defaultdict
from functools import lru_cache

d = defaultdict(list)

with open('input.txt') as f:
    for l in f:
        ll = l.strip().split(' ')
        d[ll[0][:-1]] += ll[1:]

@lru_cache(maxsize=None)
def recur(key, dac, fft):
    if key == 'out': return 1 if dac and fft else 0
    return sum([recur(k, dac or key=='dac', fft or key=='fft') for k in d[key]])

print(recur('svr', False, False))

