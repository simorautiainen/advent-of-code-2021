import itertools
import numpy as np
import collections

with open("inputs/day11") as data:
  f = data.readlines()
  data = np.array(list(map(lambda x: list(x.strip()), f))).astype(np.int32)

point = collections.namedtuple('point', ['x', 'y'])
vecs = [point(i, k) for i in range(-1,2) for k in range(-1,2) if not(k == 0 and i == 0)]

def is_point_in_bounds(inp_point, data):
  return inp_point.x >=0 and inp_point.x < data.shape[1] and inp_point.y >=0 and inp_point.y < data.shape[0]

def do_one_iter(data):
  flashes = 0
  flashed = []
  data += 1
  coords = [point(*one_point[::-1]) for one_point in zip(*np.where(data >= 10))]
  for a_point in coords:
    flashes += flash_a_point(a_point, data, flashed)
  data[data >= 10] = 0
  return flashes

def flash_a_point(inp_point, data, flashed):
  total_flashes = 1
  for vec in vecs:
    new_p = point(vec.x + inp_point.x, vec.y + inp_point.y)
    if is_point_in_bounds(new_p, data):
      data[new_p.y, new_p.x] += 1
      if data[new_p.y, new_p.x] == 10 and not new_p in flashed:
        flashed.append(new_p)
        total_flashes += flash_a_point(new_p, data, flashed)
  return total_flashes

total = 0
part1_data = np.copy(data)
for i in range(100):
  total += do_one_iter(part1_data)

print("Part 1:", total)

part2_data = np.copy(data)
for i in itertools.count(start=1, step=1):
  cur = do_one_iter(part2_data)
  if cur == part2_data.size:
    print("Part 2:", i)
    break