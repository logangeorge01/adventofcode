

data = []
with open('input.txt') as f:
   for l in f:
      data = [int(x) for x in l.split(',')]

buckets = [0] * 9

for n in data:
   buckets[n] += 1

for n in range(256):
   #print(buckets)
   #print(sum(buckets))

   z = buckets[0]
   for i in range(8):
      buckets[i] = buckets[i+1]
   buckets[6] += z
   buckets[8] = z


#print(buckets)
print(sum(buckets))
   

