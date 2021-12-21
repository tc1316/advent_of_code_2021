import sys

with open("input.txt") as f:
    contents = f.read().split(',')
    a = [int(num) for num in contents]

ans = sys.maxsize
for x in range(min(set(a)),max(set(a))):
  curr = 0
  for i in range(len(a)):
    pos = abs(a[i] - x)
    curr += (pos*(pos+1))/2
  if curr < ans:
    ans = curr

print(ans)




    