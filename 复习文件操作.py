f=open("a.at",'w',encoding='utf-8')
# f.flush()
f.write('abc\n')
f.write('pll\n')
f.write('彭亮你好啊\n')
f=open('a.at','r',encoding='utf-8')
# print(f.readlines())#readlines()读出来是列表的形式 比较节省内存
for i in f:
    print(i)
g=open('a.at','rb')
data=g.read()
data=data.decode('utf8')  #这步 需要解码
print(data)
