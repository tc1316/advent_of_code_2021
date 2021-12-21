import numpy as np
from collections import Counter

with open('input.txt') as f:
  input = [int(x) for x in f.read().split(',')]
  
# print(np.array(input))

def fish():
  for days in range(80):
    c = len(input)
    for num in range(len(input)):
      input[num] -= 1
      if input[num] < 0:
        input[num] = 6
        input.append(8)
      
  return len(input)


def fish2():
  timers = Counter({timer: 0 for timer in range(10)})
  fishes = Counter(input)
  fishes.update(timers)

  print(fishes)

  for day in range(256):
          fishes[7] += fishes.get(0, 0)
          fishes[9] += fishes.get(0, 0)

          fishes = {fish: fishes.get(fish + 1, 0) for fish in fishes}
  return sum(fishes.values())

fish2() 

# print(fish2()) 

  