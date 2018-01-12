# 定义  判断
def register(a,b):
#查看所有内容
    f = open('account.txt','r')    # 文件名和操作命令
    account_list = f.readlines()
    f.close()
    length = len(account_list)
    #如果文件没有内容 可不添加
    if length == 0:
        f = open('account.txt','w')
        f.write(a)
        f.close()
    else:
        names = []#容器存放数据
        for name in account_list:
            name = name.rstrip()
            names.append(name)
        # 判断 帐号存在 不存在
        if a in names:
            print('注册失败')
        else:
            print('可以注册')
            # 重新打开文件  追加
            a = '\n'+a
            f = open('account.txt','a')
            f.write(a)
            f.close()
a = input('请输入帐号')
register(a,1)
