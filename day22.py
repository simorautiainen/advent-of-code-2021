import collections
import itertools

point = collections.namedtuple('point', ['x', 'y', 'z'])

instructions = []
with open("inputs/day22.test") as data:
  for line in data.readlines():
    instruction = collections.defaultdict(list)
    mode, coords = line.split(' ')
    x,y,z = map(lambda x: x.split('=')[1].split('..') , coords.split(','))
    from_p = point(int(x[0]), int(y[0]), int(z[0]))
    to_p = point(int(x[1]), int(y[1]), int(z[1]))
    instruction[mode] = [from_p, to_p]
    instructions.append(instruction)
print(instructions)

set_all_points = set()

for i, ins in enumerate(instructions):
  print(f"going through {i}/{len(instructions)} ins")
  mode, cube = next(iter(ins.items()))
  for x in range(cube[0].x, cube[1].x+1):
    if x <= 50 and x >= -50:
      for y in range(cube[0].y, cube[1].y+1):
        if y <= 50 and y >= -50:
          for z in range(cube[0].z, cube[1].z+1):
            if z <= 50 and z >= -50:
              cube_p = point(x,y,z)
              if mode=='on':
                set_all_points.add(cube_p)
              elif mode=='off' and cube_p in set_all_points:
                set_all_points.remove(cube_p)

print(len(set_all_points))