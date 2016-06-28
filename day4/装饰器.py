# def  foo():
#     print('i am foo')
#
#
# foo()

import logging
# def use_logging(func):
#
#     def wrapper(*arg,**kwargs):
#         logging.warn("%s is running"%func.__name__)
#         return func(*arg,**kwargs)
#     return wrapper
#
# def bar(name ):
#     print('i am bar %s:%s+%s' %name )
#
# bar = use_logging(bar)
# bar('bobo')
#


def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator

@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s" % name)

foo()

