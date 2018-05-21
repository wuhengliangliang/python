# 析构放法：当对象在内存中被释放时，自动触发执行。
# 注：此方法一般无需定义，因为python 是一门高级语言，
# 程序员在使用时无需关心内存的分配和释放，
# 析构函数的调用是由解释器在进行垃圾回收时是自动触发执行的
class Foo:
    def __init__(self,name):
        self.name=name
    def __del__(self):
        print('正在执行')
f1=Foo('pl')
del f1 #删除对象 所以可以触发
# del f1.name  这是属性的删除 不会触发
print("_______>") # 进行垃圾回收  自动触发del 函数
#del 整个实例删除是才会触发
