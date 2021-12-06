import itertools
import numpy as np
import time
start = time.time()
with open("inputs/day4") as data:
  f = data.read()
  stripped = [i.strip() for i in f.split('\n\n')]
  bingo_row = np.array(stripped[0].split(',')).astype(np.int64)
  tables = np.array(list(map(lambda x: x.split(), stripped[1:]))).astype(np.int64)
  tables = tables.reshape(100, 5, 5) # easier to handle when bingo tables are in 5x5 format

def which_tables_won(current_numbers, tables, tables_won: dict) -> list[int]:
  coords_of_current_numbers = np.where(np.isin(tables, current_numbers))
  table_arr = np.transpose(np.array(coords_of_current_numbers))

  finished_arrs  = []
  for i in list(dict(filter(lambda x: not x[1], tables_won.items())).keys()):
    np_arr = table_arr[table_arr[:,0] == i][:,1:]
    
    # check that there was even one match because bincount will cause error if it is given empty
    # array
    if np_arr.shape[0] > 0:
      y_count: int = np.bincount(np_arr[:,0]).max()
      x_count: int = np.bincount(np_arr[:,1]).max()
      # If there is 5 same x_value or 5 same y values, it means BINGO
      if y_count == 5 or x_count==5:
        finished_arrs.append(i)
  return finished_arrs

def calculate_final_score(table_number: int, latest_bingo_number: int, current_numbers, tables) -> int:
  only_unmarked: np.array = tables[table_number]

  # Set those numbers that are in current numbers to zero, so we can count easily the sum of
  # all other numbers
  only_unmarked[np.where(np.isin(only_unmarked,current_numbers))] = 0
  return np.sum(only_unmarked)*latest_bingo_number

def get_nth_winner_final_score(tables, bingo_row, nth_winner: int = 1) -> int:
  current_numbers = []
  tables_won = dict(zip(range(tables.shape[0]), list(itertools.repeat(False, tables.shape[0]))))
  if nth_winner < 0:
    max_number_of_winners = tables.shape[0]+1
    nth_winner = max_number_of_winners+nth_winner

  for num in bingo_row:
    current_numbers.append(num)
    just_won_tables = which_tables_won(current_numbers, tables, tables_won)
    for won_table_number in just_won_tables:
      tables_won[won_table_number] = True
      if sum(tables_won.values()) == nth_winner:
        return calculate_final_score(won_table_number, num, current_numbers, tables)


print("Part 1:", get_nth_winner_final_score(tables, bingo_row))
print("Part 2:", get_nth_winner_final_score(tables, bingo_row, -1))
print(time.time() - start)