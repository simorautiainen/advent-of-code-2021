
import collections

with open("inputs/day12") as file:
  f = file.readlines()
  data = list(map(lambda x: x.strip().split('-'), f))

connections = collections.defaultdict(set)
for from_p, to_p in data:
  connections[from_p].add(to_p)
  connections[to_p].add(from_p)

def recurse_through_part1(current_path, connections):
  amount = 0
  for connection in connections[current_path[-1]]:
    if connection == 'end':
      amount+=1
    elif (connection.islower() and not connection in current_path) or connection.isupper():
      amount += recurse_through_part1(current_path+[connection], connections)
  return amount
print("Part 1:", recurse_through_part1(['start'], connections))

def recurse_through_part2(current_path, connections):
  visits = collections.Counter(filter(str.islower, current_path))
  is_cave_visited_twice = max(visits.values()) == 2
  amount = 0
  for connection in connections[current_path[-1]]:
    if connection == 'end':
      amount += 1
    elif connection.isupper() or connection != 'start' and (connection.islower() and (not is_cave_visited_twice or not connection in current_path)):
      new_path = current_path+[connection]
      amount += recurse_through_part2(new_path, connections)
  return amount

print("Part 2", recurse_through_part2(['start'], connections))
