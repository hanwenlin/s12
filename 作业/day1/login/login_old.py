user = open("users.db", "r")
use = {}
for n in user.readlines():
    raw = n.split(' ')
    use[raw[0]] = raw[1].strip()
print(use.items())
user.close()

lock_list = open('locklist.db', 'r')
lock = []
print(lock_list.readlines())
i = 0

while True:
    user_name = input("please input your username:")
    for line in lock_list.readlines():
        line = line.strip('\n')
        if user_name == line:
            print("您的账户已锁定")
        elif user_name in use.keys():
            if use.get(user_name) == input('请输入您的密码：'):
                print("恭喜您登陆成功！")
                break
            else:
                for i in range(0, 3):
                    if use.get(user_name) == input('请输入您的密码：'):
                        print("恭喜您登陆成功！")
                        break
                    else:
                        i += 1
                        if i == 2:
                            print('您的账户：', user_name, '被锁定!')
                            print(user_name)
                            lock_list = open('locklist.db', 'a+')
                            lock_list.write(user_name + '\n')
                            lock_list.close()
                            break
                break
            break


        else:
            if len(user_name) == 0:
                print("用户名不能为空，请重新输入")
            else:
                print("输入的账户错误，请重新输入")
            break
        break
    continue
