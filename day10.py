import collections

with open("inputs/day10") as file:
  f = file.readlines()
  data = list(map(str.strip, f))

chunk_dict = {'open': list('([{<'), 'close': list(')]}>')}
point_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
point_dict_part_2 = {')': 1, ']': 2, '}': 3, '>': 4}

que = collections.deque()
total = 0
part2_total = []

for line in data:
  for mark in line:
    if mark in chunk_dict['open']:
      que.append(mark)
    elif mark in chunk_dict['close']:
      popped = que.pop()
      if chunk_dict['open'].index(popped) != chunk_dict['close'].index(mark):
        total+=point_dict[mark] # part 1
        que.clear()
        break
  if que: # part 2
    cur_total = 0
    while que:
      popped = que.pop()
      cur_total*=5
      cur_total += point_dict_part_2[chunk_dict['close'][chunk_dict['open'].index(popped)]]
    part2_total.append(cur_total)


print("Part 1:", total)
print("Part 2:", sorted(part2_total)[int(len(part2_total)/2)])