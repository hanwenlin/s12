#可命名元祖需要先创建类，这个方法仍然是collections模块提供，先导入，使用其nametuple的方法创建可命名元祖之后，就可以通过元祖里面元素名称访问了。
import collections

MytupleClass = collections.namedtuple('MytupleClass',['x', 'y', 'z'])

obj = MytupleClass(11,22,33)
print(obj.x)
print(obj.y)
print(obj.z)