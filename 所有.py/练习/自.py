zhao_hao_and_mi_ma = {}
def wzry_deng_lu(zh,mm):
    for zh_1,mm_1 in zhao_hao_and_mi_ma.items():
        if zh == zh_1:
	    if mm == mm_1:
	        print('登录成功')
	    else:
	        print('密码错误')
        else:
	    print('帐号错误')
'''
    print('打开成功')
def zhuce():
    print('注册成功')
def denglu():
    print('登录成功')
    zhaohao = input('输入你的帐号')
    mima = input('输入你的密码')
    if zhaohao in zhaohao and mima.values():
        print('请从新输入帐号')
    else:
	zhao_hao_and_mi_ma['zhao_hao']=zhaohao
	zhao_hao_and_mi_ma['mi_ma']=mima
	print('帐号注册成功，请登录')
	wzry_deng_lu(zhaohao,mima)
    print('注册帐号')
''' 
