'''
游戏：英雄联盟
新手指导：
1、注册帐号
2、登录帐号
3、选择服务器
4、创建名称
人物职业
'''
lolo = '新手指导'
print(lolo.center(40))
print('*'*40)
print('*'*40)
print('第一步:%s\n第二步：%s\n第三步：%s\n'%('注册','登录','选择服务器'))
print('*'*40)
lol = [{'name':'123','passwd':'321'}]
while True:
    print('*'*40)
    print('1、登录','2、注册','4、进入''3、退出')
    register_login = int(input('请输入你要选择的功能序号'))

    def register():# 注册
        # 创建一个函数
        name = input('输入你要注册的帐号')
        zhanghao_list = []
        for dictionary in lol:
            zhanghao_list.append(dictionary['name'])
        if name in zhanghao_list:
            print('帐号已存在,请重新输入')
        elif name not in zhanghao_list:
            passwd = input('请输入你的密码')
            # 创建一个字典
            dic = {}
            dic['name']= name
            dic['passwd'] = passwd
            lol.append(dic)
            print('注册成功') 
           
    # 登录
    def login():
        name = input('输入你的帐号')

	for dictionary in lol:
            zhanghao_list = []
            zhanghao_list.append(dictionary['name'])
        if name not in zhanghao_list:
            print('帐号错误，请重新出入')
        elif name in zhanghao_list:
            pswd = input('请输入密码')
            i = 0
            length = len(lol)
            dic = {}# 字典
           
            while i <= length -1:
                dic = lol[i]
                if dic['name'] == name:
                    mimas = int(dic['passwd'])
                    break 
                else:
                    i += 1 
                    dic = {}
            if pswd == mimas:
                print('欢迎来到英雄联盟')
    # 服务器
    def server():
        name = input('输入要进入的服务器')
        dm = '德玛西亚'
       
        zhanghao_listt = [{'name':'德玛西亚'}]
        for name in zhanghao_listt:
            zhanghao_listt.append(dictionary['name'])
        if name in zhanghao_listt:
            print('欢迎来到联盟')
        elif name not in zhanghao_listt:
            print('没有这个服务器')
            dic = {}
            dic['name'] = name
            zhanghao_listt.append(dic)
            print('进入')
            
            print('密码错误')
    if register_login == 2:
        register()
    elif register_login == 1:
        login()
    elif register_login == 3:
        print('祝你玩的愉快')
        break
    elif server == 4:
        server()
    print('欢迎进入德玛西亚')
        
