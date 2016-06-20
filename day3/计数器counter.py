import collections    #导入模块，因为不常用所有默认没有被导入
obj= collections.Counter('adfdfcvgsdfdfggfd.')
print(obj)
ret = obj.most_common(4)
print(ret)

for k in obj.elements():
    # print(item)
    print(k)
#因为计数器继承了dict的类，所以他也继承了字典所有的方法
for k,v in obj.items():
    print(k,v)
    # 下面是输出

#     C:\Users\zhangjun\AppData\Local\Programs\Python\Python35\python.exe C:/Users/zhangjun/PycharmProjects/s12/day3/counter.py
# Counter({'f': 5, 'd': 5, 'g': 3, '.': 1, 'c': 1, 'a': 1, 'v': 1, 's': 1})
# [('f', 5), ('d', 5), ('g', 3), ('.', 1)]
# .
# f
# f
# f
# f
# f
# g
# g
# g
# d
# d
# d
# d
# d
# c
# a
# v
# s
# . 1
# f 5
# g 3
# d 5
# c 1
# a 1
# v 1
# s 1
#
# Process finished with exit code 0
