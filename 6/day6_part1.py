with open('input.txt') as f:
  x = [char.strip().split(",") for char in f]
  input = [int(num) for num in x[0]]


def fish():
  for days in range(80):
    for num in range(len(input)):
      input[num] -= 1
      if input[num] < 0:
        input[num] = 6
        input.append(8)
  
  return input

print(len(fish()))



  