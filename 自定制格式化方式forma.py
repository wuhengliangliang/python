x='{0} {1} {2}'.format('dog','pl','op')#传入指定用format
print(x)
#做成一个字典的形式
format_dic={
    'ymd':'{0.year}{0.month}{0.day}',
    'mdy':'{0.month}-{0.day}-{0.year}',
    'd:m:y':'{0.day}:{0.month}:{0.year}',
}
class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    def __format__(self, format_spec):
        print("-->",format_spec)
#找不到需要加入一个判断
        if not format_spec:
            format_spec='ymd'
        fm=format_dic[format_spec]#这个key 指的是format指代定义的字典
        return fm.format(self)
d1=Date('2018','4','19')
# x='{0.year}:{0.month}:{0.day}'.format(d1)
format(d1)
# print(x)
print(format(d1))
print(format(d1,'ymd'))
print(format(d1,'d:m:y'))