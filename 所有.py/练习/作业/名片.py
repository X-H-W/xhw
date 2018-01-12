'''
1.添加一个新的名字
2.删除一个名片
3.修改一个名片
4.查询一个名片
5.显示所有名片
6.退出系统
'''
print('*'*20)
card_infors = []
while True:
    num = int(input('请输入操作序号'))
    if num == 1:#添加名片
        new_name = input('请输入新的名字:')
        new_qq = input('请输入新的QQ:')
        new_wechat = input('请输入微信:')
        new_addr = input('请输入地址:')
        new_tel = input('请输入电话:')
        #创建一个空字典
        #第一个方法
        #new_infor = {}
        #new_infor['name'] = new_name
        #new_infor['qq'] = new_qq
        #new_infor['wechat'] = new_wechat
        #new_infor['addr'] = new_addr
        #new_infor['tel'] = new_tel
        #第二个方法
        new_infor = {'name':new_name,'qq':new_qq,'addr':new_addr,'tel':new_tel}
        card_infors.append(new_infor) 
        for name in card_infors:
            print('*'*20)
            for k,v in name.items():
                print('%s:%s'%(k,v))
    elif num == 2:#删除名片
        name = input('请输入要删除的名片')
        index = 0
        for dic in card_infors:
        #如果用户输入的名字和我们当前
            if dic['name']==name
                del card_infors[index]
            else:
                index+=1
    elif num == 3:#修改名片
        temp1 = input('请输入你要修改的名片')
        
            print('错误')
    elif num == 4:#查询名片 
        temp = input('请输入你要查询的名片姓名') #temp是变量
        if temp == new_infor['name']:
                print(temp)
    elif num == 5:#显示所有名片
        for dic in card_infors:
            print('*'*20)
            for k,v in dic.items():
                print('%s:%s'%(k,v))
    else:
        break
        print('退出系统')
