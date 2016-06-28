
def outer(func):
    def inner(*args,**kwargs):
        print('before')
        r = func(*args,**kwargs)
        print("after")
        return r
    return inner

@outer
def f1(arg):
    print(arg)
    return "砍你"
@outer
def f2(*args,**kwargs):
    print(*args,**kwargs)
