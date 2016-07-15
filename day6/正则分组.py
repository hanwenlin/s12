import re

# origin = "has dfafafadfdas098u29341"
# # r = re.match("h\w+",origin)
# # r = re.match("h(\w+)",origin)#分组
# r = re.match("h(?P<name>\w+)",origin) #分组命名?P<name>
#
# print(r.group())#获取匹配到的所有结果
# print(r.groups())#获取分组匹配到的结果
# print(r.groupdict())
'''
has
('as',)
{'name': 'as'}
'''
# match和search的分组一样，没有特殊的，findall有特殊的
origin = "hasaabc dfafafadf halaabc das098u29341"
r = re.findall("h(\w+)a(ab)c",origin)
print(r)
# [('as', 'ab'), ('al', 'ab')]  分组就是在整体正则匹配出的结果中再匹配取值


origin = "hello alex bcd alex lge alex acd 19"
r = re.split("alex",origin,1)
print(r)
# ['hello ', ' bcd alex lge alex acd 19']
r = re.split("(alex)",origin,1)
print(r)
# ['hello ', 'alex', ' bcd alex lge alex acd 19']
r = re.split("a(le)x",origin,1)
print(r)
# ['hello ', 'le', ' bcd alex lge alex acd 19']
r = re.split("(a(le)x)",origin,1)
print(r)
# ['hello ', 'alex', 'le', ' bcd alex lge alex acd 19']