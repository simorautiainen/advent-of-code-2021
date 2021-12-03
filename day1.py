
with open("inputs/day1") as data:
  f = data.readlines()
  data = [int(i.strip()) for i in f]

#part 1
increased = 0
for i in range(1,len(data)):
  increased += data[i] > data[i-1]

print(f"Part 1 increased ones = {increased}")
#part 1 with oneliner
increased = sum([data[i] > data[i-1] for i in range(1,len(data))])
print(f"Part 1 increased ones = {increased}")



# part 2
from collections import deque

d = deque(data[:3])
increased = 0
prev_sum=sum(d)
for val in data[3:]:
  d.popleft()
  d.append(val)
  current_sum = sum(d)
  increased += current_sum > prev_sum
  prev_sum=current_sum

print(f"Part 2 Increased ones = {increased}")

# part 2 with oneliner
increased = sum([sum(data[i-3:i]) > sum(data[i-4:i-1]) for i in range(4, len(data)+1)])
print(f"part 2 increased = {increased}")