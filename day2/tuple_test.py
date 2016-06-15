l1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100, ]
tup = tuple(l1)  # 把list转换成tuple
print(tup)
print(type(tup))
l2 = list(tup)  # 把tuple转换成list
print(l2)
print(type(l2))

l3 = l2.append(100)
print(l3)
