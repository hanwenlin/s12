import  time
import sys

def view_bar(num,total):
    rate = num / total
    rate_num = int(rate * 100)
    r1 = '\r%s>>%d%%' %("="*num,rate_num,)  #\r回到当前行输出
    # print(r)
    sys.stdout.write(r1)
    sys.stdout.flush()      #



if __name__ == '__main__':


    for i in range(0,101):
        time.sleep(0.5)
        view_bar(i,100)