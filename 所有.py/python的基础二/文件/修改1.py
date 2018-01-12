def register(account,password):
    c = open('帐号','w+')
    c.write(account)
    c.close()
    c1.write(password)
    c1.close()
def login(account,password):
    o = open('帐号','r')
    b = o.readlines()
    o1 = open('密码','r')
    a = o.readlines()
    if account in b:
        print('帐号输入正确')
        for mm in a:
            if password == mm:
                print('登录成功')
            else:
                print('错误')
    else:
        print('帐号不存在')
    o.close()
    o1.close()
num = int(input('输入是登录还是注册 注1或2'))   
account = input('请输入帐号')
password = input('请输入密码')
if num == 1:
    login(account.password)
elif num == 2:
    register(account.password)
    
