# data = list(range(1,6000,3))
# # print(data)
# i = 601
# if i in data:
#     print(i)
# else:
#     print('不存在')


def binary_search(data_source,find_n):
    mid = int(len(data_source)/2)
    if len(data_source) >=1:
        if data_source[mid] > find_n:#data in left
            # print("data in left of [%s]")
            print(data_source[:mid])
            binary_search(data_source[:mid],find_n)
        elif data_source[mid] < find_n:#data in right
            # print("data in right of [%s]")
            print(data_source[mid:])
            binary_search(data_source[mid:],find_n)
        else:
            print("found find_s,",data_source[mid])
    else:
        print("cannot found")

if __name__ =='__main__':
    data = list(range(1,600000))
    binary_search(data,1)