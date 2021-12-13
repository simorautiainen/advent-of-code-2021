import itertools
from typing import DefaultDict
import numpy as np
import collections

folds = []
with open("inputs/day13") as file:
  f = file.read()
  #print(f)
  f= f.split("\n\n")
  data = np.array(list(map(lambda x: x.split(','), f[0].split('\n')))).astype(np.int64)
  for c in f[1].split('\n'):
    fold = c.split('\n')[0].split(' ')[-1].split('=')
    folds.append(fold)


def do_fold(inp_data, fold):
  data = np.copy(inp_data)
  key, value = fold
  value = int(value)
  if key == 'y':
    for i in range(data.shape[0]):
      x,y=data[i]
      if y >= value:
        data[i] = [x, value-(y-value)]
  elif key == 'x':
    for i in range(data.shape[0]):
      x,y=data[i]
      if x >= value:
        data[i] = [value-(x-value), y]
  return data

new_data = data
for i, fold in enumerate(folds):
  new_data= do_fold(new_data, fold)
  if i == 0:
    uniques = np.unique(new_data, axis=0)
    print("Part 1:", uniques.shape[0])


def print_data(data):
  zero_arr = np.zeros([max(data[:,1])+1, max(data[:,0])+1])
  for x,y in data:
    zero_arr[y, x] = 1
  for k in range(zero_arr.shape[0]):
    print(''.join([' ' if i==0 else '1' for i in zero_arr[k]]))
uniques = np.unique(new_data, axis=0)
flipped = np.flip(uniques, axis = 1)
print("PART 2:\n")
print_data(flipped)
