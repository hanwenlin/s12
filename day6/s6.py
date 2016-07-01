import json


# dic = {"k1":"v1"}
# print(dic,type(dic))
# result = json.dumps(dic)
# print(result,type(result))

'''结果：
{'k1': 'v1'} <class 'dict'>
{"k1": "v1"} <class 'str'>
json.dumps讲python的数据格式转化为json
'''

# 序列化
s1 = '{"k1":123}'
print(s1,type(s1))
dic = json.loads(s1)
print(dic,type(dic))

'''结果
{"k1":123} <class 'str'>
{'k1': 123} <class 'dict'>
'''


'''
json.dumps()
json.loads()
# 上面两个都是在内存之间转换
# 下面两个序列化或者反序列化之后会写入文件，索引参数中要打开文件
json.dump()
json.load()
'''

# li = [11,22,33]
# json.dump(li,open('db','w'))
li = json.load(open('db','r'))
print(type(li),li)

'''结果<class 'list'> [11, 22, 33]'''