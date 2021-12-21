import numpy as np

with open('input.txt') as f:
  input = [int(x) for x in f.read().split(',')]


# print(np.array(input))

def fish():
  for days in range(256):
    c = len(input)
    for num in range(len(input)):
      input[num] -= 1
      if input[num] < 0:
        input[num] = 6
        input.append(8)
      
  return input

# print(len(input))
odd = 0
for i in range(1,5,2):
  odd += 2*i**3
  print(odd)

even = 0
for i in range(2,4,2):
  even += 2*i**3
  print(even)

odd*=4
print(odd)



  