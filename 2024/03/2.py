import re

reg = r"mul\(\d+,\d+\)"
do = r"do\(\)"
dont = r"don't\(\)"

a = ''

with open('input.txt') as f:
    for l in f:
        a += l

m = re.finditer(reg, a)
dos = re.finditer(do, a)
donts = re.finditer(dont, a)

st = []
for n in m:
    mst = n.group()
    i1 = int(mst.split('(')[1].split(',')[0])
    i2 = int(mst.split(',')[1].split(')')[0])
    st.append((n.start(), i1 * i2))

for n in dos:
    st.append((n.start(), -10001))
for n in donts:
    st.append((n.start(), -10000))

s = 0
mm = 1
for n in sorted(st):
    if n[1] == -10001:
        mm = 1
    elif n[1] == -10000:
        mm = 0
    else:
        s += n[1] * mm

print(s)
