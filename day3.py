import collections
import itertools

with open("inputs/day3") as data:
  f = data.readlines()
  data = [i.strip() for i in f]

def get_counter(input_data):
  bit_locations = list(map(str,range(len(input_data[0]))))
  mapped = [map(''.join,list((zip(bit_locations, map(str,i))))) for i in input_data]
  full_list = list(itertools.chain(*mapped)) # every element is a bit location from left + that bit's value
  return collections.Counter(full_list)
counter = get_counter(data)

# part 1
final_most_common = ""
final_most_uncommon = ""
for k in range(len(data[0])):
  is_more_zeros = counter[str(k)+'0'] > counter[str(k)+'1']
  final_most_common += '0' if is_more_zeros else '1'
  final_most_uncommon += '1' if is_more_zeros else '0'
print("Power consumption =", int(final_most_common, 2) * int(final_most_uncommon, 2))

#part 2
oxy = data[:]
scrubber = data[:]

for k in range(len(data[0])):
  if len(oxy) > 1:
    counter = get_counter(oxy)
    if counter[str(k)+'0'] > counter[str(k)+'1']:
      oxy=list(filter(lambda x: x[k]=="0", oxy))
    else:
      oxy=list(filter(lambda x: x[k]=="1", oxy))
  if len(scrubber) > 1:
    counter = get_counter(scrubber)
    if counter[str(k)+'0'] > counter[str(k)+'1']:
      scrubber=list(filter(lambda x: x[k]=="1", scrubber))
    else:
      scrubber=list(filter(lambda x: x[k]=="0", scrubber)) 


print("Life support rating =", int(scrubber[0],2)*int(oxy[0],2))