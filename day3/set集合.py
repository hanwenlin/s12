old_dict = {
    "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#2":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 }
}

# cmdb 新汇报的数据
new_dict = {
    "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 800 },
    "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#4":{ 'hostname':'c2', 'cpu_count': 2, 'mem_capicity': 80 },
}




old_set = set(old_dict.keys())
update_list = list(old_set.intersection(new_dict.keys()))

new_list = []
del_list = []

for i in new_dict.keys():
    if i not in update_list:
        new_list.append(i)

for i in old_dict.keys():
    if i not in update_list:
        del_list.append(i)

print(update_list,new_list,del_list)











# print(type(old_dict))
# print(type(new_dict))
#
# s1 = set([1,2,3])
# s2 = set([2,3,4])
# print(type(s1),type(s2))
# s3 = s2.difference(s1)
# print(s3)
# s4 = s1.intersection(s2)
# print(s4)
# s5 = s2.intersection(s1)
# print(s5)
# # s1.intersection_update(s2)
# # print(s1)