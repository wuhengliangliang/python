# name='sb'
# def ok():
#     name='hlf'
#     print(name)
#     def mo():
#         nonlocal name
#         name='lo'
#     mo()
#     print(name)
# ok()
# print(name)
# print(name)
# print('-'*60)
name="sk"
def sk():
    name="alxe"
    def ssbb():
        nonlocal name
        name="冷静"
    ssbb()
    print(name)
    print(name)
sk()
print(name)
sk()
#函数心得：在函数中 一个模块有对应的print
# 并且在调用的时候 里到外来一一对应
def abc():
    print('helll')
abc()
moudle_name='test'
m=__import__(moudle_name)
m.abc()