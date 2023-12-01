

data = []
c = 0
with open('input.txt') as f:
   for l in f:
      for n in l.strip().split('| ')[1].split():
         if len(n) in [2, 3, 4, 7]:
            c += 1
      
print(c)





