# 在程序中：务必保证先定义类，后产生对象
# #程序中类的用法
# .:专门用来访问属性，本质操作的就是__dict__
# OldboyStudent.school #等于经典类的操作OldboyStudent.__dict__['school']
# OldboyStudent.school='Oldboy' #等于经典类的操作OldboyStudent.__dict__['school']='Oldboy'
# OldboyStudent.x=1 #等于经典类的操作OldboyStudent.__dict__['x']=1
# del OldboyStudent.x #等于经典类的操作OldboyStudent.__dict__.pop('x')

#程序中的对象
#调用类，或称为实例化，得到对象
# s1=OldboyStudent()
# s2=OldboyStudent()
# s3=OldboyStudent(）



# http://www.cnblogs.com/linhaifeng/articles/6182264.html#_label1
# dog1={ "name":"元昊",
#         "gender":"母的",
#         "type":"藏獒",
#
# }
# dog2={ "mingzi":"元昊",
#         "gender":"母的",
#         "type":"藏獒",
# }
# person1={ "name":"pl",
#         "gender":"super man",
#         "type":"人",
# }

def dog(name,gender,type):
    def jiao(dog):
        print("一条狗[%s],汪汪汪"%dog['name'])
    def chi_shi(dog):
        print("一条[%s] 正在吃屎"%dog['type'])
    def wan_shua(dog):
        print("一条[%s][%s]狗正在玩耍"%(dog['gender'],dog['name']))
    def init(name,gender,type):
        dog1 = {"name": "元昊",
                "gender": "母的",
                "type": "藏獒",
                'jiao':jiao,
                'chi_shi':chi_shi,
                'wan_shua':wan_shua,
                }
        return dog1
    res=init(name,gender,type)
    return res

d1=dog('元昊','母','中华田园犬')
d2=dog('alxe','公','藏獒')
d3=dog('sb','women','taidi')
print(d1)
print(d2)
print(d3)
d1['jiao'](d1)
d2['chi_shi'](d2)
d3['wan_shua'](d3)
#  把一类事物的相同特征和动作整合到一起就是类
#类是一个抽象的概念
#对象：就是基于类而创建的一个具体的事物（具体存在的）
#也就是特征和动作整合到一起
 