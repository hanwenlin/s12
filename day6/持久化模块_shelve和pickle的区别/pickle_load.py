import pickle

f = open('pickle_test.pkl','rb')
a=pickle.load(f)
print(a)

b=pickle.load(f)
print(b.n)

c=pickle.load(f)
print(c.n)


'''
['alex', 'rain', 'test']
123334
123
'''
# 从这里可以看出，当你通过pickle.dump了三次持久化了，你也可以通过pickle.load三次去读取，每次读取都是按照最后写入以此往前的
#从这里可以看出，这个持久化和shelve的区别，这个持久化是写入的逆序读取的，shelve可以在写入是取名，读取可以按照名字进行读取