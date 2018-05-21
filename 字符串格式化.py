msg='my name is %s my hobby'%'pl'
print(msg)
msg='i am my hobby is alex','lhf'
print(msg)
msg='i am '+'pl'
print(msg)#用加号 会增加内存
msg='i am %s my hobby is %s'%('lhf',[1,2])#%s可以用任何类型数字，字母 列表都可以
print(msg)
#字符串的浮点数
tpl="percent % 2.2f%%"%2.2222222#用%.4s可以截取后四位
print(tpl)
tpl2="i am %(name)s age %(age)d"%{"name":"alex","age":18}
print(tpl2)#以键值得方式传送值
#百分号的方式   %[(name)][flage]:+-数字(左对齐 右对齐)，[width]
print("root",'x','0','0',sep=':')#分割符式sep=
#format字符串格式化
tp="i am {},age {},{}".format("(seven)",18,'alex')
print(tp)#利用format传送值
# 在大括号中,可以用列表 元组，字母数字，但是 必须一一对应的关系
t="i am {2},age {1},{0}".format("seven",18,'alex')#对应索引的关系
print(t)
#可以取相同的  如果取不到  会报错
tt="i am {name},age {age},{name}".format(**{"name":"seven","age":18})
print(tt)#要传字典必须加入两个星号
l=["seven",18]
p="i am {:s} age {:d}".format(*l)#列表的方式来对应
print(p)
t1="numbers：{:b},{:0},{:d},{:x},{:X},{:%}".format(15,15,15,15,15,15.87623)
print(t1)

