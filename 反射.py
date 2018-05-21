#http://www.cnblogs.com/linhaifeng/articles/6204014.html#_label2
# 四个可以反射的对象
#python面向对象中的反射：通过字符串的形式操作对象相关的属性。
# python中的一切事物都是对象（都可以使用反射）
class BlackMedium:#类本身也是一个属性
    feture='Ugly'
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr

    def sell_hourse(self):
        print('【%s】 正在卖房子，傻逼才买呢' %self.name)

    def rent_hourse(self):
        print('【%s】 正在租房子，傻逼才租呢' % self.name)


print(hasattr(BlackMedium,'feture'))
# getattr('pl',"pl")


#
# b1=BlackMedium('万成置地','天露园')
# b1.name--->b1.__dic__['name']
# print(b1.__dict__)
#
# # b1.name
# # b1.sell_hourse
# print(hasattr(b1,'name'))
# print(hasattr(b1,'sell_hourse'))
# print(hasattr(b1,'selasdfasdfsadfasdfasdfasdfasdl_hourse'))
#
#
#
# print(getattr(b1,'name'))
# print(getattr(b1,'rent_hourse'))
# func=getattr(b1,'rent_hourse')
# func()
# # print(getattr(b1,'rent_hourseasdfsa')) #没有则报错
# print(getattr(b1,'rent_hourseasdfsa','没有这个属性')) #没有则报错
#
#
# # b1.sb=True
# setattr(b1,'sb',True)
# setattr(b1,'sb1',123)
# setattr(b1,'name','SB')
# setattr(b1,'func',lambda x:x+1)
# setattr(b1,'func1',lambda self:self.name+'sb')
# print(b1.__dict__)
# print(b1.func)
# print(b1.func(10))
# print(b1.func1(b1))
# del b1.sb
# del b1.sb1
# delattr(b1,'sb')  与类的实例 才有关系 否则 无关
# print(b1.__dict__)
import test as pll
print(pll)
print(hasattr(pll,'say_hi'))#
class Foo:
    def __init__(self,x):
        self.x=x
    def __getattr__(self, item):
        print("执行的是我")
    def __getattribute__(self, item):#首先触发的是这个
        print("执行的是__getattribute__(self, item):")
        raise AttributeError('抛出异常')#自己定的自己
f1=Foo(10)
print(f1.x)
f1.xxxx #找不到时候 会触发 def __getattr__(self, item): 这个函数
#属性存在时候 会返回这个值  不存在时候 会 触发一个异常
