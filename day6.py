import collections
import itertools

with open("inputs/day6") as data:
  f = data.readlines()
  data = list(map(int, f[0].split(',')))
  
def get_nth_day_total(data, days):

  counter = collections.Counter(data)
  extras = collections.Counter()
  for amount, i in enumerate(itertools.cycle(range(7))):
    if amount == days:
      break
    added_index = (i+2) % 7
    update_dict = {added_index: counter[i] - extras[i]}
    extras.update(update_dict)
    counter.update(update_dict)
    extras[i] = 0

  return counter.total()

print("Part 1", get_nth_day_total(data, 80))
print("Part 2", get_nth_day_total(data, 256))
