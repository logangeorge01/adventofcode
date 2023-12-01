

a = []

inp = ['RNFVLJSM', 'PNDZFJWH', 'WRCDG', 'NBS', 'MZWPCBFN', 'PRMW', 'RTNGLSW', 'QTHPNBV', 'LMHZNF']

with open('input.txt') as f:
   for l in f:
      x = l.split(' ')
      a.append((int(x[1]), int(x[3]), int(x[5])))

for n in a:
   inp[n[2]-1] += inp[n[1]-1][-n[0]:][::-1]
   inp[n[1]-1] = inp[n[1]-1][:-n[0]]

print(''.join([x[-1] for x in inp]))

