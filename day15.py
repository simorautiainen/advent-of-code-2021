import itertools
import numpy as np
import collections
import functools

with open("inputs/day15") as data:
  f = data.readlines()
  data = np.array(list(map(lambda x: list(x.strip()), f))).astype(np.int32)

print(f"{data =}")

point = collections.namedtuple('point', ['x', 'y'])
vecs = [point(0, 1), point(1, 0)]

def is_point_in_bounds(inp_point):
  return inp_point.x >=0 and inp_point.x < data.shape[1] and inp_point.y >=0 and inp_point.y < data.shape[0]

start = point(0, 0)
vecs = [point(0, 1), point(1, 0), point(-1, 0), point(0,-1)]

def print_d(dat):

  for k in range(dat.shape[0]):
    print(' '.join([str(int(i)) for i in dat[k]]))

def calc(inp_data, start=point(0,0)):
  data = np.copy(inp_data)
  djikstar_data = np.full(data.shape, np.sum(data))

  visited = []
  djikstar_data[start.y, start.x] = 0
  while len(visited) < djikstar_data.size:
    print(len(visited))
    tmp_djikstar = np.copy(djikstar_data)
    for vis in visited:
      tmp_djikstar[vis.y, vis.x] = np.sum(data)
    min_point = point(*np.flip(list(zip(*np.where(tmp_djikstar==np.amin(tmp_djikstar)))))[0])

    for vec in vecs:
      new_p = point(min_point.x+vec.x, min_point.y+vec.y)
      if is_point_in_bounds(new_p) and not new_p in visited:
        to_new_point_total = data[new_p.y, new_p.x]+djikstar_data[min_point.y, min_point.x]
        if djikstar_data[new_p.y, new_p.x] > to_new_point_total:
          djikstar_data[new_p.y, new_p.x] = to_new_point_total

    visited.append(min_point)
  print(djikstar_data.size)
  return djikstar_data
shap = data.shape  

djik = calc(data)
print("Part 1:", djik[-1,-1])