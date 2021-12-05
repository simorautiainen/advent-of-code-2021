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
  first = point(*points[0])
  second = point(*points[1])
  
  if first.x == second.x or first.y == second.y: # horizontal and vertical
    ys = min([first.y, second.y]) + np.arange(abs(first.y-second.y)+1)
    xs = min([first.x, second.x]) + np.arange(abs(first.x-second.x)+1)

    counter.update(map(lambda x: point(*x), itertools.product(xs, ys)))
  else: # Diagonal
    left_point, right_point = sorted([first, second], key=lambda x: x.x)
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