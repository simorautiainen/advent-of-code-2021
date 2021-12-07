import collections
import itertools

with open("inputs/day7") as data:
  f = data.readlines()
  data = list(map(int, f[0].split(',')))


dicta = collections.defaultdict(int)
for i in range(min(data), max(data)):
  for k in data:
    dicta[i] += abs(k-i)

print("Part 1", min(list(dicta.values())))

dicta = collections.defaultdict(int)
for i in range(min(data), max(data)):
  for k in data:
    dicta[i] += sum([d for d in range(abs(k-i)+1)])

print("Part 2", min(list(dicta.values())))