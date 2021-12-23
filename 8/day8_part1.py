# 1 -> 2
# 7 -> 3
# 4 -> 4
# 2,3,5 -> 5
# 0, 6,9 -> 6
# 8 -> 7

import re

with open("input.txt") as f:
    contents = f.read()
    x = re.split('\n|\|',contents)

ans = []
for line in x:
  if x.index(line) % 2 != 0:
    ans += line.split()

c = 0
for num in ans:
  if len(num) in [2,3,4,7]:
    c+=1
print(c)
