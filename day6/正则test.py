import re
import sys
# 字符匹配（普通字符，元字符）：
# 普通字符：大多数字符和字符都会和自身匹配
ret = re.findall('al.x','yuanaleSxalexwupeiqi')
print(ret)
# ['alex']
# 2元字符： . ^  $  *  +  ?  {}  []  |  ()  \
#   . 匹配除换行符以外的任意字符
# 下面把alex中的e换成f照样可以匹配
# 下面把alex中的e换成换行符就匹配不了了

re.findall('al.x','yuanaleSxalexwupeiqi')
['alex']
re.findall('al.x','yuanaleSxalfxwupeiqi')
['alfx']
re.findall('al.x','yuanaleSxal\nxwupeiqi')
[]
#^ 尖角符号 匹配起始位置的字符串
re.findall('^al.x','yuanaleSxalexwupeiqi')
[]
#$  匹配终止位置的字符串
re.findall('al.x$','yuanaleSxalexwupeiqi')
[]
#   .*   指的是字符串中间位置任意字符串0到多次
re.findall('al.*x','yuanaleSxalexwupeiqi')
['aleSxalex']

#  +   指1到多次
re.findall('al.+x','yuanaleSxalexwupeiqi')
['aleSxalex']

#  ？  指0到1次
re.findall('al.?x','yuanaleSxalexwupeiqi')
['alex']

#大括号{}更灵活一些，可以指定几次到几次的匹配，看下面，如果不指定开始的次数的话，就是0
re.findall('al.{1,5}x','yuanaleSxaleeeeexwupeiqi')
['aleSx', 'aleeeeex']
re.findall('al.{1,5}x','yuanaleSxaleeeeeeexwupeiqi')
['aleSx']
# 不指定起始数值
re.findall('al.{,5}x','yuanaleSxaleeeeeeexwupeiqi')
['aleSx']
re.findall('al.{,5}x','yuanaleSxaleeeeeeexwupeiqialx')
['aleSx', 'alx']
#中括号里面的字符不再有特殊意义，表示里面的任意一个字符
#b或者c其中任意一个字符
re.findall('a[bc]d','abd')
['abd']
re.findall('a[bc]d','acd')
['acd']

#a-z任意一个字符，或者说任意一个小写字母
re.findall('a[a-z]d','acd')
['acd']
re.findall('a[a-z]d','accd')
[]
# 上面这个没有匹配到，说明中括号里面任意一个字符，不是多个，如果要匹配多个就要加通配符
re.findall('a[a-z]+d','accd')
['accd']
re.findall('a[a-z]*d','accd')
['accd']
#元字符到中括号里面没有特殊意义了，除了个别的-
# a可以匹配到
re.findall('a[a*]d','aad')
['aad']
# 中括号里面的*也可以匹配到
re.findall('a[a*]d','a*d')
['a*d']
# 如果把中间字符换成d就匹配不到了，说明*在中括号里面只表达自己，没有其他意义了
re.findall('a[a*]d','add')
[]
# 横杠在中括号里面有特殊意义，指的是谁到谁的意思
re.findall('a[1-9]d','add')
[]
re.findall('a[1-9]d','a4d')
['a4d']
#尖角号在中括号中表示非的意思
re.findall('a[^f]d','a4d')
['a4d']
re.findall('a[^f]d','afd')
[]
re.findall('a[^f]d','add')
['add']
#\d  在中括号里表示任意一个数字
re.findall('a[\d]d','a1d')
['a1d']#一个1可以匹配到
re.findall('a[\d]d','a4d')
['a4d']#一个4也可以匹配到
re.findall('a[\d]d','aad')
[]#一个字母就匹配不到了
re.findall('a[\d]d','a11d')
[]#两个数字也匹配不到

