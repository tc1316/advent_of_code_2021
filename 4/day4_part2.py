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
  mostpasses = 0
  currenthighest = 0
  for i in random:
    count = 0
    for board in boards:
      bingo = False
      board[board==i] = -1
            
      for r in range(board.shape[0]):
        if (np.all(board[r] == -1) or np.all(board[:,r] == -1)) and bingo == False:
          bingo = True
          val = sum_unmarked(board)
          if mostpasses == 0:
            currenthighest = val*i
            mostpasses = count 
          elif count > mostpasses:
            currenthighest = val*i
            mostpasses = count
          board.fill(-2)
    count += 1
  return currenthighest

print(bingo())

# winning_number =  bingo()[0]
# bingo_array = bingo()[1]


# print(sum_unmarked(bingo_array)*winning_number)

