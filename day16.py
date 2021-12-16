import math
import operator
with open("inputs/day16") as data:
  f = data.readlines()
  binary_data = ''.join(map(lambda char: format(int(char, 16), '04b'), f[0]))

total_version = 0

id_functions = {0: sum, 1: math.prod, 2: min, 3: max, 5: operator.gt, 6: operator.lt, 7: operator.eq}
def read_packet(inp_str, how_many_packets):
  curr_str  =inp_str[:]
  global total_version # part 1
  totals = []
  for _ in range(how_many_packets):
    cur_version = int(curr_str[:3],2) # part 1
    total_version += cur_version # part 1
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
      if cur_id < 5:
        totals.append(int(id_functions[cur_id](total)))
      else: # lt, gt and eq requires input unpacked
        totals.append(int(id_functions[cur_id](*total)))
  return [curr_str, totals]

final_str, totals = read_packet(binary_data, 1)

print("Part 1", total_version)
print("Part 2", totals[0])