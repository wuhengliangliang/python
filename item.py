class Foo:
    def __getitem__(self, item):#检查
        print("getitem")
        return
    def __setitem__(self, key, value):#赋值
        print("setitem")
        self.__dict__[key] = value
    def __delitem__(self, item):#删除
        print("delitem")
f1=Foo()   #没有传入任何的值 所以 为空
print(f1.__dict__)
f1['name']='pl'#没有调用属性  要在set函数中添加一个属性设置
f1['age']='18'#这两个需要在赋值函数中 封装一个属性 self.__dict__[key] = value
print(f1.__dict__)#触发的是attr的系列的
del f1.name
print(f1.__dict__)
#item 只是用于字典的方式操作 f1. 是attr的内置函数 item 运用中括号
del f1['name']#触发了
f1['age']
