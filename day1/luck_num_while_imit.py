__author__ = 'zhangjun'

luck_num = 6
input_num = -1

guess_count = 0
#while input_num != luck_num:
#while input_num != luck_num and guess_count < 3:
while  guess_count < 3:
    print("guess num:",guess_count)
    input_num = int(input("input my lucky num:"))

    if input_num < luck_num:
        print("so small!")
    elif input_num > luck_num:
        print("so big!")
    else:
        print("bingo!")
        break
#   guess_count = guess_count + 1
    guess_count += 1
# if luck_num == input_num:
#     print("bingo!")
else:
    print("input too mach")