user_list=[{'name':'alex','passwd':'123'},{'name':'pl','passwd':'123'},
           {'name':'pll','passwd':'123'},{'name':'xiaoyu','passwd':'123'},]
current_user={'username':None,'login':False}
def auth_func(func):
    def wrapper(*args,**kwargs):
        if current_user["username"]and current_user['login']:
            res=func(*args,**kwargs)
            return res
        username=input("用户名：").strip()
        passwd=input("密码").strip()
        for index,user_dic in enumerate(user_list):
            if username==user_dic['name']and passwd==user_dic['passwd']:
                current_user["username"]=username
                current_user['longin']=True
                res=func(*args,**kwargs)
                return res
        else:
            print('用户名或密码错误')
    return wrapper
@auth_func
def index():
    print("欢迎来到我家")
@auth_func
def home(name):
    print("欢迎回家%s"%name)
@auth_func
def shopping_car(name):
    print('购物车里有%s,%s,%s'%('奶茶','妹妹','玩具'))
home("产品经理")
shopping_car("产品经理,购物车，我的物品")
index()
