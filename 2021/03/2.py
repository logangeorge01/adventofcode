

data = []
with open('input.txt') as f:
   for l in f:
      data.append(l.strip())

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

ox = int(get_rating(data, 0, "1")[0], 2)
co2 = int(get_rating(data, 0, "0")[0], 2)
print(ox * co2)

