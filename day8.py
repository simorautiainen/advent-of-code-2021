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

  inp = i[0].strip().split(' ')
  output = i[1].strip().split(' ')
  combined = np.array(list(map(lambda x: ''.join(sorted(x)), inp)))

  mappings = collections.defaultdict(str)
  len_arr = np.array([len(k) for k in combined])

  actual_numbers[1] = set(combined[np.where(len_arr == 2)][0])
  actual_numbers[4] = set(combined[np.where(len_arr == 4)][0])
  actual_numbers[7] = set(combined[np.where(len_arr == 3)][0])
  actual_numbers[8] = set(combined[np.where(len_arr == 7)][0])
  six_nine_zero = list(set(combined[np.where(len_arr==6)]))

  two_three_five = list(set(combined[np.where(len_arr==5)]))
  for iter in six_nine_zero:
    is_legit = True
    for char in actual_numbers[4]:
      if not char in iter:
        is_legit = False
        break
    if is_legit:
      actual_numbers[9]=set(iter)
      break
  e = list(actual_numbers[9] ^ all_possible)[0]

  a= list(actual_numbers[1] ^ actual_numbers[7])[0]
  zero_six = list(filter(lambda x: not actual_numbers[9] == set(x), six_nine_zero))
  for k in zero_six:
    de = list(actual_numbers[9] ^ set(k))
    is_legit = True
    for t in actual_numbers[1]:
      if t in de:
        is_legit =False
    if is_legit:
      break
  de.remove(e)
  d = de[0]

  actual_numbers[6] = set(list(filter(lambda x: d in x, zero_six))[0])

  actual_numbers[0] = set(list(filter(lambda x: not set(x) in [actual_numbers[6], actual_numbers[9]], six_nine_zero))[0])
  c = list(actual_numbers[6] ^ all_possible)[0]

  actual_numbers[2] = set(list(filter(lambda x: e in x, two_three_five))[0])
  three_five = list(filter(lambda x: not actual_numbers[2] == set(x), two_three_five))


  actual_numbers[3] = set(list(filter(lambda x: c in x, three_five))[0])
  actual_numbers[5] = set(list(filter(lambda x: not actual_numbers[3] == set(x), three_five))[0])
  final_str = ""

  for u in output:
    for key, value in actual_numbers.items():
      if value == set(u):
        final_str += str(key)
        
  count += int(final_str)
  finding_nums = [4,2, 7, 3]
  for u in output:
    if len(u) in finding_nums:
        count1 += 1

print("Part 1:", count1)
print("Part 2", count)
dicta = collections.defaultdict(int)
counter = collections.Counter()
