

a = []

with open('input.txt') as f:
   for l in f:
      a.append(l)

s = 0
for l in a:
    rm = 0
    gm = 0
    bm = 0
    for i in range(len(l)-2):
        prev = ''
        if l[i] == ' ' and l[i+1] == 'r':
            prev += l[i-1]
            if l[i-2].isdigit():
                prev = l[i-2] + prev
            rm = max(rm, int(prev))
        prev = ''
        if l[i] == ' ' and l[i+1] == 'g':
            prev += l[i-1]
            if l[i-2].isdigit():
                prev = l[i-2] + prev
            gm = max(gm, int(prev))
        prev = ''
        if l[i] == ' ' and l[i+1] == 'b':
            prev += l[i-1]
            if l[i-2].isdigit():
                prev = l[i-2] + prev
            bm = max(bm, int(prev))

    s += rm * gm * bm

print(s)
    
