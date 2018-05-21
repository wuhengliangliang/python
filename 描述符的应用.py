#__get__():调用一个属性时,触发
#__set__():为一个属性赋值时,触发
#__delete__():采用del删除属性时,触发
#直接用描述符本身的对象是没有调用的效果的
class Typed:
    def __init__(self,key,expect_type):
        self.key=key
        self.expect_type=expect_type
    def __get__(self, instance, owner):#owner 是p1的类
        print('get方法')
        # print('instance参数【%s】'%instance)
        # print('owner参数【%s】'%owner)
        return instance.__dict__[self.key]  #get方法 会找return 里面的key
    def __set__(self, instance, value):#set里接收的instance 就是p1本身
        print('set方法')
        if not isinstance(value,self.expect_type):
            # print("你传入的类型错误")
            # return #相当于终止函数
            raise TypeError('%s传入的类型错误，不是%s'%(self.key,self.expect_type)) #直接结束
        # print('instance参数【%s】' % instance)
        # print('value参数【%s】'%value )
        instance.__dict__[self.key]=value
    def __delete__(self, instance):
        print("delete方法")

        instance.__dict__.pop(self.key)
        # print('instance参数【%s】' % instance) #p1的实例
class People:
    name=Typed('name',str) #name属性被taped代理了  触发了 t1.__set__
    age=Typed('age',int)
    def __init__(self,name,age,salary):#没有对这些属性加上类型限制
        self.name=name
        self.age=age
        self.salary=salary
p1=People('pl',18,2000000)#实列化的过程  #触发了get 方法
 # 实列属性>非数据描述符  所以不会触发get 函数
print(p1.salary)
print(p1.__dict__)
# #  #加上类型限制
# print("下一步")
# p1.name # 会触发了 get 方法
# # print(p1.name)
# p1.name='egon'#为一个属性赋值时候触发  修改了一下 还是触发了set
# #做了一次属性的更改
# print(p1.__dict__)
# del p1.name #触发了删除的操作
# #数据描述符的优先级高于属性 所以属性的操作都是 去找描述符去了
# print(p1.__dict__)
p1=People(111,18,2000000)
print(p1.__dict__)

