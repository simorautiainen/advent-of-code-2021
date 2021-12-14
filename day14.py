
import collections
import functools

with open("inputs/day14") as file:
  f = file.read()
  polymer, pairs = f.split('\n\n')
  pairs = list(map(lambda y: [tuple(y[0]), y[1]], map(lambda x: x.split(' -> '), pairs.split('\n'))))

def do_x_iterations(polymer: str, how_many_iters: int) -> collections.Counter:
  paired = zip(polymer, polymer[1:])
  counter = collections.Counter(polymer)
  for tuple_pair in paired:
    counter += recurse_a_tuple_pair(tuple_pair, how_many_iters)
  return counter

@functools.cache
def recurse_a_tuple_pair(tuple_pair: tuple, depth: int, current_depth: int = 0) -> collections.Counter:
  counter = collections.Counter()
  if depth == current_depth:
    return counter
  current_depth+=1
  for pair in pairs:
    pair_condition, new_char = pair
    if pair_condition == tuple_pair:
      counter[new_char] += 1
      counter += recurse_a_tuple_pair((tuple_pair[0], new_char), depth, current_depth)
      counter += recurse_a_tuple_pair((new_char, tuple_pair[1]), depth, current_depth)
      break
  return counter


counter = do_x_iterations(polymer, 10).most_common()
print("Part 1:", counter[0][1]-counter[-1][1])
counter = do_x_iterations(polymer, 40).most_common()
print("Part 2:", counter[0][1]-counter[-1][1])