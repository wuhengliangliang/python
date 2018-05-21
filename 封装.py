class People:
    _star='earth'
    __st='pll'#封装到内部
    def __init__(self,id,name,age,salary):
        self.id=id
        self.name=name
        self.age=age
        self.salary=salary
    def get_id(self):
        print("我是彭亮啊，我的id是[%s]"%self.id)
    def get_st(self):#接口函数
        print(self.__st)

p1=People('123','alex','18','1000000')
print(p1._star) # 说是python 中的封装，是可以访问的，并不会真正的阻止你访问私有的属性
# 封装的本质 是明确区分内外  约定  ：任何一单下滑线开头的都应该 是内部的，私有的
p2=People('123','alex','18','1000000')
print(p2._People__st)#双下划线时候需要用 _类名加上__实例化的名字
#第二层面的封装：类中定义私有的，只在累的内部使用，外部无法访问（实际上可以用p2._People__st方式访问）
#第三层面的封装：明确区分内外，内部的实现逻辑，外部无法知晓，并且为封装到内部的逻辑
#提供一个访问接口给外部使用（这才是真正意义上的封装）
p1.get_st()#外部调用接口函数
class Room:
    def __init__(self,name,owner,width,length,high):
        self.name=name
        self.owner=owner
        self.__width=width
        self.__length=length
        self.high=high
    def tell_area(self):#内部定义一个接口函数 可以供外部调用
        return self.__width*self.__length
r1=Room('陋室铭','彭亮',100,1000,10)
print(r1.tell_area())#实现了真正意义上的封装
print(r1.name)           #用下划线 进行封装
#封的时候 接口一定得选好
