import itertools
import numpy as np

with open("inputs/day4") as data:
  f = data.read()
  stripped = [i.strip() for i in f.split('\n\n')]
  bingo_row = np.array(stripped[0].split(',')).astype(np.int64)

  tables = np.array(list(map(lambda x: np.array_split(x.split(), 5), stripped[1:]))).astype(np.int64)


def did_table_win(table_number, current_numbers) -> bool:
  coords_of_current_numbers = tuple(zip(*np.where(np.isin(tables[table_number], current_numbers))))
  if len(coords_of_current_numbers) > 0:
    back_to_np = np.array(coords_of_current_numbers)
    y_count = np.bincount(back_to_np[:,0]).max()
    x_count = np.bincount(back_to_np[:,1]).max()
    # If there is 5 same x_value or 5 same y values, it means BINGO
    if y_count == 5 or x_count==5:
      return True
  return False

def calculate_final_score(table_number: int, latest_bingo_number: int, current_numbers) -> int:
  only_unmarked: np.array = tables[table_number]
  # set those that are not in current_numbers to zero
  only_unmarked[np.where(np.isin(only_unmarked,current_numbers))] = 0
  return np.sum(only_unmarked)*latest_bingo_number

def get_nth_winner_final_score(nth_winner: int = 1) -> int:
  current_numbers = []
  tables_won = dict(zip(range(tables.shape[0]), list(itertools.repeat(False, tables.shape[0]))))

  for num in bingo_row:
    current_numbers.append(num)
    for d in range(len(tables)):
      if tables_won[d]: continue
      is_done: bool = did_table_win(d, current_numbers)
      if is_done == True:
        tables_won[d] = True
        if sum(tables_won.values()) == nth_winner or nth_winner == -1 and all(tables_won.values()):
          return calculate_final_score(d, num, current_numbers)

print(get_nth_winner_final_score())
print(get_nth_winner_final_score(-1))