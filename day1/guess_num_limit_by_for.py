
luck_num = 6

for i in range(0,3):
    guess_num = raw_input("Pls input your guess_num:");
    if guess_num == luck_num:
        print("bingo!")
        break
    elif guess_num < luck_num:
        print("your guess_num so big!")
    else:
        print("your guess_num so small!")
print("Entered too many times")
