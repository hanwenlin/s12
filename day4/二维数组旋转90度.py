# data = [[col  for col in range(4)] for row in range(4)]
'''
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]
'''
# for row in data:
#     print(row)
# print('----------')
#
# for r_index,row in enumerate(data):
#     print('#----------#')
#     for c_index in range(r_index,len(row)):
#         tmp = data[c_index][r_index]
#         data[c_index][r_index] = row[c_index]
#         data[r_index][c_index] = tmp
#         print('-----')
#         for r in data:
#             print(r)


data = [[col for col in range(4)] for row in range(4)]
for i in range(len(data)):
    a = [data[i][i] for row in range(4)]
    print(a)