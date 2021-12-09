import operator
import functools
import numpy as np
import collections

with open("inputs/day9") as data:
  f = data.readlines()
  data = np.array(list(map(lambda x: list(x.strip()), f))).astype(np.int32)

point = collections.namedtuple('point', ['x', 'y'])
vecs = [point(0,1), point(1,0), point(-1,0), point(0, -1)]
def is_point_in_bounds(inp_point):
  return inp_point.x >=0 and inp_point.x < data.shape[1] and inp_point.y >=0 and inp_point.y < data.shape[0]

# part 1
legits = []
for iy, ix in np.ndindex(data.shape):

  is_smallest = True
  for vec in vecs:
    new_p = point(ix+vec.x, iy+vec.y)

    if is_point_in_bounds(new_p) and data[iy, ix] >= data[new_p.y, new_p.x]:
      is_smallest = False
      break
  if is_smallest:
    legits.append(point(ix,iy))

total = 0
for x,y in legits:
  total += data[y,x]+1
print(f"Part 1 = {total}")

#part 2
def find_bas(inp_point: point, legit_locs: list[point]) -> list[point]:
  for vec in vecs:
    new_p = point(inp_point.x+vec.x, inp_point.y+vec.y)

    if (not new_p in legit_locs) and is_point_in_bounds(new_p) and not (data[new_p.y, new_p.x] == 9):
      legit_locs.append(new_p)
      find_bas(new_p, legit_locs)

  return legit_locs

sizes = []
for a_point in legits:
  bas_arr = find_bas(a_point, [a_point])
  sizes.append(len(bas_arr))

print("Part 2", functools.reduce(operator.mul, sorted(sizes)[-3:]))
