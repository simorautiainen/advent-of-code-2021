import math
import operator
import collections
import itertools
import numpy as np
with open("inputs/day17") as data:
  f = data.readlines()
  data = f[0].split(' ')
  xs = data[2].split('=')[1].split('..')
  xs[1] = xs[1][:-1]
  xs = list(map(int, xs))

  ys = data[3].split('=')[1].split('..')
  ys = list(map(int, ys))

max_ys = []
for x in itertools.count(start=1, step= 1):
  x_sum = sum(range(x+1))
  if x_sum >= xs[0] and x_sum <= xs[1]:
    did_not_append = 0
    for y in itertools.count(start=0, step= 1):
      y_sum = sum(range(y+1))
      for y_minus in itertools.count(start=1, step= 1):
        cur_y = y_sum - sum(range(y_minus+1))
        if cur_y >= ys[0] and cur_y <= ys[1]:
          did_not_append = 0
          max_ys.append(y_sum)
        elif cur_y < ys[0]:
          did_not_append+=1
          break
      if did_not_append > 200:
        break
  elif x_sum > xs[1]:
    break
print("Part 1:", max(max_ys))

point = collections.namedtuple('point', ['x', 'y'])
hits_arr = set()
max_no_hits_in_a_row = 300 # depends on the input :D you need to increase this if the answer is wrong
min_start_y = -200 # depends on the input :D you need to decrease (or in rare case increase) this if the answer is wrong
cur_no_x_hits_in_a_row = 0
for x in itertools.count(start=1, step= 1):
  cur_no_y_hits_in_a_row = 0
  for y in itertools.count(start=-min_start_y, step= 1):
    for step in itertools.count(start=0, step= 1):
      cur_x = sum(range(x-step, x+1)) if (x-step) > 0 else sum(range(x+1))
      cur_y = sum(range(y-step, y+1))
      if cur_x >= xs[0] and cur_x <= xs[1] and cur_y >= ys[0] and cur_y <= ys[1]:
        cur_no_y_hits_in_a_row = 0
        cur_no_x_hits_in_a_row = 0
        hits_arr.add(point(x, y))
      elif cur_y < ys[0]:
        cur_no_y_hits_in_a_row += 1
        break
    if cur_no_y_hits_in_a_row > max_no_hits_in_a_row:
      cur_no_x_hits_in_a_row +=1
      break
  if cur_no_x_hits_in_a_row > max_no_hits_in_a_row:
    break

print("Part 2:", len(hits_arr))