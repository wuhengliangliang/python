# isinstance(obj,cls)检查是否obj是否是类 cls 的对象
# 1 class Foo(object):
# 2     pass
# 4 obj = Foo()
# 6 isinstance(obj, Foo)
# issubclass(sub, super)检查sub类是否是 super 类的派生类
# 复制代码
# 1 class Foo(object):
# 2     pass
# 4 class Bar(Foo):
# 5     pass
# 7 issubclass(Bar, Foo)
# 什么是反射
#
# 反射的概念是由Smith在1982年首次提出的，主要是指程序可以访问、检测和修改它本身状态或行为的一种能力（自省）。这一概念的提出很快引发了计算机科学领域关于应用反射性的研究。它首先被程序语言的设计领域所采用, 并在Lisp和面向对象方面取得了成绩。
# 2
# python面向对象中的反射：通过字符串的形式操作对象相关的属性。python中的一切事物都是对象（都可以使用反射）
#
# 四个可以实现自省的函数
#
# 下列方法适用于类和对象（一切皆对象，类本身也是一个对象）
# 三 __setattr__,__delattr__,__getattr__
#
#
# 复制代码
# class Foo:
#     x=1
#     def __init__(self,y):
#         self.y=y
#
#     def __getattr__(self, item):
#         print('----> from getattr:你找的属性不存在')
#
#
#     def __setattr__(self, key, value):
#         print('----> from setattr')
#         # self.key=value #这就无限递归了,你好好想想
#         # self.__dict__[key]=value #应该使用它
#
#     def __delattr__(self, item):
#         print('----> from delattr')
#         # del self.item #无限递归了
#         self.__dict__.pop(item)
#
# #__setattr__添加/修改属性会触发它的执行
# f1=Foo(10)
# print(f1.__dict__) # 因为你重写了__setattr__,凡是赋值操作都会触发它的运行,你啥都没写,就是根本没赋值,除非你直接操作属性字典,否则永远无法赋值
# f1.z=3
# print(f1.__dict__)
#
# #__delattr__删除属性的时候会触发
# f1.__dict__['a']=3#我们可以直接修改属性字典,来完成添加/修改属性的操作
# del f1.a
# print(f1.__dict__)
#
# #__getattr__只有在使用点调用属性且属性不存在的时候才会触发
# f1.xxxxxx