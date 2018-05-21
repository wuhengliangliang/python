#描述符的总结
#描述符是可以实现大部分python类特性中的底层魔法包括
#  @ classmethod @staticmethod,@property 甚至是__slots__属性
 # 装饰器 也可以是一个类
           # @ 后面跟一个名字 就是语法堂
class Lazyproperty:
    def __init__(self,func):
        self.func=func
    def __get__(self, instance, owner): #描述符的get方法 有两个参数 一个是 instance 一个是 owner  描述符是代理别人都的属性
        print("get方法被触发")  #instance 就是r1的实例本身 owner 是r1.的类
        res=self.func(instance)
        return res
    def __set__(self, instance, value):
        pass
class Room:
    def __init__(self,name,width,length):
        self.name=name
        self.width=width
        self.length=length
    # @ Lazyproperty# 给类增加描述符的功能  area=Lazyproperty(area) 得到一个返回值 就是实例化的对象 装饰器只要加上括号就是在运行  # 相当于把Lazyproperty 加上一个括号（这个括号中中传入的参数就是下面定义的函数名） # 运行
    #  可以是一个类也可以是一个函数 area=Lazyproperty(area)
    @property # 这一步相当于触发了 area 函数的执行   # area=Lazyproperty(area)  这个就是相当于这个功能一样 #@ Lazyproperty
    def area(self):
        return self.width*self.length
    @property
    def test(self):
        return '11111111'
r1=Room('厕所',100,100)
# print(r1.area)
# print(Room.__dict__)
print(r1.area)
print(r1.test)
print(r1.area)
