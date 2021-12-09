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


def bingo():
  for i in random:
    count = 0
    for board in boards:
      board[board==i] = -1
           
      for r in range(board.shape[0]):
        if np.all(board[r]==-1):
          return [i,boards[count % len(boards)]]
          
      for c in range(board.T.shape[0]):
        if np.all(board.T[c] == -1):
          return [i,boards[count % len(boards)]]
      
      count += 1

winning_number =  bingo()[0]
bingo_array = bingo()[1]

def sum_unmarked(arr):
  return int(np.sum(arr, where=arr >-1))

print(sum_unmarked(bingo_array)*winning_number)
