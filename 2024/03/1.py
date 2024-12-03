import re

reg = r"mul\(\d+,\d+\)"

a = ''

with open('input.txt') as f:
    for l in f:
        a += l

m = re.findall(reg, a)

s = 0
for n in m:
    i1 = int(n.split('(')[1].split(',')[0])
    i2 = int(n.split(',')[1].split(')')[0])
    s += i1 * i2

print(s)
