import itertools
import numpy as np
import collections
import functools

with open("inputs/day15") as data:
  f = data.readlines()
  data = np.array(list(map(lambda x: list(x.strip()), f))).astype(np.int32)

print(f"{data =}")

point = collections.namedtuple('point', ['x', 'y'])

def is_point_in_bounds(inp_point, data):
  return inp_point.x >=0 and inp_point.x < data.shape[1] and inp_point.y >=0 and inp_point.y < data.shape[0]

start = point(0, 0)
vecs = [point(0, 1), point(1, 0), point(-1, 0), point(0,-1)]

def print_d(dat):

  for k in range(dat.shape[0]):
    print(' '.join([str(int(i)) for i in dat[k]]))

def calc(inp_data, start=point(0,0)):
  data = np.copy(inp_data)
  djikstar_data = np.full(data.shape, np.sum(data))
  shape = djikstar_data.shape
  djikstar_data[start.y, start.x] = 0
  data_sum = np.sum(data)
  i = 0
  while True:
    if i % 1000==0:
      print(f"{i} / {shape[0]*shape[1]}") # every 1000 iterations print to see progress
    i += 1

    min_point = point(*list(zip(*np.where(djikstar_data==np.amin(djikstar_data))))[0][::-1])

    if min_point == point(shape[1]-1, shape[0]-1):
      return djikstar_data[min_point.y, min_point.x]
    for vec in vecs:
      new_p = point(min_point.x+vec.x, min_point.y+vec.y)
      if is_point_in_bounds(new_p, data) and djikstar_data[new_p.y, new_p.x] != (data_sum+1):
        to_new_point_total = data[new_p.y, new_p.x]+djikstar_data[min_point.y, min_point.x]
        if djikstar_data[new_p.y, new_p.x] > to_new_point_total:
          djikstar_data[new_p.y, new_p.x] = to_new_point_total
    djikstar_data[min_point.y, min_point.x] = data_sum+1

lowest_path = calc(data)
print("Part 1", lowest_path)

part2data = np.hstack((data, data+1, data+2, data+3, data+4))
part2data = np.array(np.vstack((part2data, part2data+1, part2data+2, part2data+3, part2data+4)))
part2data = part2data % 9
part2data[part2data == 0] = 9

lowest_path = calc(part2data)
print("Part 2", lowest_path)