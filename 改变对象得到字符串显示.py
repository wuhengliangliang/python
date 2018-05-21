class Foo:
    pass
f1=Foo()#一切节对象
print(f1)
file=open("test",'w')#一切皆对象 但是出现的不是 ，
# 一切皆对象 但是有一些出现的不是想象的  一定是动了手脚
# 定制一些方法来控制输出的是啥
print(file)
class Foo:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '名字是%s 年龄是%s'%(self.name,self.age)  #自己控制str的返回值
    pass
    # def __repr__(self):
    #     return '名字是%s 年龄是%s'%(self.name,self.age)  #自己控制str的返回值
    # pass  运用在解释器当中 print()调用repr 从而调用__repr__()

f1=Foo('pl',18)#实例调用的是类 但是类中没有这个方法
print(f1) #调用的str  调用的f1.__str__()  触发的是str
#如果__str__()没有被定义，n那么就会使用__repr__来代替输出
#注意这两方法的返回值必须是字符串，否则抛出异常


