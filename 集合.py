s={1,2,3,4,5}
print(s)
dic={"key":"vale"}
#集合与字典不同的是，字典是键值对组成的
print(dic)
a={1,1,1,2,3,5,4,6,6,6}#集合是不同的元素组成
#  注意可以去除重合的
print(a)
i={"alex","alex","mle"}#集合的无序性和不可重性
print(i)
#l={[1,2,3],4,5}集合的不可变性  可以定义元组不能定义列表
#print(l)
o=set("hello")#自带的内建函数 可以定义集合
print(o)
s1=set(["alex",2,3])#用set  就可以用列表的方式
print(s1)
s1.add('5')#只能加入单个的引号中的元素，不能用逗号隔开
print(s1)
s1.clear()#清除  与列表和字典相同类型
print(s1)
s2={'s',1,2,3}
s2.pop()
print(s2)#随机删除pop

s2.remove('s')#指定的元素删除用remove,删除不存在的元素会报错
print(s2)
s.discard(2)#删除不存在的数不会报错
print(s)
             #集合关系运算交差并集
python=['lcg','szw','zjw']
linux=['lcg','syw']
python_and_linux=[]
for p in python:#用for循环处理两个列表中共同的元素
    if p in linux:
        python_and_linux.append(p)
print(python_and_linux)
p_s=set(python)
l_s=set(linux)
print(p_s,l_s)
print(p_s&l_s)#求交集用&或者用 变量名.intersection
print(p_s.union(l_s))#或者用|也可以表示并集
print(p_s-l_s)#求差集，内建函数是difference，那边减那边 除了相同的 剩下被减数的集合元素
print(l_s-p_s)
#交差补集
print(p_s^l_s) #内建函数p_s.symmetric_difference(l_s)
ss1={1,2,3}
ss2={1,2,4}
print(ss1.isdisjoint(ss2))#判断如果没有 交集 就得到true，
print(ss1.issubset(ss2))#判断前面的是后面的子集
print(ss2.issuperset(ss1))#前面的集合是后面集合的父集
#.update 可以更新后赋值给前面的 变量名
ss1.update(ss2)#可以传元组 和列表 都可以，add 只能增加一个值
print(ss1)
# 符号 没有加号
#   集合可以追加的  但是不能修改  是可变类型，s=frozenset()不可变的集合


