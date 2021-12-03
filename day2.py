from collections import defaultdict
with open("inputs/day2") as data:
  f = data.readlines()
  data = [i.strip() for i in f]

d = defaultdict(int)
depth_coeff={'up': -1, 'down': 1}
for i in data:
  instruction, val = i.split(' ')
  if instruction in depth_coeff:
    d['depth'] += int(val) * depth_coeff[instruction]
  else:
    d[instruction] += int(val)
    d['depth_2'] += d['depth'] * int(val) # part2. Depth is now aim in part 2 and depth2 is depth

print("Part 1:", d['depth']*d['forward'])
print("Part 2:", d['depth_2']*d['forward'])
