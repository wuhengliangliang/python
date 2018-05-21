#什么是迭代：更新换代
l=[12,1,25,3]
for i in l:
    print(i)
iter_l=l.__iter__()
print(iter_l.__next__())#相当于for的迭代
index=0
while index < len(l):
    print(l[index])
    index+=1
m=open('a.txt','r+')
iter_m=m.__iter__()
print(iter_m.__next__(),end='')
print(iter_m.__next__(),end='')
print(next(iter_m))
#只要遵循可迭代类型  就是  可迭代对象
#只要有生成器也就是数据类型，也就是可迭代对象
                   #生成器 在python 中有两种表现形式：函数和生成器表达式
#生成器函数的表现形式
def test():
    yield 100
g=test()
print(g.__next__())
  #三元表达式
name='alxe'
res='sb' if name=='alxe' else 'dsb'
print(res)
#列表解析
egg_list=[]
for i in range(10):
    egg_list.append('鸡蛋%s'%i)
print(egg_list)
l=['鸡蛋%s'%i for i in range(10)]
print(l)
li=['成绩%s'%i for i in range(10) if i > 5 ]
print(li)
ll=('鸡蛋%s'%i for i in range(10))#直接的可迭代 是用元组的方式 生成器 使用元组表现形式
print(next(ll))
#在用next的时候 如果next 完毕  会报错
#生成器表达式 直接可以省内存
print(sum(list(range(10000000))))
print(sum(i for i in range(10000)))
                            #浅拷贝
s=[[1,2],'alex','pl']
s1=s.copy()
s1[0][1]=5
print(s,s1)
#修改列表中嵌套列表的元素 浅拷贝 会出现问题
#浅拷贝只能拷贝列表中的第一层
#深拷贝 全部克隆
#copy.copy()浅拷贝
#copy.deepcopy()深拷贝
                               #set 重点
#去重性  在列表中的嵌套列表，和字典的时候  时候 不能用set 转换
#可变集合 不能作为字典的键
li=[1,2,3,74]
s=set(li)
s.add('uu')#在集合中只能添加一个元素
print(s)
s.update([12,'eee'])#在uppdate中连个元素时候必须用列表的形式
print(s)
s.remove('eee')
print(s)
s.pop()
print(s)#随机删除 pop
print(set('nn')<set('alexalexank'))#必须有元素在另一个集合里面
print(set('nn') and set('alexalexank'))#取并集
print(set('nn') or set('alexalexank'))
#差集 （-  ） .difference

