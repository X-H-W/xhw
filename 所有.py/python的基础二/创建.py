def zhuce(account,password):
    f = open('account.txt','r')
    account_lisr = f.readlines()
    pass
def denglu(account,password):
    f = open('account.txt','r')#只读打开
    account_list = f.readlines()
    names = []
    for name in account_list:
        names.append(name.rstrip())
    if account in names:
        print('登录成功')
    else:
        print('登录失败')

account = input('请输入你的帐号')
denglu()
