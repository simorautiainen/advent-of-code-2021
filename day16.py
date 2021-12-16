import itertools
import numpy as np
import collections
import functools

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
  for _ in range(how_many_packets):
    cur_version = int(curr_str[:3],2)
    total_version += cur_version
    cur_id = int(curr_str[3:6],2)
    curr_str = curr_str[6:]
    if cur_id == 4:
      #total_str = ""
      while curr_str[0] == '1':
        #total_str += curr_str[1:5]
        curr_str = curr_str[5:]
      #total_str += curr_str[1:5]
      curr_str = curr_str[5:]
    else:
      if curr_str[0] == '1':
        sub_packets = int(curr_str[1:12], 2)
        curr_str = read_packet(curr_str[12:], sub_packets)
      else:
        bits_to_check = int(curr_str[1:16], 2)
        curr_str = curr_str[16:]
        curr_str_len = len(curr_str)
        while (bits_to_check - (curr_str_len-len(curr_str))) != 0:
          curr_str = read_packet(curr_str, 1)

  return curr_str

read_packet(binary_data, 1)
print(total_version)