li=["a",2,12,"sd","alex",["彭亮","小羽"],"mkl"]
print(li)#列表中可以嵌套列表，可以是数字，字符串，列表
print(li[2])
print(li[3:-1])
li[1]=[11,22,33,44]#列表可以被修改的
print(li)
#删除
del li[1:3]
print(li)
#列表也可以用in来操作
#在列表中每一个元素是用逗号来划分的在列表中的元素的列表中的元素
#比如内嵌套的列表中的元素不算是在里面
lii=[1,12,19,"age",["石振翁",[19,10],"彭亮"],"ex",True]
ma= lii[4][1][1]#内嵌列表中找出所需要的值
print(ma)
a="123"
vvv=str (a)#字符串的转换
print(vvv)
new_li=list(a)
print(new_li)
#字符串想转换为列表，内部使用for循环
lo=[11,22,33,"asd"]#如果都是字符串可以用join的方法
li.append(3)#不需要赋值 ，可以直接在原来的后面直接追加
print(li)
#li.clear()#清除列表内的元素
#print(li)
bv=li.copy()#浅拷贝
print(bv)
kl=li.count("a")#计算元素中的出现的个数
print(kl)
li.extend([997,"bda"])#二者不同的是扩展原列表
print(li)
pp=li.index(997)#根据值获取当前值索引位置
print(pp)
li.insert(0,88)#指定索引位置插入想要的
print(li)
o=li.pop()#删除某个值 并且获取删除的值
# 括号中如果不指定默认删除最后一个值
print(li)
print(o)
li.remove("a")#与pop类似  指定 删除某个元素
print(li)
li.reverse()#反转
print(li)
lili=[11,22,33,44]
lili.sort(reverse=True)
print(lili)

text='hjejjdfljkf'
for i in range(len(text)):
    print(i,text[i])
lii=['123','456']
lii.append(987)
print(lii)#添加  只能添加一个字符串
lii.pop(0)#指定的范围
print(lii)