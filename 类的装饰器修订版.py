 # 类的装饰器有什么好处：可以操作类的属性


def Typed(**kwargs):
    def deco(obj): # deco 是一个局部作用域里的
        for key,val in kwargs.items(): # 这一步相当于把@Typed(x=1,y=2,z=3)的参数加入了Foo的属性中
            setattr(obj,key,val)
        # obj.x=1
        # print('>>>',kwargs)
        # print('类名---->',obj)#既 有了Foo这个类  又有了想要给Foo增加的属性
        return obj #返回值
    # print('====>',kwargs)
    return deco
@Typed(x=1,y=2,z=3)  # 必须传入参数  #函数名加小括号就是下运行函数 #Typed(x=1,y=2,z=3)--->deco  @deco(Foo)
class Foo:
    pass
print(Foo.__dict__)
@Typed(name='pl')
class Bar:
    pass
print(Bar.name)
@Typed(age=18)
class Age:
    pass
print(Age.age)