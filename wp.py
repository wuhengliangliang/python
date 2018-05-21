test='i love you computeR'
v=test.capitalize()
print(v)
v1=test.endswith('R')
print(v1)
test1='alex'
v2=test1.find('ex',1,7)
print(v2)
test2='i am name'
print(test2)
v3=test1.format(name='alex')
print(v3)
m='i am {0},age {1}'
print(m)
n=test1.format(name='alex,a=19')
print(n)
i=m.format('alex',19)
print(i)
x='i am {name} age {a}'
xx=x.format_map({'name':'wo','a':12})
print(xx)
test3="ush123"
v5=test3.isalnum()
print(v5)
f="12345678\t1233"
d=f.expandtabs(8)
print(d,len(f))
wo="nest\temail\tpasswod\nlayng\twoa\t123\n"
w=wo.expandtabs(10)
print(w)
p="wo"
t=p.isalpha()
print(t)
n="123"
g=n.isdigit()
print(g)
b="d1d "
c=b.isidentifier()
print(c)
dd="二"
i=dd.isnumeric()
print(i)
xx=" eft"
l=xx.isspace()
print(l)
s=input(" ")
print(s)
