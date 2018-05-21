class Room():
    def __init__(self,name,owner,width,length,height):
        self.name=name
        self.owner=owner
        self.width=width
        self.height=height
        self.length=length
    @property
    def cal_area(self):
        #print("%s家的%s 面积是%s" %(self.owner,self.name,self.length*self.width))
        return self.length*self.width
    @property
    def cal_volume(self):
        return self.length*self.height*self.width


r1=Room('厕所','彭亮',100,100,10000)
#r1.cal_area()
r1.cal_area#加上装饰器 就不需要 加括号调用
print(r1.cal_area)
print(r1.owner,r1.name)
r2=Room('别墅','彭亮',1000,1000,100000)
print('这是属于彭亮和笨丫头韦斯羽的别墅大约有',r2.cal_volume)
print(r2.name,r2.owner)



