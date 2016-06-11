__author__ = 'zhangjun'

luck_num = 6
input_num = -1


while input_num != luck_num:
    input_num = int(input("input my lucky num:"))

    if input_num < luck_num:
        print("so small!")
    elif input_num > luck_num:
        print("so big!")
#   else:
#       print("bingo!")
#       break

print("bingo!")