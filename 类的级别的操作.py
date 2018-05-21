#类调用自己的方法
#静态方法
class Room:
    tag=1
#     @classmethod#只能 访问类的属性
#     def tell_info(cls,x):
#         # print(cls)
#         print("____>",cls.tag,x)#直接调用类
# Room.tell_info(10)
    @staticmethod#和类和实例分别分隔开  只是名义上的归属类管理，不能使用类变量和实例变量，是类的工具包
    def have_a_bath(a,b,c):
        print('%s %s %s 正在洗澡'%(a,b,c))
Room.have_a_bath('pl','pll','plll')
