#一个元类没有申明自己的元类，默认他的元类就是type，除了使用元类type，
# 用户也可以通过继承type来自定义元类（顺便我们也可以瞅一瞅元类如何控制类的创建，工作流程是什么）
class MyType(type):  # 自定义一个元类 也就是类
    def __init__(self,a,b,c):
        print('wdeawd')
        print(a)
        print(b)
        print(c)
    def __call__(self, *args, **kwargs):
        print('.......'*20)  # 就是在执行 Foo.__init__
        print(args,kwargs)
        obj=object.__new__(self) # object.__new__(Foo)-->(这一步就是来产生f1的)f1
        self.__init__(obj,args,kwargs)  # 就是在执行 Foo.__init__
class Foo(metaclass=MyType):# Foo 括号里面是定义的一个元类是 MyType #Foo=MyType(Foo,'FOO',(),{})--->__init__
    def __init__(self,name):
        self.name=name  # f1.name = name name这个属性字典被封装在obj的属性字典中
print(Foo)
f1=Foo('pl',x=1)
print(f1) # 当加入 call 方法时候 触发 call 这样会导致 f1是 none
# 实例去调用方法 自动 传给 self 参数  然后运行
# 类去调用方法  该传几个 传几个参数
# Foo() 这样就是在执行内部的call方法

