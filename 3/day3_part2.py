lines = []
with open('input.txt') as f:
    lines = f.readlines()

n = len(lines[0]) #Length of one binary number

def oxygen(): #Find most common value
  nums = lines

  for i in range(n-1):
    zeroes = 0
    ones = 0

    for num in nums:
      if int(num[i]) == 0:
        zeroes += 1
      elif int(num[i]) == 1:
        ones += 1

    if zeroes > ones:
      nums = [num for num in nums if int(num[i]) == 0]
    elif ones >= zeroes:
      nums = [num for num in nums if int(num[i]) == 1]

    if len(nums) == 1:
      return int(nums[0],2)
  
def co2(): #Find least common value
  nums = lines

  for i in range(n-1):
    zeroes = 0
    ones = 0

    for num in nums:
      if int(num[i]) == 0:
        zeroes += 1
      elif int(num[i]) == 1:
        ones += 1

    if zeroes <= ones:
      nums = [num for num in nums if int(num[i]) == 0]
    elif ones < zeroes:
      nums = [num for num in nums if int(num[i]) == 1]

    if len(nums) == 1:
      return int(nums[0],2)
  
print(oxygen()*co2())
  
