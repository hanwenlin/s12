# '''
# bytearray([source [, encoding [, errors]]])
# 中文说明：
# bytearray([source [, encoding [, errors]]])返回一个byte数组。Bytearray类型是一个可变的序列，并且序列中的元素的取值范围为 [0 ,255]。
#
# 参数source:
#
# 如果source为整数，则返回一个长度为source的初始化数组；
#
# 如果source为字符串，则按照指定的encoding将字符串转换为字节序列；
#
# 如果source为可迭代类型，则元素必须为[0 ,255]中的整数；
#
# 如果source为与buffer接口一致的对象，则此对象也可以被用于初始化bytearray.。
# '''
# p = bytearray('张君',encoding='utf-8')
# print(p)
#
# p = bytes('张君',encoding='utf-8')
# print(p)
# a = bytearray(1)
# print(a)
#
#
# chr()将数字转换成字符
# ord()将字符转换成数字
#


# filter
li = [11, 22, 33, 44, 55]
def func(x):
    if x > 33:
        return True
    else:
        return False

n = filter(func,li)
list(n)