from enum import unique
import re

with open("test.txt") as f:
  contents = f.read()
  x = re.split('\n|\|',contents)

nl = [[''.join(sorted(chars)) for chars in x] for x in [line.split() for line in x]]
encoded = [code for code in nl if nl.index(code) % 2 == 0]
ans = [v for v in nl if nl.index(v) % 2 != 0]
unique_num_dict = { 2:1, 4:4, 3:7, 7:8 }

class GetNums():
  def get_unique_nums():
    list_of_configs = []
    for list in encoded:
      config = {}
      for i in list:
        if len(i) in unique_num_dict.keys():
          config.update({unique_num_dict[len(i)]: i})
      list_of_configs.append(config)
    return list_of_configs


  # def get_top_horizontal():
  #   top_horizontal = sorted(set([char for char in config[7]]) ^ set([char for char in config[1]]))[0]

  def get9(cfg_list):
    for list in encoded:
      for config in cfg_list:
        for i in list:
          nine_trial = sorted(set(config[7] + config[4]))
          nine_remainders = sorted(set(nine_trial) ^ set([char for char in config[8]]))
          for j in nine_remainders:
            x = sorted(nine_trial + [j])
            if "".join(x) == i:
              # bottom_horizontal = j
              # print(bottom_horizontal)
              config.update({9: i})
              # bottom_left_vertical = nine_remainders[(nine_remainders.index(j)+1) % 2]
              # print(bottom_left_vertical)
    return cfg_list
     
  def get5(cfg_list):
    for list in encoded:
      for config in cfg_list:
        for i in list:
          five_trial = sorted(set([char for char in config[9]]) ^ set([char for char in config[1]]))
          five_remainders = sorted(set(five_trial) ^ set([char for char in config[9]]))
          for j in five_remainders:
            x = sorted(five_trial + [j])      
            if "".join(x) == i:
              # bottom_right_vertical = j
              # print(bottom_right_vertical)
              config.update({5: i})
              # top_right_vertical = five_remainders[(five_remainders.index(j)+1) % 2]
              # print(top_right_vertical)
    return cfg_list

  def get6(cfg_list):
    for list in encoded:
      for config in cfg_list:
        for i in list:
          six_trial = sorted(set(config[5]))
          six_remainders = sorted(set([char for char in config[8]]) ^ set(six_trial))
          for j in six_remainders:
            x = sorted(six_trial + [j])      
            if "".join(x) == i:
              # top_left_vertical = j
              # print(top_left_vertical)
              config.update({6: i})
              # middle_horizontal = zero_remainders[(zero_remainders.index(j)+1) % 2]
              # print(middle_horizontal)
    return cfg_list

  
  def get(cfg_list):
    for list in encoded:
      for config in cfg_list:
        for i in list:
          six_trial = sorted(set(config[5]))
          six_remainders = sorted(set([char for char in config[8]]) ^ set(six_trial))
          for j in six_remainders:
            x = sorted(six_trial + [j])      
            if "".join(x) == i:
              # top_left_vertical = j
              # print(top_left_vertical)
              config.update({6: i})
              # middle_horizontal = zero_remainders[(zero_remainders.index(j)+1) % 2]
              # print(middle_horizontal)
    return cfg_list

# unfinished
    