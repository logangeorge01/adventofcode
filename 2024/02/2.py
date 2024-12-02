


def test(n, inc, skipped = False):
    for i in range(len(n) - 1):
        diff = n[i + 1] - n[i] if inc else n[i] - n[i + 1]
        if not (0 < diff < 4):
            if skipped:
                return False
            n1 = n[:i] + n[i + 1:]
            n2 = n[:i + 1] + n[i + 2:]
            return test(n1, inc, True) or test(n2, inc, True)
    return True

a = []
with open('input.txt') as f:
    for l in f:
        a.append([int(x) for x in l.split()])

s = 0
for n in a:
    if test(n, True) or test(n, False):
        s += 1

print(s)


