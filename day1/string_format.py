__author__ = 'zhangjun'

name = raw_input("name:").strip()
age = raw_input("age:")
job = raw_input("job:").strip()

#print("Infomation of []:" + name + "\nName:[]" + name + "\nage:[]" + age  + "\njob:[]" + job )
#print("Infomation of %s:\nName:%s\nAge:%s\nJob:%s" %(name,name,age,job))


msg='''
Infomation of %s:
    Name:%s
    Age:%s
    Job:%s
'''%(name,name,age,job)

print(msg)
