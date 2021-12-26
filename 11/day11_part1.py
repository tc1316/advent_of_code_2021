import numpy as np

with open('input.txt') as f:
  input = [list(line.strip()) for line in f]
  array = np.array([x for x in input]).astype(int)

y_length = array.shape[0]
x_length = array.shape[1]
ones = np.ones(np.shape(array))
count = 0

def IncrementNeighbours(r, c): 
  dirs = [(1,1),(1,0),(1,-1),(0,1),(-1,-1),(-1,0),(-1,1),(0,-1)]
  for dr,dc in dirs:
    rr = r + dr
    cc = c + dc
    if rr >= 0 and cc >= 0 and rr < y_length and cc < x_length and array[rr][cc] != 0:
      array[rr][cc] += 1

def CheckFlashes():
  global count
  flashed = True

  while flashed:
    flashed = False
    for r in range(y_length):
      for c in range(x_length):
        if array[r][c] >= 10:
          array[r][c] = 0
          IncrementNeighbours(r,c)
          flashed = True
          count += 1
  return count

for i in range(100):
  array = np.add(array, ones)
  CheckFlashes()
  print(count)

  


