反射

实例：伪造Web框架路由系统

反射：基于字符串的形式去对象（模块）中操作其成员
        getattr ,delattr,setattr,hasattr
扩展：导入模块
        import XXX
        from XXX  import oooo
        
        obj = __import__("xxx")
        obj = __import__("xxx.oo.xxx",fromlist=True)