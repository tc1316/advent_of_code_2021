lines = []
with open('input.txt') as f:
    lines = f.readlines()

print(lines)

n = len(lines[0]) #Length of one binary number

def gamma():
  bits = []
  for i in range(0,n-1):
    tmp = { "zeroes": 0, "ones": 0}
    for line in lines:
      if int(line[i]) == 0:
        tmp["zeroes"] += 1
      elif int(line[i]) == 1:
        tmp["ones"] += 1
    if tmp["zeroes"] > tmp["ones"]:
      bits.append(0)
    else:
      bits.append(1)
  return int("".join(map(str, bits)),2)
  
def epsilon():
  bits = []
  for i in range(0,n-1):
    tmp = { "zeroes": 0, "ones": 0}
    for line in lines:
      if int(line[i]) == 0:
        tmp["zeroes"] += 1
      elif int(line[i]) == 1:
        tmp["ones"] += 1
    if tmp["zeroes"] < tmp["ones"]:
      bits.append(0)
    else:
      bits.append(1)
  return int("".join(map(str, bits)),2)

print(gamma()*epsilon())


  
