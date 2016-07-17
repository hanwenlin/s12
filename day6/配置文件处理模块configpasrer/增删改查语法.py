# [section1]
# k1 = v1
# k2:v2
#
# [section2]
# k1 = v1

import configparser

config = configparser.ConfigParser()
config.read('example.ini')

########## 读 ##########
#读取整个配置文件的分段，按列表输出
secs = config.sections()
print(secs)
# ['bitbucket.org', 'topsecret.server.com']


# 读取指定的选项
options = config.options(secs[0])
print(options)
# ['user', 'serveraliveinterval', 'compression', 'compressionlevel', 'forwardx11']


item_list = config.items(secs[0])
print(item_list)
#[('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'), ('forwardx11', 'yes'), ('user', 'hg')]


val = config.get(secs[0],options[0])
print(val)
val = config.getint(secs[0],options[1])
#这里发现一个问题，当输出的options为字符串的时候报错。待处理
print(val)

########## 改写 ##########
#删除指定的分段
# sec = config.remove_section('bitbucket.org')
# config.write(open('example2.ini', "w"))
#判断是否有指定的分段，没有的话就添加
# sec = config.has_section('alex')
# sec = config.add_section('alex')
# config['alex']['age']='21'
# config.write(open('example2.ini', "w"))

#修改指定的分段里的选项
# config.set('alex','age','22')
# config.write(open('i.cfg', "w"))
#删除指定的配置部分
# config.remove_option('alex','age')
# config.write(open('i.cfg', "w"))


'''
结果
['bitbucket.org', 'topsecret.server.com']
['user', 'serveraliveinterval', 'compression', 'compressionlevel', 'forwardx11']
[('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'), ('forwardx11', 'yes'), ('user', 'hg')]
hg
45
'''