import functools

a = []

with open('input.txt') as f:
    for l in f:
        a = [int(x) for x in l.strip().split()]

@functools.cache
def re(n, c):
    if c == 75:
        return 1
    if n == 0:
        return re(1, c + 1)
    if len(str(n)) % 2 == 0:
        ll = re(int(str(n)[:len(str(n)) // 2]), c + 1)
        rr = re(int(str(n)[len(str(n)) // 2:]), c + 1)
        return ll + rr
    return re(n * 2024, c + 1)

print(sum([re(x, 0) for x in a]))
