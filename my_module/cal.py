def add(x,y):
    return x+y
def sum(x,y):
    return x-y
import time
print(time.time())
t=time.localtime()
print(time.localtime())
print(t.tm_year)
print(t.tm_wday)
print(time.gmtime())
#将结构化时间转换为时间戳
print('_'*80)
print(time.mktime(time.localtime()))
#将结构化时间转换成字符串
print(time.strftime("%Y-%m-%d %X",time.localtime()))#时和秒 统一的写法是%X
#将字符串时间转换成结构化时间
print(time.strptime("2018:04:02:17:41:15","%Y:%m:%d:%X"))

print(time.asctime())
print(time.ctime())
import datetime
print(datetime.datetime.now())