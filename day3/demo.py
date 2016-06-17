# 数据库中原有
old_dict = {
    "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#2":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
}
  
# cmdb 新汇报的数据
new_dict = {
    "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 800 },
    "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#4":{ 'hostname':'c2', 'cpu_count': 2, 'mem_capicity': 80 },
}
#
# 需要删除：？
# 需要新建：？
# 需要更新：？ 注意：无需考虑内部元素是否改变，只要原来存在，新汇报也存在，就是需要更新
print(old_dict)
print(new_dict)
# 交集
# 更新old_dict
# 更新new_dict
old_set = old_dict.keys()
print(old_set)
update_dict = set(old_dict).difference(new_dict)
print(update_dict)
