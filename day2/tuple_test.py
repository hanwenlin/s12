l1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100, ]
# tup = tuple(l1)
# print(tup)
# print(type(tup))
# l2 = list(tup)  # 把tuple转换成list
# print(l2)
# print(type(l2))
# print(type(tup))
#
# print(l2.append(100))
# # print(type(l3))
# # print(l3)


# l1 = [11,22,33,44,55,66,77,88,99,00,100]
# print(type(l1))
# print(l1)
#
# tup1 = tuple(l1)           # 把list转换成tuple
# print(type(tup1))
# print(tup1)
#
# l2 = list(tup1)            # 把tuple转换成list
# l2.append(1000)
# print(type(l2))
# print(l2)
# print(type(str(tuple(tup1)))) # 把tuple转换成str
# print(str(tuple(tup1)))
tup1 = (11,22,33,44,55,66,77,88,99,00,100,11,111)
# print(tup1.index(100))
# 10
# print(tup1.__contains__(44))
# print(44 in tup1.__iter__())
# True
# True
print(tup1[0].__le__(44))      #<=
print(tup1[0].__eq__(44))       #==
print(tup1[0].__ge__(44))       #>=
print(tup1[0].__gt__(44))       #>
print(tup1[0].__lt__(44))       #<
print(tup1.__getitem__(1))      #使用角标取对应的key
print(tup1[1])
tup2 = tup1.__new__(l1)
print(tup2)