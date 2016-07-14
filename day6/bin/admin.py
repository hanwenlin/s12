import  sys
import os
#找到执行文件的绝对路径加入system path
res = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(res)
print(res)
