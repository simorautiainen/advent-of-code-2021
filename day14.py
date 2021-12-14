
import collections
import functools

with open("inputs/day14") as file:
  f = file.read()
  polymer, pairs = f.split('\n\n')
  pairs = list(map(lambda x: x.split(' -> '), pairs.split('\n')))

def do_x_iterations(polymer: str, how_many_iters: int) -> collections.Counter:
  zipped = zip(polymer, polymer[1:])
  counter = collections.Counter(polymer)
  for tuple_pair in zipped:
    counter += recurs(tuple_pair, how_many_iters)
  return counter

@functools.cache
def recurs(tuple_pair: tuple, depth: int, current_depth: int = 0) -> collections.Counter:
  counter = collections.Counter()
  if depth == current_depth:
    return counter
  current_depth+=1
  string_pair: str = ''.join(tuple_pair)
  for pair in pairs:
    pair_condition, inser_char = pair
    if pair_condition == string_pair:
      counter[inser_char] += 1
      counter += recurs((tuple_pair[0], inser_char), depth, current_depth)
      counter += recurs((inser_char, tuple_pair[1]), depth, current_depth)
  return counter


counter = do_x_iterations(polymer, 10).most_common()
print("Part 1:", counter[0][1]-counter[-1][1])
counter = do_x_iterations(polymer, 40).most_common()
print("Part 2:", counter[0][1]-counter[-1][1])