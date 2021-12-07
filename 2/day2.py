hz = 0
depth = 0
aim = 0

lines = []
with open('input.txt') as f:
    lines = f.readlines()


for line in lines:
  command = line.split(" ")
  if command[0] == 'forward':
    hz += int(command[1])
    depth += aim * int(command[1])
  elif command[0] == 'down':
    aim += int(command[1])
  elif command[0] == 'up':
    aim -= int(command[1])

print(hz*depth)