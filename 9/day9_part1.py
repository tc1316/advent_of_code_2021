from scipy import signal
import numpy as np

with open('input.txt') as f:
  input = [list(line.strip()) for line in f]
  array = np.array([x for x in input]).astype(int)

rows_len = np.shape(array)[1]
cols_len = np.shape(array)[0]


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

def CalcRisk():
  risk = 0
  for r in range(rows_len):
    for c in range(cols_len):
      if LowPoint(array, r, c):
        risk += array[r][c] + 1
  return risk

print(CalcRisk())