#字符串格式
'''
s1 = "{0} is {1}"
l = ['alex','sb','dd']
# result = s1.format('alex','sb')
result = s1.format(*l)
print(result)
'''
'''
s1 = '{name} is {acter}'

result = s1.format(name='alex',acter='sb')
print(result)
'''
'''
s1 = "{name} is {acter}"
d = {'name':'alex','acter':'sb'}
result = s1.format(**d)
print(result)
'''
func = lambda a: a+1

# 创建形式参数a
# 函数内容 a+1 并把结果return
ret = func(99)
print(ret)