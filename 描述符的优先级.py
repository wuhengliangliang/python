class Foo:
    def __get__(self, instance, owner):#取值触发
        print("get")
    def __set__(self, instance, value):#赋值触发
        print("set",instance,value)
        # instance.__dict__["x"]=value #如果进行这步操作 就会在下一个类中调用字典传入值
    def __delete__(self, instance):#删除触发
        print("delete")
class Bar:
    x=Foo() #这就显示描述符在何地
b1=Bar()
b1.x=1  #实例化中 会现在自己的属性字典当中寻找 找不到 则在类中找
        # 类对应的是对象，对象里面是一个描述符
print(Bar.x)#触发了get属性
# 没有触发 类属性 会高于 描述符的属性  所以只在自己的字典中触发
del b1.x # 主要先对自己的类实例化 然后去 找描述符
                     #  优先级的大小如下:
                     # 类属性>数据描述符
                     # 数据描述符>实例属性
                     # 实例属性 >非数据描述符
                     # 非数据描述符 >找不到
print("----->"*20)
b2=Bar()
Bar.x=1111111 #当类属性重新对x赋值 便不会触发描述符的操作
b2.x  #这就证明了类属性的优先级高于数据描述符 高于 实例属性


