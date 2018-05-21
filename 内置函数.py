#abs()绝对值
print(all([1,2,0,'alx']))#判断所有的元素的bool值，
print(all(''))#如果可迭代对象是空 返回的是true
print(bin(3))#十进制转换为二进制

#对于bool 是空 none ，0，其余都是true
print(bool(''))
name='你好'
print(bytes(name,encoding='utf-8'))#需要编码 先定义一个变量
# 把一个字符串 改成一个编码打印出来
print(bytes(name,encoding='utf-8').decode('utf-8'))#decode是解码
print(bytes(name,encoding='utf-8').decode('gbk'))#asc11码不能编码中文
print(chr(122))
print(dir(all))#打印某一个对象，一个查看对象
print(divmod(10,3))#取余
dic={'name':'alex'}
dic_str=str(dic)#转换为字符串
print(dic_str)
express="1-2*5"
t=eval(express)#打印数据类型 与字符串的值
print(t)
#hash  不可变的数据类型，不问传入的长度多长 都有固定的长度
#可以用来检查 东西是否被篡改。
#print(help(all))#里面函数怎么用
print(hex(12))#十进制转换为16进制
print(oct(12))#十转8

print(isinstance(1,int))#判断是否为（int）：(可变)   类型
l=[1,3,2,100]
print(max(l))
print(min(l))
print(list(zip(('a','b','c'),(1,2,3))))
print(list(zip(('a','b','c','d'),(1,2,3))))#自左向右 一一对应的关系
p={'name':'alxe','age':18}
print(list(zip(p.keys(),p.values())))#zip  拉链的方法  只要是序列就可以
#zip: 序列包括 列表 元组 字符串
age_dic={'age':18,'age1':20,'age2':22}#比较一位一位比较的在asc2的值
print(max(age_dic.values()))
print(max(age_dic))#默认的k值
for item in zip(age_dic.values(),age_dic.keys()):
    print(item)
    #zip是一个可迭代对象 必须用for 来打印出来
#不同的类型用max函数无法比较
print(list(zip(age_dic.values(),age_dic.keys())))
#max函数处理的是可迭代对象，相当于一个for循环取出每个元素进行比较
#注意不同类型之间不能进行比较，是从每个元素的第一个位置依次比较
#如果这一个位置分出大小，后面的都不需要比较了，直接得出这两元素的大小
#字典无序的无法进行比较（在列表中的字典）
people=[
    {'name':'alex','age':100},
    {'name':'wupeiqi','age':1000}

]
ret=[]
max(people,key=lambda dic:dic['age'])
for item in people:
    ret.append(item['age'])
print(ret)
print(pow(3,3,2))#3**3%2
l=[3,5,84,9]
print(list(reversed(l)))
print(set('hellol'))#set是集合
l='hello'
s1=slice(1,3)
print(l[s1])#必须把切片放在列表中
#对于sorted 排序 不能不同类型
people=[
    {'name':'alxe','age':100000},
    {'name':'wupeiqi','age':10000},
]
print(sorted(people,key=lambda dic:dic['age']))
#匿名函数 需要早列表里面
name_dic={
    'alex':2000,
    'wupeiq':300,
    'yuanhao':9000
}
print(sorted(name_dic,key=lambda key:name_dic[key]))
print(sorted(zip(name_dic.values(),name_dic.keys())))
print(sum(range(101)))
mag='123'
if type(mag) is str:
    mag=int(mag)
    res=mag+1
    print(res)
def test():
    msg="dasdsadd"
    print(msg)
    print(vars())
test()

# def pl():
#     print('你好啊')
# import test
# test.pl()#import 不能导入字符串
# moudle_name='test'
# m=__import__(moudle_name)  可导入字符串
# m.test()

