# 什么是元类 是类的模板
# 原类就是类的类，是类的模板
# 元类是如何创建类的，正如类是创建对象的模板一样
# 元类的实例为类，正如类的实例为对象（f1对象是Foo类的一个实例，Foo类是type类的一个实例）
# type是python的一个内建元类，用来控制生成类，python 中任何class 定义的类实质都是type类实例化的对象
class Foo:
    pass
f1=Foo()#f1是通过Foo实例化的对象
print(type(f1))
print(type(Foo)) # 类的类就是对象
def __init__(self):
    pass
def test(self):
    pass
FFo=type('Foo',(object,),{'x':1,'__init__':__init__,'test':test})
print(FFo.__dict__)
print(FFo.x)
