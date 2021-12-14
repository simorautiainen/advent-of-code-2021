
import collections
import functools
with open("inputs/day14") as file:
  f = file.read()
  polymer, pairs = f.split('\n\n')
  pairs = list(map(lambda x: x.split(' -> '), pairs.split('\n')))

def do_x_iter_zipper(polymer, how_many_iters):
  zipped = zip(polymer, polymer[1:])
  counter = collections.Counter(polymer)
  for a_zip in zipped:
    counter += recurs(a_zip, how_many_iters)
  return counter

@functools.cache
def recurs(inp_zip, how_many_iters, cur_iter=0):
  counter = collections.Counter()
  if cur_iter == how_many_iters:
    return counter
  cur_iter+=1
  stringi = ''.join(inp_zip)
  for pair in pairs:
    inbetween, inserted = pair
    if inbetween == stringi:
      counter[inserted] += 1
      counter += recurs((inp_zip[0], inserted), how_many_iters, cur_iter)
      counter += recurs((inserted, inp_zip[1]), how_many_iters, cur_iter)
  return counter


counter = do_x_iter_zipper(polymer, 10).most_common()
print("Part 1:", counter[0][1]-counter[-1][1])
counter = do_x_iter_zipper(polymer, 40).most_common()
print("Part 2:", counter[0][1]-counter[-1][1])