'''
def  show(*args):
    print(*args,type(args))
show(1,2,3.4)
show('abcmdsklsdkewnk,v')
输出结果
1 2 3.4 <class 'tuple'>
abcmdsklsdkewnk,v <class 'tuple'>
'''
def show(*args,**kwargs):
    print(args,type(args))
    print(kwargs,type(kwargs))
# show(1,1,2,2,3,4,'lsl,xzldsjkjlkmxklcjsjakld,xc',n1=88,alex='sb',k1='v1',k2='v2')
# # 输出的结果：
# (1, 1, 2, 2, 3, 4, 'lsl,xzldsjkjlkmxklcjsjakld,xc') <class 'tuple'>
# {'alex': 'sb', 'k2': 'v2', 'k1': 'v1', 'n1': 88} <class 'dict'>
# 两个动态参数，可以接收任何形式的数据类型，没有=号的统统接收为元组，有等号的接收为字典
#写参数的时候把一个*的放前面，两个*的放后面。执行的时候也是这样的顺序，否则会报错

l = [1,2,3,4,5]
b = {'n1':888,'alex':'sb'}
'''
show(l,b)
输出结果是
([1, 2, 3, 4, 5], {'alex': 'sb', 'n1': 888}) <class 'tuple'>
{} <class 'dict'>
'''

# 如果在使用函数的动态参数功能的时候，想传入参数是列表或者字典的时候，
# 设置好变量之后，在运行的时候设置形参的时候，也要加上一个*和两个**

show(*l,**b)
# 输出结果
# (1, 2, 3, 4, 5) <class 'tuple'>
# {'alex': 'sb', 'n1': 888} <class 'dict'>