# 反斜杠
# 1、反斜杠加上元字符，可以让元字符去掉特殊的功能，就是转义
# 2、反斜杠加上某些普通字符，可以让普通字符变成有特殊功能的字符
# 引用序号对应的字组所匹配的字符串
'''
\d   匹配任何十进制数；他相当于累[0-9]
\D   匹配任何非数字字符；它相当于类 [^0-9]
\s   匹配任何空白字符；  它相当于类  [\t\n\t\f\v]
\S   匹配任何非空白字符；它相当于类  [^ \t\n\r\f\v]
\w   匹配任何字母数字字符；他相当于类 [a-zA-Z0-9_]
\W   匹配任何非字母数字字符；他相当于类 [^a-zA-Z0-9_]
\b:  匹配一个单子便捷，也就是指单词和空格间的位置。
     匹配单词边界（包括开始和结束），这里的“单词”，是指连续的字符、数字和
     下划线组成的字符串。注意，在\b的定义和\w的和\W的交界，
'''

re.findall('I','I am zhanIjun')
['I', 'I']
re.findall(r'I\b','I am zhanIjun')
['I']
re.findall(r'I\b','I$am zhanIjun')
['I']

# 正则的方法
re.match()
re.search()
re.findall()
re.sub()


#1、
# re.match(pattern,string,flags=0)
# 第一个参数是规则，第二个是字符串，第三个参数是编译标志位，用户修改正则表达式的匹配方式，如：是否区分大小写，多行匹配等等

'''
re.match('com','comwww.runcomoob')  #match默认返回一个match的object，要取值，用其中的方法
# <_sre.SRE_Match object; span=(0, 3), match='com'>
re.match('com','comwww.runcomoob').group()
'com'
>>> a.span()
(0, 3)
>>> a.start()
0
>>> a.end()
3
>>> a.end()
3
'''
# sub  查找替换，第一个参数，要找的字符串，第二个参数是要替换的内容，第三个参数是字符串，第四个参数是替换几次
re.sub("g.t","have",'I get A,   Igot B,  I gut C')
'I have A,   Ihave B,  I have C'
re.sub("g.t","have",'I get A,   Igot B,  I gut C',2)
'I have A,   Ihave B,  I gut C'
#subn跟sub唯一的不同是，替换之后把替换次数返回给结果了
re.subn("g.t","have",'I get A,   Igot B,  I gut C')
('I have A,   Ihave B,  I have C', 3)
# split
re.split('\d+','one1tow2three3four4')
['one', 'tow', 'three', 'four', '']

# 6、compile

# re.compile(strPattern[,flag]):
'''
    这个方法是pattern类的工厂方法，用于将字符串的正则表达式便以为
        pattern对象，第二个参数flag是匹配模式，取值可以使用按位或者运算符'|'
        表示同时生效，如果re.I|re.M
    可以把正则表达式编译成一个正则表达式对象，可以把那些经常使用的正则表达式编译成正则表达式对象，这样可以提高效率，下面是一个正则表达式对象的一个例子：
'''
import re
text = "JGood is a handsome boy, he is cool, clever, and so on..."
regex = re.compile(r'\w*oo\w*')
print(regex.findall(text))
['JGood', 'cool']
#查找所有包含'oo'的单词
#如果正则只用一次的话效率没什么影响，如果用多次的话，先编译成正则表达式对象这种方法效率更高

# 正则表达式中匹配\的话要用四个\来匹配，python中默认要用\来转义\。正则也需要用\来转义，所有四个\正则匹配出来交给python还剩下两个\
a=re.search('\\\\','www.run\comoob')
a.group()
'\\'
#用r的意义就是原生字符串的意思
a=re.search(r'\\','www.run\comoob')
a
# <_sre.SRE_Match object; span=(7, 8), match='\\'>
#例如\d在asiic码中就有特殊功能，要用\d匹配数字的时候就要用r，声明匹配规则中的\d是原生字符串
# 还有\a
a=re.search(r'\da','4aaa')
a
# <_sre.SRE_Match object; span=(0, 2), match='4a'>



