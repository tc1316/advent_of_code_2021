from __future__ import barry_as_FLUFL
import numpy as np
from operator import itemgetter

input = []
with open('input.txt') as f:
  for line in f:
    input += line.splitlines()
  coords = [tuple(x.split(',')) for x in input[0:input.index('')]]
  instructions = [x.split('=') for x in input[input.index('')+1:]]

int_coords = []
for x,y in coords:
  int_coords.append((int(x), int(y)))

x_len = max(int_coords,key=itemgetter(0))[0]+1
y_len = max(int_coords,key=itemgetter(1))[1]+1
blank_paper = np.zeros((y_len,x_len))
print(np.shape(blank_paper))

def MarkPaper(bp):
  for x,y in int_coords:
    bp[y][x] = 1
  return bp

def FirstFoldPaper(instr,array):
  fold = instr[0]
  fold_at = int(fold[1])
  if 'y' in fold[0]:
    orig = array[:fold_at,:] 
    flipped = np.flipud(array[fold_at+1:,:])
    # Need to add conditions for weird y-folding cases
    array = np.add(orig, flipped)
    print(array)
  elif 'x' in fold[0]:
    orig = array[:,0:fold_at] 
    flipped = np.fliplr(array[:,fold_at+1:])
    if np.shape(orig) != np.shape(flipped):
      dif = np.shape(orig)[1] - np.shape(flipped)[1]
      flipped = np.c_[np.zeros((y_len,dif)),flipped]
    array = np.add(orig,flipped)
  return np.count_nonzero(array)

print(FirstFoldPaper(instructions, MarkPaper(blank_paper)))

