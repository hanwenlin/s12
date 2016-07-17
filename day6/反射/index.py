'''
inp字符串类型  inp='login'
两个不相等commons.inp() #commons.login
反射就是利用字符串的形式去对象（模块）中操作（寻找、检查）成员
getattr寻找
hasattr检查
delattr删除
setattr设置

'''
# obj = __import__("commons")

# import commons
# obj.login()
def run():
    #account/login
    inp = input("请输入你要访问的url:")
    m, f = inp.split('/')   #通过分隔符把两个词分开。前面作为模块名，后面作为函数名
    obj = __import__("lib."+m,fromlist=True)     #通过__import__方法把字符串作为模块名导入
    if hasattr(obj,f):      #检查模块中的函数是否存在
        func = getattr(obj,f)   #存在则赋值给func
        func()                  #执行函数
    else:
        print(404)              #如果不存在。输出404



if __name__=='__main__':
    run()