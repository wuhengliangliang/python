import sys
import os
print(sys.path)#当前程序执行的路径的输出
for i in sys.path :
    print(i)
print("------->>>>")
print(os.getcwd())#获取当前所在的路径
os.chdir(r"C:\Users\Administrator\PycharmProjects\untitled")#r是转义的意思这段话是转换路径
print(os.getcwd())
#os.makedirs(r"aa/bbb/ccc")#多层目录下递归，在aa下有一个bbb,在bbb下有ccc
# os.remove(r"aa/bbb/ccc")#删除空目录 有文件 不能删除
# os.rename("aa","bb")重命名文件或者目录】
# os.system("获取当前的绝对路径")#在CMD中找到所有的文件的名字
print(os.path.abspath(__file__))#系统所在的当前目录下的文件名
print(os.path.split(os.path.abspath(__file__)))#将path分割成目录和文件名二元组返回
print(os.path.join("d:\\"))
print(os.path.join("d:\\","www.","baidu","a.py"))#拼接个绝对路径
print(os.path.join(os.path.dirname(os.path.abspath(__file__)),'b','123','text'))
#加入到当前的路径下
