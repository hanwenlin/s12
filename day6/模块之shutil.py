#高级的文件，文件夹，压缩包处理模块
import shutil
# shutil.copyfileobj(fsrc, fdst, length=16*1024)#拷贝文件对象
'''
def copyfileobj(fsrc, fdst, length=16*1024):
    """copy data from file-like object fsrc to file-like object fdst"""
    while 1:
        buf = fsrc.read(length)
        if not buf:
            break
        fdst.write(buf)
'''
# open('模块.txt',) as f:
# shutil.copyfileobj('s6.py','copy.file',length=16*1024)
# shutil.copyfile('s6.py','s6.test.txt') #拷贝文件
# shutil.copymode('s6.py','s6.test.txt')#仅拷贝权限。内容、组、用户均不变
# shutil.copystat('s6.py','s6.test.txt')#拷贝状态信息，包括：mode bits, atime, mtime, flags
# shutil.copy('s6.py','s6.test.txt')#拷贝文件和权限
# shutil.copy2('s6.py','s6.test.txt')#拷贝文件和状态信息
# guize = shutil.ignore_patterns('*.txt')
# shutil.copytree('C:/Users\\zhangjun\\PycharmProjects\\s12\\day6\\', 'C:/Users\\zhangjun\\PycharmProjects\\s12\\day6\\shuitl_test\\', ignore=guize)#递归的去拷贝文件可以设置忽略规则
# shutil.rmtree('C:/Users\\zhangjun\\PycharmProjects\\s12\\day6\\shuitl_test\\')
# shutil.move('C:/Users\\zhangjun\\PycharmProjects\\s12\\day6\\Test1\\','C:/Users\\zhangjun\\PycharmProjects\\s12\\day6\\fuck\\')
# ret = shutil.make_archive('wwwwwwwwww','gztar',root_dir='C:/Users\\zhangjun\\PycharmProjects\\s12\\day6\\fuck\\')
# 上面命令会在此路径下生成一个wwww.tar.gz文件C:\Users\zhangjun\PycharmProjects\s12\day6\wwwwwwwwww.tar.gz
# 压缩

import tarfile
# 压缩
# tar = tarfile.open('your.tar','w')
# tar.add('C:/Users\\zhangjun\\PycharmProjects\\s12\\day6\\fuck\\hash模块.py', arcname='hash.zip')
# tar.add('C:/Users\\zhangjun\\PycharmProjects\\s12\\day6\\fuck\\正则test.py', arcname='正则.zip')
# tar.close()
# 解压缩
# tar = tarfile.open('your.tar','r')
# tar.extractall(path='C:/Users\\zhangjun\\PycharmProjects\\s12\\day6\\解压缩')#可以设置解压地址
# tar.close()
import zipfile
#压缩
z = zipfile.ZipFile('laxi.zip','w')
z.write('db')
z.write('s6.py')
z.close()
#解压
z = zipfile.ZipFile('laxi.zip','r')
z.extractall('C:/Users\\zhangjun\\PycharmProjects\\s12\\day6\\解压缩')#可以设置路径密码等功能
z.close()