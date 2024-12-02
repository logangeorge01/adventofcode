

a = []

def inc(n):
    for i in range(len(n) - 1):
        if not (0 < n[i+1] - n[i] < 4):
            return False
    return True
        
def dec(n):
    for i in range(len(n) - 1):
        if not (0 < n[i] - n[i+1] < 4):
            return False
    return True

with open('input.txt') as f:
    for l in f:
        a.append([int(x) for x in l.split()])

s = 0
for n in a:
    if inc(n) or dec(n):
        s += 1

print(s)
        

