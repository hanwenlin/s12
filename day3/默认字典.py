# 原生字典解决办法
values = [11, 22, 33,44,55,66,77,88,99,90]

my_dict = {}

for value in  values:
    if value>66:
        if my_dict.has_key('k1'):
            my_dict['k1'].append(value)
        else:
            my_dict['k1'] = [value]
    else:
        if my_dict.has_key('k2'):
            my_dict['k2'].append(value)
        else:
            my_dict['k2'] = [value]
# 复制代码
# defaultdict字典解决办法
# 默认字典指定了这个字典vlaue默认的类型为list，就不用再初始化了
from collections import defaultdict

values = [11, 22, 33,44,55,66,77,88,99,90]

my_dict = defaultdict(list)

for value in  values:
    if value>66:
        my_dict['k1'].append(value)
    else:
        my_dict['k2'].append(value)