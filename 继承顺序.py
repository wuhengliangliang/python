#在python3中，都是新式类 继承顺序采用 广大优先搜索
class A:   #广度优先，找到父类 不找 进行另一支开始找 ，深度：从左先找到父类 开始找另一支找
    print("A")
class B(A):
    print("B")
class C(A):
    print("C")
class D(B):
    print("D")
class E(C):
    print("E")
class C(A):
    print("C")
class F(D,E):
    pass
    # print("F")
f1=F()
# print(f1)
print(F.__mro__)#,mro 中 子类会优于父类被检查，多个父类会根据他们在列表中的顺序被检查，
# 如果对下一个类存在两个合法的选择，选择第一个父类
#调用父类 父类名 加上.___init___
#只有实列化时候 会自动传入一个参数，对象 去调用类方法时候 会自动传self(可以不用加)







