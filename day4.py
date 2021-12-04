import collections
import itertools
import numpy as np

with open("inputs/day4") as data:
  f = data.read()
  stripped = [i.strip() for i in f.split('\n\n')]
  bingo_row = stripped[0]

  tables = list(map(lambda x: np.array_split(x.split(), 5), stripped[1:]))

coord = collections.namedtuple('Coord', ['x', 'y', 'val'])
bingo_locs = collections.defaultdict(set)
actual_locs = collections.defaultdict(set)

tables_won = dict(zip(range(len(tables)), list(itertools.repeat(False, len(tables)))))

for d, table in enumerate(tables):
    for i, row in enumerate(table):
      for k, val in enumerate(row):
        actual_locs[d].add(coord(k, i, int(val)))

def did_table_win(table_number) -> bool:
  bingo_coords: set = bingo_locs[table_number]
  ys = list(map(lambda a: 'y'+str(a.y), bingo_coords))
  xs = list(map(lambda a: 'x'+str(a.x), bingo_coords))
  counter = collections.Counter(itertools.chain(ys, xs))
  most_common = counter.most_common(1)

  if len(most_common) < 1:
    return False

  most_common_val: int = most_common[0][1]
  # if there is 5 same x coords or 5 same y coords in bingo_locs
  return 5 == most_common_val

def calculate_final_score(table_number: int, latest_bingo_number: int) -> int:
  unmarked_coords: set = bingo_locs[table_number] ^ actual_locs[table_number]
  unmarked_sum: int = sum(map(lambda x: x.val, unmarked_coords))
  return unmarked_sum*latest_bingo_number

def get_nth_winner_final_score(nth_winner: int = 1) -> int:
  for num in bingo_row.split(','):
    for d, table in enumerate(tables):
      for i, row in enumerate(table):
        for k, val in enumerate(row):
          if num == val:
            bingo_locs[d].add(coord(k, i, int(val)))

      is_done: bool = did_table_win(d)
      if is_done == True:
        tables_won[d] = True
        if sum(tables_won.values()) == nth_winner or nth_winner == -1 and all(tables_won.values()):
          return calculate_final_score(d, int(num))


print(get_nth_winner_final_score())
print(get_nth_winner_final_score(-1))