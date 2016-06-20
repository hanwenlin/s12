#函数默认是没有参数的
# show():--->show()

#一个参数
# def show(arg):
#     print(arg)
# show('klkkk')

#两个参数
# def show(arg,xxx):
#     print(arg,xxx)
# show('kkk','777')


#默认参数，必须放在后面
# def show(a1,a2=999):
#     print(a1,a2)
# show(111)  #只赋值一个输出的结果是111 999
# show(111,222)#两个参数都赋值，输出结果111 222

#指定参数，指定参数名称赋值，可以打乱形参顺序，，输出结果111 999
def show(a1,a2):
    print(a1,a2)
show(a2=999,a1=111)
