import math
import itertools
import ast
import functools

with open("inputs/day18") as data:
  f = data.readlines()
  lists = []
  for line in f:
    lists.append(ast.literal_eval(line))

def red(first, second):
  total_list = []
  total_list.append(first)
  total_list.append(second)
  while True:
    tmp_total_list = total_list.copy()
    while True:
      iter_total_list = explode_first(tmp_total_list, 1)
      iter_total_list = replace_minus_ones(iter_total_list)
      if iter_total_list == tmp_total_list:
        break
      tmp_total_list = iter_total_list
    iter_total_list = split_first(iter_total_list)
    if iter_total_list == total_list:
      break
    total_list = iter_total_list
  return total_list

def replace_minus_ones(arr):
  arr_copy = arr.copy()
  for i, curr in enumerate(arr_copy):
    if isinstance(curr, list):
      arr_copy[i] = replace_minus_ones(curr)
    else:
      if curr == -1:
        arr_copy[i] = 0
  return arr_copy
def split_first(arr):
  arr_copy = arr.copy()
  for i, curr in enumerate(arr_copy):
    if isinstance(curr, list):
      new = split_first(curr)
      if curr != new:
        arr_copy[i] = new
        return arr_copy
    else:
      if curr >= 10:
        curr_arr = [math.floor(curr/2), math.ceil(curr/2)]
        arr_copy[i] = curr_arr
        return arr_copy
  return arr_copy

def explode_first(arr, cur_depth):
  if cur_depth == 5 and isinstance(arr, list):
    return -1
  left_part = arr[0].copy() if isinstance(arr[0], list) else arr[0]
  right_part = arr[1].copy() if isinstance(arr[1], list) else arr[1]
  if isinstance(left_part, list):
    new_left_part = explode_first(left_part, cur_depth+1)
    if (new_left_part == -1 or is_ind_most_zero(new_left_part, 1)) and new_left_part != left_part:
      right_part = add_val_to_ind_most(right_part,0, get_ind_most_val(left_part, 1))
    if new_left_part != left_part:
      return [new_left_part, right_part]
  if isinstance(right_part, list):
    new_right_part = explode_first(right_part, cur_depth+1)
    if (new_right_part == -1 or is_ind_most_zero(new_right_part, 0)) and new_right_part != right_part:
      left_part = add_val_to_ind_most(left_part,1, get_ind_most_val(right_part, 0))
    if new_right_part != right_part:
      return [left_part, new_right_part]
  return [left_part, right_part]

def add_val_to_ind_most(arr, ind, val):
  if isinstance(arr, list):
    inp_arr = arr.copy()
    if isinstance(inp_arr[ind], list):
      inp_arr[ind] = add_val_to_ind_most(inp_arr[ind], ind, val)
    else:
      if inp_arr[ind] == -1:
        inp_arr[ind] = 0
      inp_arr[ind] += val 
    return inp_arr
  else:
    if arr == -1:
      return val
    return arr + val

def is_ind_most_zero(arr, ind):
  if isinstance(arr, list):
    if isinstance(arr[ind], list):
      return is_ind_most_zero(arr[ind], ind)
    else:
      return arr[ind] == -1
  else:
    return arr == -1 # its not actually array but a value

def get_ind_most_val(arr, ind):
  if isinstance(arr, list):
    if isinstance(arr[ind], list):
      return get_ind_most_val(arr[ind], ind)
    else:
      if arr[ind] < 0:
        return 0
      return arr[ind]
  else:
    return arr # its not actually array but a value

def get_magnitude(left, right):
  if isinstance(left, list):
    magn_left = get_magnitude(*left) * 3
  else:
    magn_left = left*3
  if isinstance(right, list):
    magn_right = get_magnitude(*right) * 2
  else:
    magn_right = right * 2
  return magn_left + magn_right

all_reduced = functools.reduce(red, lists)
print("Part 1", functools.reduce(get_magnitude, all_reduced))


best_magn = 0
for perm in itertools.permutations(lists, r=2):
  reduced = red(*perm)
  magn = get_magnitude(*reduced)
  if magn > best_magn:
    best_magn = magn

print("Part 2", best_magn)