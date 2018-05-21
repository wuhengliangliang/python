import pickle
import hashlib
import time
def creat_md5():
    m=hashlib.md5()
    m.update(str(time.time()).encode('utf-8'))
    return m.hexdigest()
id=creat_md5()
print(id)
class Base:
    def save(self):
        with open('school.l','wb') as f:
            pickle.dump(self,f)#dump 一个对象所以传了一个self
class School(Base):
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
class Course(Base):
    def __init__(self,name,price,period,school):
        self.name=name
        self.price=price
        self.period=period
        self.school=school
s1=School('阜师院','阜阳')
s2=School('四中','蚌埠')
s3=School('北科大','北京')
Course('linux',100000,'10weeks','北科大')
msg='''
    1 阜阳校区
    2 北京校区
    3 蚌埠校区

'''
while True:
    print(msg)
    menu={
        '1':s1,
        '2':s2,
        '3':s3,
    }
    choice=input("<<<")
    school=menu[choice]
    name=input("课程名称")
    price=input('课程费用')
    period=input("课程周期")
    new_course=Course(name,price,period,school)#在这里的学校改变成了输入的学校重新的命名
    print("这个%s需用%s,需要多少%s"%(new_course.name,new_course.price,new_course.period))