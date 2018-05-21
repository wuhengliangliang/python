import os
def file_handler(backend_data,res=None,type='fetch'):
    if type == 'fetch':
        with open('pll.t','r') as pl:
            tag=False
            ret=[]
            for read_line in pl:
                if read_line.strip() == backend_data:
                    tag=True
                    continue
                if tag and read_line.startswith('backend'):
                        # tag=False
                        break
                if tag:
                    print('\033[1;45m%s\033[0m' %read_line,end='')
                    ret.append(read_line)
        return ret
    elif type == 'change':
        with open('pll.t', 'r') as pl, \
                open('haproxy.conf_new', 'w') as write_f:
            tag = False
            has_write = False
            for read_line in pl:  # server
                if read_line.strip() == backend_data:
                    tag = True
                    continue
                if tag and read_line.startswith('backend'):
                    tag = False
                if not tag:
                    write_f.write(read_line)
                else:
                    if not has_write:
                        for record in res:
                            write_f.write(record)
                        has_write = True
        os.rename('pll.t', 'haproxy.conf.bak')
        os.rename('haproxy.conf_new', 'pll.t')
        os.remove('haproxy.conf.bak')
def fetch(data):
    print("\033[1;35m这是查询功能\033[0m")
    print('\033[1;33m这是用户数据\033[0m',data)
    backend_data='backend %s'%data
    with open('pll.t','r') as pl:
        tag=False
        for read_line in pl:
            if read_line.strip()==backend_data:
                tag=True
                continue
            if tag and read_line.startswith('backend'):
                break
            if tag:
                print('\33[1;46m%s\33[0m'%read_line,end=' ')

def add():
    print('这是增加的吗')
def change(data):
    print("需要改变",data)
    backend=data[0]['backend']
    backend_data = 'backend %s' % backend
    old_server_record='%s server %s %s weight %s maxconn %s\n'%(' '*8,data[0]['record']['weight'],
                                                                    data[0]['record']['server'],
                                                                    data[0]['record']['weight'],
                                                                    data[0]['record']['maxconn'])
    new_server_record = '%sserver %s %s weight %s maxconn %s\n' % (' ' * 8, data[1]['record']['server'],
                                                                   data[1]['record']['server'],
                                                                   data[1]['record']['weight'],
                                                                   data[1]['record']['maxconn'])
    print(old_server_record)
    res=fetch(backend)
    print(res)
    if not res or old_server_record not in res:
        return "修改记录不存在"
    else:
        index=res.index(old_server_record)
        res[index]=new_server_record

    res.insert(0,'%s\n' %backend_data)
    file_handler(backend_data,res=res,type='change')
def delete():
    print("这是删除的")


def quit():
    print("退出")
if __name__ == '__main__':
    #if __name__ == '__main__'
    # 就相当于是 Python 模拟的程序入口。Python 本身并没有规定这么写，这只是一种编码习惯。
    # 由于模块之间相互引用，不同模块可能都有这样的定义，而入口程序只能有一个。到底哪个入口程序被选中，这取决于 __name__ 的值。
    msg='''
    1：查询
    2: 添加
    3：改变
    4：删除
    5：退出
    '''
    dic_name={'1':fetch,
              '2':add,
              '3':change,
              '4':delete,
              '5':quit,
    }
    while True:
        print(msg)
        choice=input('请输入你的选项：').strip()
        if not choice:continue
        if choice=='5':break
        data=input('请输入你的数据：').strip()
        if choice !='1':
            data=eval(data)#查询需要用eval转换成本身的数据类型
        res=dic_name[choice](data)
        print('最终结果',res)
# [{'backend':'www.oldboy1.org', 'record':{'server':'2.2.2.4','weight': 20,'maxconn':3000}},{'backend':'www.oldboy1.org','record':{'server':'2.2.2.5','weight':30,'maxconn':4000}}]
