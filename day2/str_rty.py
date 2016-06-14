#__contains__是否包含子序列
# name = 'zhangjun'
# result = name.__contains__('hang')
# print(result)
# capotalize首字符大写
# result = name.capitalize()
# print(result)
#所有字符以小写输出
# result = name.casefold()
# print(result)
#str居中，第一个参数是说总共输出的宽度。第二个参数是在字符两边填充的内容
# result = name.center(30,'*')
# print(result)
# ***********ZHangjun***********
#统计子序列出现的次数
# reslut = name.count('n')
# print(reslut)
# 2
# result = name.count('n',0,5)
# print(result)
# 1
# 字符编码转换
# result = name.encode("gb2312")
# print(result)
# b'\xd6\xb1\xbd\xd3'
# 以什么结尾，可以指定起始位
# result = name.endswith('n',0,4)
# print(result)
#把tab换成空格默认8个空格
# name = 'a\t lex'
# result = name.expandtabs(tabsize=6)
# print(result)
# print(len(result))
# print(name)
# print(len(name))
#find查找子集,找到返回索引位置。找不到返回-1
#可以设置起始位置
name = 'zhangjun'
result = (name.find('j',start=None))
print(result)
