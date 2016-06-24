# enumerate自增序列
'''
li = ['iphone','mac','tea']

for i,items in enumerate(li,100):
    print(i,items)
'''
#eval
print(eval("6*8"))   #直接通过字符串运算
'''
# filter,map #一个做过滤的，一个做条件的
li = [11,22,33,44]
new_li = map(lambda x:x+100,li)
print(list(new_li))
'''
'''
li = [11,22,33,44]
def func(x):
    if x >33:
        return True
    else:
        return False
new_li = filter(func,li)
print(list(new_li))
'''
li = [11,22,33,44]
# 求商数和余数
set = divmod(101,99)
print(set)
(1, 2)
set1 = float.__abs__(-0.123)
print(set1)
set2 = abs(-0.123)
print(set2)

l2 = (11,22,33,44,)
set3 = frozenset.l2
print(set3)

