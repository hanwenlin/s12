import copy
dic = {
    'cpu' :[80,],
    'mem' :[80,],
    'disk':[80,]
}
print('before:',dic)

new_dic = copy.deepcopy(dic)
new_dic['mem'][0]=50
print('深拷贝的结果')
print(dic)
print(new_dic)
print('浅拷贝的结果')
new1_dic = copy.copy(dic)
new1_dic['mem'][0]=30
print(dic)
print(new1_dic)

# 结果
# before: {'cpu': [80], 'disk': [80], 'mem': [80]}
# 深拷贝的结果
# {'cpu': [80], 'disk': [80], 'mem': [80]}
# {'cpu': [80], 'disk': [80], 'mem': [50]}
# 浅拷贝的结果
# {'cpu': [80], 'disk': [80], 'mem': [30]}
# {'cpu': [80], 'disk': [80], 'mem': [30]}