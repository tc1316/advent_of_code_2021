with open('input.txt') as f:
  input = [list(line.strip()) for line in f]

pairs = { ')':'(', ']':'[', '}':'{','>':'<'}

points = { '(':1, '[':2, '{':3,'<':4 }

def FilterCorrupted(lines):
  incomplete = []
  for line in lines:
    stack = []
    for char in line:
      if char in pairs.values():
        stack.append(char)
      elif char in pairs.keys():
        if stack[-1] == pairs[char]:
          stack.reverse()
          stack.remove(pairs[char])
          stack.reverse()
        else:
          stack = []
          break
    if len(stack) != 0:
      incomplete.append(line)
  return incomplete
  

def FindIncompleteChars(lines):
  remainder = []
  for line in lines:
    stack = []
    for char in line:
      if char in pairs.values():
        stack.append(char)
      elif char in pairs.keys():
        if stack[-1] == pairs[char]:
          stack.reverse()
          stack.remove(pairs[char])
          stack.reverse() 
    remainder.append(stack)   
  return remainder

def ReverseIncompleteChars(incomplete_list):
  reversed_incomplete_list = []
  for x in incomplete_list:
    x.reverse()
    reversed_incomplete_list += [x]
  return reversed_incomplete_list

def ScoreCompletion(reversed_incomplete_list):
  scores = []
  for line in reversed_incomplete_list:
    score = 0
    for x in line:
      score *= 5
      score += points[x]
    scores.append(score)
  median = (len(scores)-1) // 2
  return sorted(scores)[median]

x = FilterCorrupted(input)
y = FindIncompleteChars(x)

z = ReverseIncompleteChars(y)


print(ScoreCompletion(z))