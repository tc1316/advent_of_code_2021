with open('input.txt') as f:
  input = [list(line.strip()) for line in f]

pairs = { ')':'(', ']':'[', '}':'{','>':'<'}

points = { ')':3, ']':57, '}':1197,'>':25137 }


def FindCorrupted():
  score = 0
  for line in input:
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
          score += points[char]
          break
      else:
        stack.append(char)
  return score
  
print(FindCorrupted())