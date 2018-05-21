#http://www.cnblogs.com/linhaifeng/articles/6182264.html
# def school(name,addr,type):
#     def init(name,addr,type):
#         sch = {
#             'name': name,
#             'addr': addr,
#             'type': type,
#             'kao_shi': kao_shi,
#             'zhao_sheng': zhao_sheng,
#         }
#         return sch
#     def kao_shi(school):
#         print('%s 学校正在考试' % school['name'])
#     def zhao_sheng(school):
#         print('%s %s %s 正在招生' % (school['type'], school['name'],school['addr']))
#     return init(name,addr,type)
# s1=school('old boy','tian cai','私立学校')
# print(s1)
# print(s1['name'])
# s1['zhao_sheng'](s1)
# s2=school('清华','北大','哈弗')
# s2['zhao_sheng'](s2)
                                 #类

class Dog:
    def __init__(self,name,type,addr):
        self.name=name
        self.type=type
        self.addr=addr
    def bark(self):
        print("一条名叫%s %s狗正在%s上吊自杀"%(self.name,self.type,self.addr))
dog1=Dog('alex','female','阜师院')
print(dog1.__dict__)
dog1.bark()

#属性
#类是用来描述一类食物，类的对象指的是这一类事物中的一个个体
#属性：数据属性 就是变量，函数属性：在面向对象里通常称为方法
#类和对象均用 ‘点’ 来访问自己的属性
class Chinese:
    dang='中国人爱共产党'
    def sui_di_tu_tan(self):
        print("随地吐痰")
print(Chinese.dang)
Chinese.sui_di_tu_tan('wo')
print(Chinese.__dict__['dang'])
Chinese.__dict__['sui_di_tu_tan']('wo')

class Chinese:
    def __init__(self,name,age,gender):
        print("初始化函数")
        self.mingzi=name
        self.nianji=age
        self.xingbie=gender
    def sui_di_tu_tan(self):
        print('%s已经%s但是还在吐痰'%(self.mingzi,self.nianji))
    def cha_dui(self):
        print('他插队到了前面')
    # cha_dui('小明')
p1=Chinese('小方',22,'female')#实列  类名 加括号的形式
print(p1.__dict__)
print(p1.nianji)#调用单个的  用点来代替以上类中的前一个
p1.sui_di_tu_tan()
p2=Chinese('小明',18,'男的')
print(p2.__dict__)


#类属性 函数属性
