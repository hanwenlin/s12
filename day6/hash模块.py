import hashlib

obj = hashlib.md5(bytes('oldboy',encoding='utf-8')) #防止撞库，两次加密，在此基础上加密下面的str
obj.update(bytes('123',encoding='utf-8'))#指定要加密的str。
result = obj.hexdigest()
print(result)


import sys
sys.exit(1)