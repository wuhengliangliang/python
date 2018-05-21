#授权：授权是包装的一个特性，包装一个类型通常是对已存在的类型的一些定制，
# 这种做法可以新建,修改或删除原有产品的功能。
# 其它的则保持原样。授权的过程,即是所有更新的功能都是由新类的某部分来处理,
# 但已存在的功能就授权给对象的默认属性。
class Open:
    def __init__(self,filename,mode='r',encoding='utf-8'):
        self.file=open(filename,mode,encoding=encoding)#封装了所有的文件方法
        self.mode=mode
        self.encoding=encoding
    # def read(self):
    #     print("read")
    # def write(self):
    #     pass
    def __getattr__(self, item):
        print(item)
        return getattr(self.file,item)#get 一个内存地址，return 一个方法
f1=Open('a.txt','w')#被封装后 在父类找不到
print(f1.file)
print(f1.read)#找不这个方法 全部被封装在file 这个属性当中
