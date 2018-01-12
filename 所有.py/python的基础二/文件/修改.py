def zhuce(account,password):
    f = open('account.txt','w')
    f.write(account)
    f.close()
    f2 = open('password.txt','w')
    f2.write()
    f2.close()
print('注册成功')

def denglu(account,password):
    f = open('account.txt','r')
    b = readlines()
    f2 = open('password.txt','r')
    c = f2.readlines()
    if account == b[0]:
        if password ==c[0]:
            print('登录成功')
    f.colse()
    f2.close()
    
