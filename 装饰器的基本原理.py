#装饰器本身就是函数
# 装饰器就是闭包函数的一种应用场景
# 二 什么是装饰器
#
# 装饰器他人的器具，本身可以是任意可调用对象，被装饰者也可以是任意可调用对象。
# 强调装饰器的原则：1 不修改被装饰对象的源代码 2 不修改被装饰对象的调用方式
# 装饰器的目标：在遵循1和2的前提下，为被装饰对象添加上新功能
def deco(obj):
    print('===========',obj)
    obj.x=1
    obj.y=2
    obj.z=3
    return obj
### @deco是全局变量
# @deco  # 装饰器的原理就是 运行了deco 目的是：test=deco(test)   deco把test传入进去同时得到一个(返回值 传给func)  再赋给test
# def test():
#     print('test函数运行')
# print("+"*20)
# @deco  #就是相当于 Foo=deco(Foo)
# class Foo:
#     pass
# print(Foo.__dict__)
 #  @ 不仅可以在函数前面加  还可以在类前面加
print("-------------------"*30)
# @deco
def test(): # 一切皆对象 test 也是对象
    print('test')
test.x=1
test.y=2
print(test.__dict__)