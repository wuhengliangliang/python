f=open('陈丽',encoding='utf-8')#文件的编码问题
data=f.read()
print(data)
#文件读取模式 是 r w a   只读 只写
#默认打开的模式 是读 模式
print(f.readable())
#  w  文件存在会直接清空，新建一个空文档 覆盖在上面
p=open('陈丽','r+',encoding='utf-8')
p.write("2222222222\n")#需要直接加入一个换行
# p.write("11111111111111111\n")#写的参数 必须是字符串，读出来的也是一样
# p.close()
# with open('a.txt','w') as f:
#     f.write('111111\n')#产生一个新的文件 不用手动关闭
print(sum(range(101)))
from functools import reduce
l=[1,25,6,3]
res=reduce(lambda x,y:x+y,l,10)#列表的名字 和初始值
print(res)
f=open('tses.py','wb')
f.write(bytes('11111\n',encoding='utf-8'))#不能写字符串 用bytes转换成字符串
f.write('杨戬\n'.encode('utf-8'))
# f=open('a.txt','w',encoding='gbk')
# print(f.closed)
# print(f.encoding)
#当不知道原文件的编码是什么  读和写 都会报错
#tell告诉当前位置在哪
#seek用来控制光标的时间
p.truncate(2)
#用来文件的截取  注意截取的时候不能用写
o=open('a.txt','rb')
# print(o.tell())
# o.seek(10,2)#seek相对位置 不能用编码形式
# # 可以倒着读 负号 第一个括号内的数字是字节
# print(o.tell())
# print(o.read())
# data1=o.readlines()
# print(data1[-1].decode('utf-8'))
#seek的高级玩法 ：需要查找文件的最后一行
for i in o:#循环文件袋额推荐方式
    off=-10
    while True:
        o.seek(off,2)
        data=o.readlines()
        if len(data) > 1:
            print('文件的最后一行%s'%(data[-1].decode('utf-8')))
            break
        off*=2