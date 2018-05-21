class School:
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
    def zhao_shen(self):
        print('%s 正在招生'%self.name)
class Course:
    def __init__(self,name,price,period,school):
        self.name=name
        self.price=price
        self.period=period
        self.school=school
s1=School('阜师院','北京',)
s2=School('oldboy','南京')
s3=School('oldboy','东京')
c1=Course('linux',10,'1h',s1)
print(c1.school.addr)
msg='''
    1 老男孩北京校区
    2 老男孩南京校区
    3 老男孩东京校区

'''
while True:
    print(msg)
    menu={
        '1':s1,
        '2':s2,
        '3':s3,
    }
    choice=input(">>>")
    school_obj=menu[choice]
    name=input("课程名：")
    price=input("课程费用")
    period=input("课程周期")
    new_course=Course(name,price,period,school_obj)
    print('课程%s属于%s学校'%(new_course.name,new_course.school.name))
    