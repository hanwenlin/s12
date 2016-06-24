#__contains__是否包含子序列
name = 'zhangjun'
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
result = name.endswith('n',0,4)
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
# name = 'zhangjjun'
# result = (name.find('j', 5))
# print(result)
#format格式化输出，通过{}占位符，提前设置字符串填充的位置，
# name = 'zhang\t{}\t{}'
# result = name.format('jun','sir')
# print(result)
#通过变量设置
# name = 'zhang\t{sed_name}\t{job}'
# result = name.format(sed_name='jun',job='IT')
# print(result)
#index查找子集
# name = 'zhang'
# result = name.index('b')
# print(result)
# # 如果存在返回子集的索引位置，如果不存在直接报错
#
#isalnum意思是如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
# name = '111aaaaa'
# print(name.isalnum())
# True
#下面这个测试 出了字母数字还有标点符号
# name = 'a..123'
# print(name.isalnum())
# False
#如果string里全部都是字母的话返回真，否则返回假
# name = '11111aaaaaa'
# print(name.isalpha())
# False
# 下面全部都是字母返回真
# name ='aaaaaaaaaa'
# print(name.isalpha())
# True

# 都是十进制的数字返回真，否则返回假
# # string = '123123123e'
# # print(string.isdecimal())
# # False
# 下面这个字符串都是十进制的数字，返回真
# string = '121212120'
# print(string.isdecimal())
# False

#如果字符串至少有一个数字。都是数字返回真，否则返回假
# string = '11'
# print(string.isdigit())
# True
# #判断字符串是否是合法的标识符，字符串仅包含中文字符合法，实际上这里判断的是变量名是否合法。如：
# print('_a'.isidentifier())
# print('3a'.isidentifier())
# print('中国'.isidentifier())
# True
# False
# True
# 中国 = 111
# print(type(中国))
# True
#判断字符串里是内容是否全部可以打印，意思是否含有转义字符
# print('aaaaa'.isprintable())   True
#print('aaaaa\t'.isprintable())   False
#判断字符串里至少有一个字符且全部为空的话为真，
# print(' a '.isspace())  False
# print('  '.isspace())  True
# 判断字符串每个单词的首字母是否大写。字符串必须至少包含一个字母字符，否则返回False。即使首字母字符前面有非字母字符，如中文、数字、下划线等，也不影响对首字母字符的判断。
# ‘中国’.istitle() -->False //字符串不包含字母，返回False
# ‘中国Abc’.istitle() -->True //虽然首字母字符A前面有非字母字符，仍然返回True
# # ‘-Abc xyz’.istitle() -->False //后一个单词的首字母不是大写，返回False
#如果字符串至少有一个，且字母全部都是大写，返回真
# print('1AAA1b'.isupper())
# print('1AAA1'.isupper())
#如果字符串至少有一个，且字母全为小写，返回真
# print('1111a'.islower())
#str为分隔符，后面的元祖和列表中索引插入分隔符
# print('a b'.join(['11','22','33']))     11a b22a b33
# print('a b'.join('112233'))             1a b1a b2a b2a b3a b3
#返回一个长度为width，左对齐的字符串，最右边填充fillchar，默认为空格。width要大于len(str)，否则返回原字符串。如：
# print('ab'.ljust(20,'*'))        ab******************
#把string中所有字母转换为小写
# print('ABc1'.lower())            abc1
'''
str.lstrip([chars])：
返回一个去除前了导字符的新字符串，chars参数是一个字符串，它包含了所有将要被移除的字符集合。默认为空格。
注：关于lstrip函数（包括rstrip和strip），网上有很多文章，但都讲的不清不楚。它实际的意思是，从原字符串的最左边开始，匹配chars里包含的所有字符，直至遇到第一个非chars字符为止，原字符串中匹配到的所有字符都被移除。
‘www.example.com’.lstrip(‘cmowz.’) -->example.com
从字符串的最左边开始匹配，直至遇到了非chars字符e为止，一共匹配了3个w字符和一个.字符，遇到e匹配结束。
'xyxxyy testyx yx yyx'.lstrip('xy ') -->'testyx yx yyx'
从字符串的最左边开始匹配，直至遇到非chars字符t为止，一共匹配了三个x三个y，和一个空格，遇到t匹配结束。

str.rstrip([chars])：
与str.lstrip()相反，从最右边开始匹配。
'xyxxyy testyx yx yyx'.rstrip('xy ') -->'xyxxyy test'

str.strip([chars])：
从字符串的两头开始匹配。
'xyxxyy testyx yx yyx'.strip('xy ') -->test
'''
# print('www.qq.com'.lstrip('cw.'))         qq.com
# print('www.qq.com'.rstrip('com.w'))       www.qq
# print('www.qq.com'.strip('com.w'))          qq
#大小写互换
#print('WWW.qq.COM'.swapcase())         www.QQ.com
#""" 分割， maxsplit最多分割几次 """
#print('www,qq,com'.split(',',0))
# splitlines按行分割，输出list
# string = '''1111111111111
# 222222222222
# 3333333333
# 44444444
# '''
# print(string.splitlines())
# ['1111111111111', '222222222222', '3333333333', '44444444']
# partition分割，前中后三段
# str = 'www.qq.com'
# print(str.partition('.'))
# 拆分 & 组合类方法：
# str.partition(sep)：
# 该方法用于拆分字符串，返回一个包含三个元素的元组。如果未能在原字符串中找到Sep，则元组的三个元素为：原字符串，空串，空串；否则，从原字符串中遇到的第一个Sep字符开始拆分，元组的三个元素为：Sep之前的字符串，Sep字符，Sep之后的字符串；如：
# 'abcdee'.partition('f') --> ('abcdee', '', '')
# 'abcdee'.partition('e') --> ('abcd', 'e', 'e')
#
# str.rpartition(sep)：
# 与str.partition()相反，从原字符串的最右边开始拆分，但是同样返回包含三个元素的元组：倒数第一个Sep之前的字符串，Sep字符，Sep之后的字符串。
# 注意”倒数Sep之前的字符串”，这个之前的字符串，是从原字符串的最左边开始算，并不是最右边。如：
# 'abcdee'.rpartition('e') --> ('abcde', 'e', '') //拆分的三个元素分别是：倒数第一个e之前的元素，e本身，e之后的元素，此外为空格
# 'abcdee'.rpartition('f') --> ('', '', 'abcdee') //拆分的三个元素分别是：空格，空格，原字符串

# 以指定字母开头，可以指定起始位置
# string = 'zhangjun'
# print(string.startswith('h',1,5))
# True
#移除两边的空格
# string = ' zhang jun '
# print(string.strip())
# zhang jun
# str.zfill(width)：
# 返回一个长度为width的数字字符串，最左边填充0。如果width小于等于原字符串长度，则返回原字符串。主要用于数字类字符串的格式化。如：
# 'abc'.zfill(5) --> '00abc' //一般不会做这种格式化，没什么意义
# '123'.zfill(5) --> '00123'
