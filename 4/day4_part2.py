import numpy as np

random = []
with open('random.txt') as f:
  for line in f:
    random += [int(x) for x in line.split(',')] 

rows = []
with open('bingo.txt') as f:
    rows += filter(None,[[int(x) for x in line.split()] for line in f])

boards = [] 
for i in range(0,len(rows),5):
  boards.append(np.array(rows[i:i+5]))

def sum_unmarked(arr):
  return int(np.sum(arr, where=arr >-1))

def bingo():
  for i in random:
    for board in boards:
      board[board==i] = -1
            
      for r in range(board.shape[0]):
        if (np.all(board[r] == -1) or np.all(board[:,r] == -1)):
          val = sum_unmarked(board)
          currenthighest = val*i
          board.fill(-2) # Marks bingo'd boards as uncheckable next iteration
  return currenthighest

print(bingo())