user  = open("users.db","r")
use = {}
for n in user.readlines():
    raw = n.split(' ')
    use[raw[0]] = raw[1].strip()
print(use.items())
user.close()
lock_list = open('locklist.db','r')
lock = {}
for n in lock_list.readlines():
    raw = n.split(' ')
    lock[raw[0]] = raw[1].strip()
print('lock:',lock)
n = 0
# print(dic)
# print(raw)
# print(raw[0])
# print(raw[1])
while True:
    user_name = input("please input your username:")
    if user_name in lock.keys():
        print("您的账户已锁定")
        break
        print(use)
    elif user_name in use.keys():
        if use.get(user_name) == input('请输入您的密码：'):
            print("恭喜您登陆成功！")
            break
        else:
            for n in range(0,3):

                if use.get(user_name) == input('请输入您的密码：'):
            print("恭喜您登陆成功！")
            break
                n += 1
                if n == 3:
                    print(use[user_name])
    else:
        print("输入的账户错误！")
        break








# for i in range(3):
#     user_name = raw_input("Please input your username:")
#     for

# str