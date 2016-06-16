#!/usr/bin/python

Shop_list = {'iphone': 6000, 'mac': 10000, 'tea': 100}             #先设定好商品列表
print('商品列表：', Shop_list.items())                             #输出商品列表给客户，供选择
name = []                                                          #创建一个list，用于临时存储客户选择的物品
gou_lis = []                                                        #创建一个list，购物车
Money = 0                                                           #新建一个数字Money，购物车商品金额累计
Balance = 15000                                                     #新建一个余额数字，
#购物环节
while True:
    name = input('请参照商品列表，输入想要购买的商品名称:')
    if name in Shop_list.keys():                                       #判断客户选择的物品是否在商品列表中
        gou_lis.append(name)                                            #如果在，追加到购物车列表中
        print(gou_lis)                                                  #打印当前购物车的商品列表
        if input('继续购物请按任意键继续，如果要结算请输入Y::') == 'y':     #判断用户继续购物还是去结算
            for n in gou_lis:                                           #如果结算循环购物车里的商品，从商品列表中取出商品对应的价格进行累加
                Money += Shop_list.get(n)
            print('购物车内的商品是：', gou_lis)
            print('购物金额为：', Money)
            break
        else:                                                              #如果没有输入y，输入任意键跳出本次循环，让用户冲洗输入想要购买的商品
            continue
    else:                                                               #如果判断客户选择的物品不在商品列表中，就打印不存在，重新进入循环
        print('您输入的商品不存在，请重新输入')
#进入结算环节，如果余额不足请充值或者清理购物车
while True:
    if Balance >= Money:                                    #如果购物车里的商品总金额小于余额的话，请客户选择是否支付
            if input('确认是否支付:') == 'y':                #请客户再次确认是否付款，确定的话直接从余额中扣除
                Balance -=  Money
                print('您付款后的余额是:', Balance)
            else:
                print('欢迎下次光临！！！')
            break
    else:
        print('您的购物金额已超过您的余额，请清理您的购物车或者充值.输入a充值|输入b清理购物车')   #清理购物车或者充值
        if input() == 'a':                                                                      #充值
            # print(type(Balance))
            Balance += int(input('请输入充值金额'))                                            #给客户充值
            print('您现在的余额是:', Balance)
        else:
            print('清理购物车,')
            del_name = input('请选择并输入购物车里放弃购买的商品名称：')                        #客户输入要清理的商品名称
            for n in range(0,3):                                                            #循环3次，如果客户输入的商品都不正确，直接退出
                if del_name in gou_lis:                                         #判断清理的商品是否存在购物车
                    gou_lis.remove(del_name)                                    #如果存在，则删除
                    print('当前购物车里的物品：', gou_lis)                       #打印当前购物车里的商品
                    if input('是否要结算,y|n') == 'y':                           #询问是否结算
                        Money = 0                                               #初始化购物车金额
                        for n in gou_lis:                                       #循环累加购物车商品的金额
                            Money += Shop_list.get(n)
                            print('购物车内的商品是：', gou_lis)
                            print('购物金额为：', Money)
                        break
                else:
                    print('您输入的商品不在购物车，请重新输入')                      #如果清理购物车时输入的商品名称不在购物车中，提示客户重新输入要放弃购买的商品
