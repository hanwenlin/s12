import pickle

l1 = [11,22,33]
r = pickle.dumps(l1)
print(r)


'''结果，转换成了python专门的字符格式。其他语言无法识别
b'\x80\x03]q\x00(K\x0bK\x16K!e.'
'''

result = pickle.loads(r)
print(result)
# 反序列化写入文件
pickle.dump(l1,open('db','wb'))
# 反序列化读取文件
r1 = pickle.load(open('db','rb'))
print(r1)