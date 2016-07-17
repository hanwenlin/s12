import re

origin = "8*12+(6-(5*6-2)/77+2)*(3-7)+8"

def Compute(num):
    if re.findall('([\*|\/|\+|\-])', num,):  # 匹配计算数值长度是否过大,
        e_str = re.findall('([\*|\/|\+|\-])', num,)
        print("e_str:",e_str)
        if len(e_str[0]) == len(num):  # 匹配是否仅剩最后一个数据
            print('returun:',num)
            return int(num)
    # else:
    #     return num
    #     # num = num.replace(str(e_str[0]), str(int(e_str[0])))  # 把长度很大的数转换为整形的字符串
    #     print(num)
    # # new_str = str(num).strip('(,)')  # 去除括号
    total = 0 #初始化为0
    if re.findall('[\*|/]+',num):# 对字符串进行乘除运算，所以先找乘除符号
        new_str = re.search('[\d]+[\*\/]+[\d]+', num)  # 优先匹配**
        print('new_str',new_str.group())
        # print('e_str:',e_str[1])
        if new_str:
            new_str = new_str.group()
            if len(new_str.split('/')) > 1:  # 处理整除运算
                total = float(new_str.split('/')[0]) / float(new_str.split('/')[1])
                print('total',total)
                num = num.replace(new_str,str(total))
                print('num',num)
                return Compute(num)
            elif len(new_str.split('*')) > 1:  # 乘法运算
                total = int(new_str.split('*')[0]) * int(new_str.split('*')[1])
                print('total*',total)
                num = num.replace(new_str,str(total))
                return Compute(num)

    elif re.findall('[\+|\-]+', num):
        new_str = re.split('([\+|\-]+\d+\.?\d*)', num)
        print('new_str:',new_str)
        for value in new_str:
            if len(str(value)) >0:
                if re.findall('.',value):
                    total += float(value)
                else:
                    total += value
                print('total+-:',str(total))
                # num = num.replace(value,total)
            else:
                print('-----------')
                return str(total)
            # new_str = num.replace(new_str, str(total))
        # return Compute(new_str)

    # return b


def str_split(args):
    Aa = args
    while True:
        ret = re.split('\(([^\(\)]*)\)',Aa,1)
        print(ret)
        for n in ret:
            # if n.__contains__('(') :
            if re.findall('^[\+\-\*\/]',n) or re.findall('[\(\)]',n) or re.findall('[\+\-\*\/]$',n) :
                print('sb',n)
                pass
            else:
                num1 = Compute(n)
                S = str.format("(%s)")%n
                Aa = args.replace(S,str(num1))
                print(Aa)
                print('###')
                # return str_split(num2


# str_split()



a = str_split(origin)
print(a)

