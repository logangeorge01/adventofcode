

a = [0 for _ in range(12)]
arr = []

with open('input.txt') as f:
   for l in f:
      arr.append(l[:-1])
      for i in range(12):
         a[i] += int(l[i])

print(len(arr))

print(a)

print('\n\n\n\n')


for l in arr:
   for c in l:
      print(c, end='\t')
   print()


print('\n\n\n\n')


for i in range(12):
   m = '0' if a[i] > 500 else '1'
   print(m)
   if len(arr) == 1:
      print(int(arr[0], 2))
      break
   newarr = []
   for l in arr:
      if l[i] == m:
         newarr.append(l)
   arr = newarr




print('\n\n\n\n\n\n\n\n\n')

def get_rating(data, pos, val_for_more_ones):
   if len(data) == 1:
       return data
   other_val = list({"0", "1"}.difference({val_for_more_ones}))[0]
   pos = pos % len(data[0])
   bits_in_pos = [line[pos] for line in data]
   if bits_in_pos.count("1") >= bits_in_pos.count("0"):
       new_data = [line for line in data if line[pos] == val_for_more_ones]
   else:
       new_data = [line for line in data if line[pos] == other_val]
   return get_rating(new_data, pos + 1, val_for_more_ones)

def run_part_2(data):
   ox = int(get_rating(data, 0, "1")[0], 2)
   co2 = int(get_rating(data, 0, "0")[0], 2)
   print(ox, co2)
   return ox * co2

print(run_part_2(arr))




print('\n\n\n\n\n\n')






with open('input.txt') as f:
    nums = [l.strip() for l in f.readlines()]
digits = list(zip(*nums))
gamma = ''.join([max(set(d), key=d.count) for d in digits])
epsilon = ''.join(['1' if c == '0' else '0' for c in gamma])
print('Power consumption: ', end='')
print(int(gamma, 2)*int(epsilon, 2))

def find_rating(lines, keep_fn):
   digit = 0
   width = len(lines[0])
   while len(lines)>1:
      ones = sum([1 for line in lines if line[digit] == '1'])
      keep_chr = keep_fn(len(lines)-ones, ones)
      lines = [l for l in lines if l[digit] == keep_chr]
      digit +=1
   return int(lines[0],2)
oxy = find_rating(nums, lambda zeroes, ones: '1' if ones >= zeroes else '0')
co2 = find_rating(nums, lambda zeroes, ones: '0' if zeroes <= ones else '1')
print(oxy, co2)
print('Life support rating: ', end='')
print(oxy*co2)



print('\n\n\n\n\n\n')






from collections import Counter

ll = [x for x in open('input.txt').read().strip().split('\n')]

theta = ''
epsilon = ''
for i in range(len(ll[0])):
	common = Counter([x[i] for x in ll])

	if common['0'] > common['1']:
		ll = [x for x in ll if x[i] == '0']
	else:
		ll = [x for x in ll if x[i] == '1']
	theta = ll[0]

ll = [x for x in open('input.txt').read().strip().split('\n')]
for i in range(len(ll[0])):
	common = Counter([x[i] for x in ll])

	if common['0'] > common['1']:
		ll = [x for x in ll if x[i] == '1']
	else:
		ll = [x for x in ll if x[i] == '0']
	if ll:
		epsilon = ll[0]

print(int(theta,2),int(epsilon,2))
print(int(theta,2)*int(epsilon,2))








