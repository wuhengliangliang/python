#对象后面加括号触发执行
class Foo: #类本身也是一个对象
    def __call__(self,*args,**kwargs):
        print('实例执行')
f1=Foo() # 产生Foo的某个call方法
f1()#Foo下的call方法
#执行时调用这个对象的类下面的call方法
