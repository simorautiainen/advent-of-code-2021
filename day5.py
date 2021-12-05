import collections
import itertools
import numpy as np

with open("inputs/day5") as data:
  f = data.readlines()
  data = np.array(list(map(lambda x: [x[0].split(','), x[1].split(',')],[i.strip().split(' -> ') for i in f]))).astype(np.int32)

counter = collections.Counter()
counter_diagonal = collections.Counter()
point = collections.namedtuple('Point', ['x', 'y'])

for c, points in enumerate(data):
  from_point = point(*points[0])
  to_point = point(*points[1])
  
  if from_point.x == to_point.x or from_point.y == to_point.y: # horizontal and vertical
    ys = min([from_point.y, to_point.y]) + np.arange(abs(from_point.y-to_point.y)+1)
    xs = min([from_point.x, to_point.x]) + np.arange(abs(from_point.x-to_point.x)+1)

    counter.update(map(lambda x: point(*x), itertools.product(xs, ys)))
  else: # Diagonal
    left_point, right_point = sorted([from_point, to_point], key=lambda x: x.x)
    length = right_point.x-left_point.x+1

    xs = left_point.x + np.arange(length)
    ys = np.arange(length) * (-1 if left_point.y > right_point.y else 1)
    ys += left_point.y

    counter_diagonal.update(map(lambda x: point(*x), np.array([xs, ys]).T))
      
arr = np.array(list(counter.values()))
print("Part 1:", sum(arr > 1))

part2_counter = counter+counter_diagonal
arr = np.array(list(part2_counter.values()))
print("Part 2:", sum(arr > 1))