import collections
import numpy as np

with open("inputs/day8") as data:
  f = data.readlines()
  data = list(map(lambda x: x.split(' | '), f))

count = 0
count1 = 0

all_possible = set("abcdefg")
for i in data:
  actual_numbers = {}

  inp = np.array(i[0].strip().split(' '))
  output = i[1].strip().split(' ')

  mappings = collections.defaultdict(str)
  len_arr = np.array([len(k) for k in inp])
  actual_numbers[1] = inp[len_arr == 2][0]
  actual_numbers[4] = inp[len_arr == 4][0]
  actual_numbers[7] = inp[len_arr == 3][0]
  actual_numbers[8] = inp[len_arr == 7][0]

  six_nine_zero = np.unique(inp[len_arr==6])

  for number in six_nine_zero:
    if set(actual_numbers[4]).issubset(set(number)): # number is 9
      actual_numbers[9]=number
      break

  e = (set(actual_numbers[9]) ^ all_possible).pop()

  zero_six = six_nine_zero[six_nine_zero != actual_numbers[9]]

  for number in zero_six:
    if set(actual_numbers[1]).issubset(set(number)): # number is zero
      de = set(actual_numbers[9]) ^ set(number)

  de.remove(e)
  d = de.pop()

  actual_numbers[6] = next(filter(lambda x: d in x, zero_six))
  actual_numbers[0] = zero_six[zero_six != actual_numbers[6]][0]
  
  c = (set(actual_numbers[6]) ^ all_possible).pop()

  two_three_five = np.unique(inp[len_arr==5])
  actual_numbers[2] = next(filter(lambda x: e in x, two_three_five))
  three_five = two_three_five[two_three_five != actual_numbers[2]]
  actual_numbers[3] = next(filter(lambda x: c in x, three_five))
  actual_numbers[5] = three_five[three_five != actual_numbers[3]][0]

  final_str = ""

  for u in output:
    for key, value in actual_numbers.items():
      if set(value) == set(u):
        final_str += str(key)
        
  count += int(final_str)
  finding_nums = [4, 2, 7, 3]
  for u in output:
    if len(u) in finding_nums:
        count1 += 1

print("Part 1:", count1)
print("Part 2", count)