__author__ = 'zhangjun'

name = input("name:").strip()
age = input("age:")
job = input("job:").strip()

#print("Infomation of []:" + name + "\nName:[]" + name + "\nage:[]" + age  + "\njob:[]" + job )
#print("Infomation of %s:\nName:%s\nAge:%s\nJob:%s" %(name,name,age,job))


msg='''
Infomation of %s:
    Name:%s
    Age:%s
    Job:%s
'''%(name,name,age,job)

print(msg)
