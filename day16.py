import itertools
import numpy as np
import collections
import functools
import math

with open("inputs/day16") as data:
  f = data.readlines()
  binary_data = ""
  for char in f[0]:
    #print(format(int(char, 16), '04b'))
    binary_data += format(int(char, 16), '04b')

#print(binary_data)

total_version = 0
def read_packet(inp_str, how_many_packets):
  curr_str  =inp_str[:]
  global total_version
  totals = []
  for _ in range(how_many_packets):
    cur_version = int(curr_str[:3],2)
    total_version += cur_version
    cur_id = int(curr_str[3:6],2)
    curr_str = curr_str[6:]
    if cur_id == 4:
      total_str = ""
      while curr_str[0] == '1':
        total_str += curr_str[1:5]
        curr_str = curr_str[5:]
      total_str += curr_str[1:5]
      totals.append(int(total_str, 2))
      curr_str = curr_str[5:]
    else:
      if curr_str[0] == '1':
        sub_packets = int(curr_str[1:12], 2)
        curr_str, total = read_packet(curr_str[12:], sub_packets)
      else:
        bits_to_check = int(curr_str[1:16], 2)
        curr_str = curr_str[16:]
        curr_str_len = len(curr_str)
        total=[]
        while (bits_to_check - (curr_str_len-len(curr_str))) != 0:
          curr_str, total_tmp = read_packet(curr_str, 1)
          total += total_tmp
      match cur_id:
        case 0:
          totals.append(sum(total))
        case 1:
          totals.append(math.prod(total))
        case 2:
          totals.append(min(total))
        case 3:
          totals.append(max(total))
        case 5:
          totals.append(int(total[0] > total[1]))
        case 6:
          totals.append(int(total[0] < total[1]))
        case 7:
          totals.append(int(total[0] == total[1]))
  return [curr_str, totals]

final_str, totals = read_packet(binary_data, 1)

print("Part 1", total_version)
print("Part 2", totals[0])