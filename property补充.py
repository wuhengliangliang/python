class ClassMethod:
    def __init__(self,func):
        self.func=func
    def __get__(self, instance, owner): #类来调用,instance为None,owner为类本身,实例来调用,instance为实例,owner为类本身,
        def feedback(*args,**kwargs):
            print('在这里可以加功能啊...')
            return self.func(owner,*args,**kwargs)
        return feedback
class People:
    name='pl'
    @ClassMethod # say_hi=ClassMethod(say_hi)
    def say_hi(cls,msg):
        print('你好啊,白痴 %s %s' %(cls.name,msg))
People.say_hi('你个白痴')
p1=People()
p1.say_hi('你个白痴')
class Goods:
    def __init__(self):
        self.original_price=1000
        self.discount=0.8
    @property
    def price(self):
        new_prince=self.original_price*self.discount
        return new_prince
    @price.setter
    def price(self,value):
        self.original_price=value
    @price.deleter
    def price(self):
        del self.original_price
obj=Goods()
obj.price #获取商品的价格
print(obj.price)
obj.price=200 #修改商品的原价
print(obj.price)

