

a = []

with open('input2.txt') as f:
   for l in f:
      a.append(l)

s = 0
for l in a:
    c1 = ''
    c2 = ''
    for i in range(len(l)):
        if l[i].isdigit():
            c1 = l[i]
            break
    for i in range(len(l)-1, -1, -1):
        if l[i].isdigit():
            c2 = l[i]
            break

    c = c1 + c2
    print(c1, c2, c)
    s += int(c)

print(s)

