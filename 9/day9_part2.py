import sys
import numpy as np

with open('input.txt') as f:
  input = [list(line.strip()) for line in f]
  array = np.array([x for x in input]).astype(int)

rows_len = np.shape(array)[1]
cols_len = np.shape(array)[0]
mirror_array = np.zeros((100,100))

def LowPoint(array,r,c):
  dirs = [(1,0),(0,1),(0,-1),(-1,0)]
  # for r, c in np.ndindex(array.shape):
  for dr, dc in dirs:
    new_r = r + dr
    new_c = c + dc
    if new_r >=0 and new_c >=0 and new_r < rows_len and new_c < cols_len:
      if array[r][c] >= array[new_r][new_c]:
        return False
  return True

def MirrorArrayFill(array, r, c):
  if array[r][c] == 9:
    return
  if r < 0 or r >= rows_len-1:
    return
  if c < 0 or c >= cols_len-1:
    return
  if array[r][c] < 0:
    return

  array[r][c] = -1
  mirror_array[r][c] = 1
  MirrorArrayFill(array, r-1, c)
  MirrorArrayFill(array, r, c-1)
  MirrorArrayFill(array, r+1, c)
  MirrorArrayFill(array, r, c+1)

def AddToBasin(basin_array, basin_size):
  if len(basin_array) < 3:
    basin_array.append(basin_size)
  elif len(basin_array) == 3 and min(basin_array) < basin_size:
    basin_array[basin_array.index(min(basin_array))] = basin_size

def CountBasinSize(mirror, real, r, c):
  prev_count = np.count_nonzero(mirror)
  MirrorArrayFill(real, r, c)
  curr_count = np.count_nonzero(mirror)
  basin_size = curr_count - prev_count
  return basin_size

def FindBasins():
  largest_three_basins = []
  for r in range(rows_len):
    for c in range(cols_len):
      if LowPoint(array, r, c):
        AddToBasin(largest_three_basins, CountBasinSize(mirror_array, array, r, c))
  return np.prod(largest_three_basins)         

print(FindBasins())
