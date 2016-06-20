#函数的定义
def mail():
    n = 123
    n += 1
    print(n)
    return 123
#跟if一样通过缩进来控制代码块
#函数的调用
mail()
#函数的重新赋值
f = mail
#如果将函数名称赋值给另外一个字符串的话，使用另外一个名称也可以直接执行
f()

ret = mail()
print(ret)
