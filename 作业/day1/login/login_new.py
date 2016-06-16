user = open("users.db", "r")  # 以只读模式打开用户数据库
use = {}  # 新建一个字典
for n in user.readlines():  # 迭代按行读取用户数据库中的数据
    raw = n.split(' ')  # 读取出来的每行数据做去空格处理
    use[raw[0]] = raw[1].strip()  # 讲每行列表中第一个元素作为key传给use字典，讲第二个元素作为value传给key
# print(use.items())                #开发过程中提示处理
user.close()  # 读取完成后关闭用户数据库文件

lock_list = open('locklist', 'r')  # 以制度模式打开locklist文件，读黑名单文件
lines = []  # 新建一个list
# print(lock_list.readlines())         #开发过程中做提示处理
for line in lock_list.readlines():  # 迭代按行读取黑名单数据，
    # print('line:', line)               #开发过程中提示处理
    lines.append(line.strip())  # 把按行读取出来的列表中的每个元素做去空格处理后，追加到lines中
# print('lock:', lines)                   #开发过程中提示处理
lock_list.close()  # 关闭文件
iii = 0  # 初始化一个变量
for i in range(0, 3):  # 循环三次
    user_name = input("please input your username:")  # 提示用户输入账户
    if len(user_name) == 0:  # 如果用户输入的用户名为空
        print("用户名不能为空！")
        continue  # 跳出本次循环，让用户重新输入
    elif user_name in lines:  # 如果用户输入的账户在黑名单list中，
        print("您的账户已经被锁定！")
        break  # 跳出整个循环
    # break
    else:  # 如果用户输入的用户名不为空，同时也不在黑名单中
        if user_name in use.keys():  # 如果用户输入的用户名正确，在数据库中能够找到
            if use.get(user_name) == input('请输入您的密码1：'):  # 提示用户输入密码，同时通过字典取值对比密码是否正确
                print("恭喜您登陆成功！")  # 正确，提示成功，并推出整个程序
                break
            else:  # 如果用户名存在数据库中，但是输入的密码不正确
                for ii in range(0, 3):  # 给用户三次机会，重新输入
                    if use.get(user_name) == input('请输入您的密码2：'):  # 用户重新输入了密码，通过字典取值做对比
                        print("恭喜您登陆成功！")  # 如果正确，提示成功，推出程序
                        break
                    else:  # 如果用户密码仍然输错，那么他还有两次输错密码的机会，超过第三次输入错误的密码，用户将被锁定
                        iii += 1  # 计数器累加
                        if iii == 2:  # 当计数器的数值达到3的时候，锁定用户
                            print('您的账户：', user_name, '被锁定!')
                            # print(user_name)
                            lock_list = open('locklist', 'a+')
                            lock_list.write(user_name + '\n')  # 持久化存储，存入本地文件，尾部做换行处理
                            lock_list.close()  # 关闭文件
                            exit()  # 推出整个程序
        else:  # 如果用户的用户名不为空，也没有被锁定，同时在用户数据库中找不到这个用户名
            print("账户不存在，请重新确认")










            #
            #     if user_name == line:
            #         print("您的账户已锁定")
            #     elif user_name in use.keys():
            #         if use.get(user_name) == input('请输入您的密码：'):
            #             print("恭喜您登陆成功！")
            #             break
            #         else:
            #             for i in range(0, 3):
            #                 if use.get(user_name) == input('请输入您的密码：'):
            #                     print("恭喜您登陆成功！")
            #                     break
            #                 else:
            #                     i += 1
            #                     if i == 2:
            #                         print('您的账户：', user_name, '被锁定!')
            #                         print(user_name)
            #                         lock_list = open('locklist.db', 'a+')
            #                         lock_list.write(user_name + '\n')
            #                         lock_list.close()
            #                         break
            #             break
            #         break
            #
            #
            #     else:
            #         if len(user_name) == 0:
            #             print("用户名不能为空，请重新输入")
            #         else:
            #             print("输入的账户错误，请重新输入")
            #         break
            #     break
            # continue
