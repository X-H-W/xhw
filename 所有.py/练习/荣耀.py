wz = [{'name':'123'},{'passwd':'321'}]
while True:
    print('1、注册2、登录')
    zhuce_login = int(input('请输入你的选项'))
    def zhuce():
        name = input('请输入你要注册的帐号')
        zhanghao = []
        for dictionary in zhanghao:
            zhanghao.append(cc['name'])
        if name in zhanghao:
            print('请重新输入帐号')
        elif name not in zhanghao:
            passwd = input('请输入你的密码')
            dic = {}
            dic['name'] = name
            dic['passwd'] = passwd
            wz.append(dic)
            print('注册成功')
    def login():
        name = input('请输入你的帐号')
        for dictionary in wz:
            zhanghao = []
            zhanghao.append(dictionary['name'])
        if name not in zhanghao:
            print('帐号输入错误，重新输入')
        elif name in zhanghao:
            pawd = input('请输入密码')
            i = 0
            length = len(wz)
            dic = {}
            while i <= length - 1:
                dic = wz[i]
                if dic['name'] == name:
                    mimas = int(dic['passwd'])
                    break
                else:
                    i += 1 
                    dic = {}
            if pswd == mimas:
                print('登录成功')
                
    if zhuce_login == 1:
        zhuce()
    elif zhuce_login == 2:
        login()
