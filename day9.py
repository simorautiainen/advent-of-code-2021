import operator
import functools
import numpy as np
import collections
point = collections.namedtuple('point', ['x', 'y'])
with open("inputs/day9") as data:
  f = data.readlines()
  data = np.array(list(map(lambda x: list(x.strip()), f))).astype(np.int32)

print(data)
legits = []

vecs = [point(0,1), point(1,0), point(-1,0), point(0, -1)]
for iy, ix in np.ndindex(data.shape):

  is_legit = True
  for vec in vecs:
    x = ix+vec.x
    y = iy+vec.y
    if x >=0 and x < data.shape[1] and y >=0 and y < data.shape[0]:
      if data[iy, ix] >= data[y, x]:
        is_legit = False
  if is_legit:
    legits.append(point(ix,iy))

total = 0
for x,y in legits:
  total += data[y,x]+1
print(f"total = {total}")

def find_bas(inp_point, already_checked_locs):
  for vec in vecs:
    new_p = point(inp_point.x+vec.x, inp_point.y+vec.y)

    if new_p in already_checked_locs:
      continue
    if (not new_p in already_checked_locs) and new_p.x >=0 and new_p.x < data.shape[1] and new_p.y >=0 and new_p.y < data.shape[0]:
      legit_point = is_legit_point(new_p, already_checked_locs)
      if legit_point:
        already_checked_locs.append(new_p)
        find_bas(new_p, already_checked_locs)

  return already_checked_locs


def is_legit_point(inp_point, already_checked_locs):
  if data[inp_point.y, inp_point.x] == 9: return False
  return True


sizes = []
for a_point in legits:
  bas_arr=  find_bas(a_point, [a_point])
  if len(bas_arr) == 105:
    longest = bas_arr

  sizes.append(len(bas_arr))

print("Part 2", functools.reduce(operator.mul, sorted(sizes)[-3:]))
