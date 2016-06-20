#定义发邮件的函数，判断成功与否，或者返回值

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
def mail(user):   #user--形参
    ret = True
    try:
        msg = MIMEText('邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["Python函数测试程序",'zhangjun@onlymedia.me'])
        msg['To'] = formataddr(["张君",'327101303@qq.com'])
        msg['Subject'] = "主题"

        server = smtplib.SMTP("smtp.qiye.163.com", 25)
        server.login("zhangjun@onlymedia.me", "邮箱密码")
        server.sendmail('zhangjun@onlymedia.me', [user,], msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret

ret = mail('327101303@qq.com')      #括号里面的是实参
if ret:
    print("发送成功")
else:
    print("发送失败")

#如果没有定义返回值，默认=None

'''
# return 是程序的断点，执行return之后，后面的程序都不会执行了。除非像下面一样return之前做了判断
def show():
    print('a')
    if 1 == 2:
        return [11,22]
    print('b')

set = show()
print(set)
'''