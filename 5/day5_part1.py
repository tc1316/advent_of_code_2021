import numpy as np

input = []
with open('input.txt') as f:
  for row in f:
    input += [row.split(',') for row in [x.strip() for x in row.split('->')]]

nums = [[int(item) for item in row] for row in input]

lines = []
for i in range(0,len(nums),2):
  lines.append(np.array(nums[i:i+2]))


def exclude_diagonals():
 filtered_lines = []
 for coords in lines:
   if np.all(coords[0][0] == coords[1][0]) or np.all(coords[0][1] == coords[1][1]):
    filtered_lines.append(coords)
 return filtered_lines

# print(exclude_diagonals()[0:5])

# [[x1, y1],[x2, y2]]
# x1 = 1st column
# x2 = 2nd column
# y1 = 1st row
# y2 = 2nd row
# [COLUMN1, ROW1]

def line_creator():
  empty = np.zeros((1000,1000))
  input = exclude_diagonals()
  for coords in input:
    fills = np.zeros((1000,1000))
    y1 = coords[0][1]
    y2 = coords[1][1]
    x1 = coords[0][0]
    x2 = coords[1][0]
    print(f"Column1= {x1}", f"Row1= {y1}",f"Column2= {x2}", f"Row2= {y2}") 
    if np.all(y1 == y2): # If y1 = y2 (rows)
      if x1 < x2:
        fills[y1,x1:x2+1] = 1
        empty += fills
      elif x1 > x2:
        fills[y1,x2:(x1+1)] = 1
        empty += fills
    if np.all(x1 == x2): # If x1 = x2 (columns)
      if y1 < y2:
        fills[y1:y2+1,x1] = 1
        empty += fills
      elif y1 > y2:
        fills[y2:y1+1,x1] = 1
        empty += fills
  return (empty>=2).sum()

print(line_creator())


 
