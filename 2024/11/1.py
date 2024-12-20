

a = []

with open('input.txt') as f:
    for l in f:
        a = [int(x) for x in l.strip().split()]

def re(n, c):
    if c == 25:
        return 1
    if n == 0:
        return re(1, c + 1)
    if len(str(n)) % 2 == 0:
        ll = int(str(n)[:len(str(n)) // 2])
        rr = int(str(n)[len(str(n)) // 2:])
        return re(ll, c + 1) + re(rr, c + 1)
    return re(n * 2024, c + 1)

print(sum([re(x, 0) for x in a]))
