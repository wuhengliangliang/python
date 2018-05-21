class Foo:
    def __init__(self,y):
        self.y=y
    def __getattr__(self, item):
        print("你找的【%s】不存在"%item)
    def __delattr__(self, item):
        print('删除操作')
    def __setattr__(self, key, value):
        self.__dict__[key]=value
        print("pl")
f1=Foo(10)
print(f1.y)
print(getattr(f1,'y'))#同调用对象的方法一样
del f1.y
del f1.x # 调用
f1.z=2
# __开头 都是内置的类
print(f1.age)#有了__getattr__()这个内置函数 找不到时候不会报错
