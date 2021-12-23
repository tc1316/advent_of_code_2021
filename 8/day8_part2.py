# Char lens
# 0 -> 6
# 1 -> 2 (unique)
# 2 -> 5
# 3 -> 5
# 4 -> 4 (unique)
# 5 -> 5
# 6 -> 6
# 7 -> 3 (unique)
# 8 -> 7 (unique)
# 9 -> 6


from enum import unique
import re

with open("test.txt") as f:
    contents = f.read()
    x = re.split('\n|\|',contents)

nl = [[''.join(sorted(chars)) for chars in x] for x in [line.split() for line in x]]

encoded = [code for code in nl if nl.index(code) % 2 == 0]
ans = [v for v in nl if nl.index(v) % 2 != 0]

unique_num_dict = { 2:1, 4:4, 3:7, 7:8 }

for list in encoded:
  dict = {}
  for i in list:
    # print(i)
    if len(i) in unique_num_dict.keys():
      dict.update({unique_num_dict[len(i)]: i})
    try:
      trial = sorted(set(dict[7] + dict[4]))
      remainders = sorted(set(trial) ^ set([char for char in dict[8]]))
      
      for j in remainders:
        x = sorted(trial + [j])
        if "".join(x) == i:
          nine = i
      print(nine, i)
    except:
      continue
    
   