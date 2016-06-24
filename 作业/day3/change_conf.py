
import json
# new_conf = input('请输入您要增加的配置:')
new_conf = ' {"backend": "test.oldboy.org","record":{"server": "100.1.7.999","weight": 20,"maxconn": 30}}'
s = json.loads(new_conf)
print(type(s))
print(s['record'])
print(s['backend'])
lines = 50
with open('haproxy.conf','r') as f:
    for num,n in enumerate(f.readlines()):
        if "test.oldboy.org" in n:
            lines = num+2
            print(lines,n)
    else:
        if num == lines:
            See = f.tell()
            print(See,n)

# with open('haproxy.conf','a') as f:
#     f.seek(Seek)
#     # s1 = '{name} is {acter}'
#     s2 = '\t\t"server" {server} "weight" {weight} "maxconn" {maxconn} '
#     result = s2.format()
import sys
import os