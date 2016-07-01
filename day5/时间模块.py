import  time
'''
print(time.clock())#返回处理器时间
print(time.process_time())#返回处理器时间，3,3开始已经废弃
print(time.time())#返回当前系统时间戳1467274490.3744617
print(time.ctime())#Thu Jun 30 16:16:50 2016输出当前系统时间
print(time.ctime(time.time()-86400))#时间戳换算后，转成字符串格式
print(time.gmtime(time.time()-86400))#按照struct格式输出时间|格林威治时间0时区。。       time.struct_time(tm_year=2016, tm_mon=6, tm_mday=30, tm_hour=8, tm_min=20, tm_sec=29, tm_wday=3, tm_yday=182, tm_isdst=0)
print(time.localtime(time.time()-86400))#时间运算后，按照struct格式输出时间，返回本地时间time.struct_time(tm_year=2016, tm_mon=6, tm_mday=29, tm_hour=16, tm_min=25, tm_sec=4, tm_wday=2, tm_yday=181, tm_isdst=0)
print(time.mktime(time.localtime()))#与time.localtime()功能相反,将struct_time格式转回成时间戳格式
# time.sleep(4)#程序阻塞4s
print('---------------')


print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()))#2016-07-01 02:13:23#将struct_time格式转成指定的字符串格式
print(time.strptime("2016-01-28","%Y-%m-%d"))#time.struct_time(tm_year=2016, tm_mon=1, tm_mday=28, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=28, tm_isdst=-1)#将字符串转换成struct格式


'''
import datetime
print(datetime.date.today())#输出格式2016-07-01
print(datetime.date.fromtimestamp(time.time()-864400))#2016-06-21把时间戳转换为日期格式
current_time = datetime.datetime.now()

print(current_time)#2016-07-01 10:18:29.621349
print(current_time.timetuple())##返回struct_time格式,time.struct_time(tm_year=2016, tm_mon=7, tm_mday=1, tm_hour=10, tm_min=18, tm_sec=54, tm_wday=4, tm_yday=183, tm_isdst=-1)

print(current_time.replace(2013,1,1))#2013-01-01 10:20:19.754649输出当前时间，但是指定的数据被替换
str_to_date = datetime.datetime.strptime("21/11/06 16:30","%d/%m/%y %H:%M")   #2006-11-21 16:30:00按指定格式格式化日期
# str_to_date = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(str_to_date)

new_date = datetime.datetime.now() + datetime.timedelta(days=10) #比现在加10天
print(new_date)
new_date = datetime.datetime.now() + datetime.timedelta(days=-10) #比现在减10天
print(str_to_date)
new_date = datetime.datetime.now() + datetime.timedelta(hours=-10) #比现在减10小时
print(str_to_date)
new_date = datetime.datetime.now() + datetime.timedelta(seconds=120) #比现在+120s
print(str_to_date)
'''
2006-11-21 16:30:00
2006-11-21 16:30:00
2006-11-21 16:30:00
'''