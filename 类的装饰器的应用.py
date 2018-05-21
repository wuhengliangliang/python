class Typed:
    def __init__(self,key,expect_type):
        self.key=key
        self.expect_type=expect_type
    def __get__(self, instance, owner):#owner 是p1的类
        # print('get方法')
        # print('instance参数【%s】'%instance)
        # print('owner参数【%s】'%owner)
        return instance.__dict__[self.key]  #get方法 会找return 里面的key
    def __set__(self, instance, value):#set里接收的instance 就是p1本身
        # print('set方法')
        if not isinstance(value,self.expect_type):
            # print("你传入的类型错误")
            # return #相当于终止函数
            raise TypeError('%s传入的类型错误，不是%s'%(self.key,self.expect_type)) #直接结束
        # print('instance参数【%s】' % instance)
        # print('value参数【%s】'%value )
        # instance.__dict__[self.key]=value
    def __delete__(self, instance):
        # print("delete方法")
        instance.__dict__.pop(self.key)
def deco(**kwargs):
    def wrapper(obj):
        for key,val in kwargs.items():
            print('===>',key,val)
            setattr(obj,key,Typed(key,val))
            setattr(People,'name',Typed('name',str)) #People.name=Typed('name',str)
        return obj
    return wrapper
@deco(name=str,age=int,gender=str,salray=float)
class People:
    name=Typed('name',str)
    age=Typed('age',int)
    salary=Typed('salary',float)
    def __init__(self,name,age,salary,gender,heigth):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
        self.height=heigth
print('------>>>>')
p1=People('pl','18',300000.0,'man',170)
print(People.__dict__)