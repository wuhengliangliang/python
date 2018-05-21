#数据属性和函数属性的增删改查
class Chinese:
    Country="China"
    def __init__(self,name,ball):
        self.name=name
        self.ball=ball

    def play_basketball(self):
        print('%s 正在打%s'%(self.name,self.ball))
p1=Chinese('小明','篮球')
print(p1.__dict__)
print(Chinese.Country)
#类属性的改变
Chinese.Country='sinapore'
print(Chinese.Country)
#增加类属性
Chinese.dang='国名党'
print(Chinese.dang)
#删除
# del Chinese.dang,Chinese.Country
# print(Chinese.__dict__)
def eat_food(self,name):
    print("小明正在吃%s"%self.ball)
Chinese.eat=eat_food
print(Chinese.__dict__)
p1.eat('蛋糕')
                         #实列属性的增删改查
country="中国-------"
class Chinese:
    country="中国"#调用这个属性
    def __init__(self,name):
        self.name=name
        print("--->",country)
    def play_ball(self,ball):
        print("%s正在打%s"%(self.name,ball))
p1=Chinese('alex')
#  不用点调用  和类和 实例没关系
p2=Chinese.country
print(p2)

class Chinese:
    country='China'
    l=['a','b']
    def __init__(self,name):
        self.name=name
p1.l=[1,2,3]#直接在p1中又赋了一个
print(p1.__dict__)
print('_______>',Chinese.l)
p1.l.append('c')
print(p1.__dict__)
print(Chinese.l)#实列调用类的方法时候 不用传第一个参数  但是类去调用实列 必须传第一个参数