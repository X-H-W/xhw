'''
游戏:英雄联盟
1.注册帐号
2.登录帐号
3.选择服务器：
4.创建名称：
人物职业:法师 射手 打野 辅助 上单
法师:火女 阿哩
射手:探险家 暗夜猎手
打野:瞎子 小丑
辅助:机器人 石头人
上弹:瑞文 剑圣
'''
lol = '英雄联盟提示'
print(lol.center(40))
print('*'*40)
print('第一步:%s\n第二步:%s\n第三步:%s\n第四步:%s\n'%('注册','登录','选择服务器','输入你要的名称'))
print('*'*40)
account_list = [{'name':'16537','passwd':'16537'}]
acc = []
#注册帐号
def register():
    account = input('注册帐号')
    passwd = input('密码')
    
    for dic in account_list:
        if account in account_list:
             
                print('存在') 
        else:
            print('注册成功')
            
            
#登录帐号

def login():
    account1 = input('请输入登录帐号')
    passwd1 = input('请输入你的密码')
    for dic in account_list:
        acc.append(dic['name'])
        if account1 in acc:
            a = acc.index(account1)
            b = account_list[int(a)]
            if passwd1 == b['passwd']:
                print('登录成功')
      
            else:
                print('密码错误')
            
        else:
            print('帐号错误')
        login()
#选择服务器 服务器:ser
    dm = '德玛西亚'
    wv = '无畏先锋'
    sj = '水晶之痕'
    print = ('服务器1:%s\n服务器2:%s\n服务器3:\n'%(dm,wv,sj))
    oo = input('请输入你要进入的服务器')
    
        # print('欢迎来%s'%oo)
    
#输入你要创建的名称
def name1():
    pass
print('*'*50)
account = input('请输入创建的帐号')
passwd = input('输入你的密码')
print('*'*50)
login()
print('*'*50)
print('由于天气原因服务器维护，现在只有德玛西亚')
a = input('请输入你要进入的服务器1是德玛西亚2是无畏先锋3是水晶之痕')
if a == 1:
    print('服务器关闭')
else:
    print('欢迎进入')

