wzry_gnts = '王者荣耀提示'
print(wzry_gnts.center(30))
print('*'*40)
print('功能1:%s\n功能2:%s\n'%('注册','登录'))
print('*'*40)
account_list = [{'name':'libai','passwd':'123456'}]
def login(account='libai',passwd='123456'):
    for dic in account_list:
        if account == dic['name']:
            if dic['passwd'] == passwd:
                print('登录成功')
            else:
                print('密码错误')
        else:
            print('帐号输入错误')
def register(zhanghao='xiaoxiao',mima='123456'):
    print('注册')
    for dic in account_list:
        if dic['name']==zhanghao:
            print('帐号已被注册')
        else:
            a = {}
            a['name']=zhanghao
            a['passwd']=mima
            account_list.append(a)
            print('帐号注册成功')
print('-'*50)
account = input('请输入帐号')
passwd = input('请输入密码')
login(account,passwd)
login()
print('-'*50)
register(account,passwd)
