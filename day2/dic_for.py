dic = {}           #创建一个空字典
all_list = [11,22,33,44,55,66,77,88,99,] #创建一个列表
for i in all_list:                  #for循环去遍历整个列表中的每个元素
    if i > 60:                       #把大于60的元素取出来
        if 'k1'in  dic.keys():      #判断key'k1'是否在字典里
            dic['k1'].append(i)      #如果k1在字典的keys中则把i追加到k1列表中
        else:
            dic['k1'] = []        #如果k1不在dic字典的keys中，则在字典dic中创建key=k1,k1的valus为列表，列表中包含了i或者一个空list
    else:
        if  'k2' in dic.keys():
            dic['k2'].append(i)
            pass
        else:
            dic['k2'] = []
print(dic.items())              #输出dic字典的key对应的valus

# dict_items([('k1', [77, 88, 99]), ('k2', [22, 33, 44, 55])])