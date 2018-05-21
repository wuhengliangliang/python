#定义 一个类
class C:
    def __init__(self):
        self.name='SB'

# 从其他文件中调用这个类
from untitled.moudle和class import C
c1=C()
#但是如果从别的模块中调用
# 不知道在那个文件下的模块 这时  需要用module
print(c1.name)
print(c1.__module__)
print(c1.__class__) #最后一个可以看出导入的 类名
