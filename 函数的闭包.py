def father(name):
    print("from father %s"%name)
    def son():
        name='pll'
        print("your father is %s"%name)
        def grandson():
            print('grandfather is %s'%name)
        grandson()
    son()
father('pl')
import time
def timer(func):
    def wrapper(*args,**kwargs):
        print(func)
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time=time.time()
        print('运行时间 %s'%(stop_time-start_time))
        return res
    return wrapper
@timer
def test(name,age):
    time.sleep(0.2)
    print("test 函数运行完毕, name：%s ,age:%s"%(name,age))
    return '这是test 的返回值'
res=test("pl",18)
# @ timer 就相当于 test=timer(test)
def test1(name,age,gender):
    time.sleep(0.2)
    print("test1函数运行完毕, 名字%s,年龄:%s，性别：%s"%(name,age,gender))
    return '这是test1 的返回值'
test1('pl',18,'male')

def test2(name,age,gender):
    print(name)
    print(age)
    print(gender)
def test1(*args,**kwargs):
    test2(*args,**kwargs)
test1('axle',18,'male')
