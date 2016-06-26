
import json
# new_conf = input('请输入您要增加的配置:')
new_conf = ' {"backend": "test.oldboy.org","record":{"server": "100.1.7.999","weight": 20,"maxconn": 30}}'
s = json.loads(new_conf)
print(type(s))
print(s['record']['server'])
print(s['backend'])


server = s['record']['server']
weight = s['record']['weight']
maxconn = s['record']['maxconn']
s2 = '''\n\t\tserver %s %s weight %s maxconn %s '''%(server,server,weight,maxconn)
print(s2)



flag = True
lines = -1


with open('haproxy.conf','r+') as f:
    for num,n in enumerate(f.readlines()):
        if "test.oldboy.org" in n:
            lines = num+2
            flag = False
            print(lines,n)
        else:
            if num == lines and flag == False :
                Seek = f.tell()
                f.writelines(s2)
                # print(n)

# with open('haproxy.conf','a') as f:
#     f.seek(Seek)
#     f.writelines(s2)