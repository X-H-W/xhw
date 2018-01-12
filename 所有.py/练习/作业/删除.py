# 1 是添加名字 2.删除名字  3.修改名字  4.查询定义
print('*'*50)
print('名字关系管理系统v1.0')
print('1.添加一个新的名字')
print('2.删除一个名字')
print('3.修改一个名字')
print('4.查询一个名字')
print('*'*50)
names = []
while True:
    num = int(input('请输入你需要的功能'))
    print('num=%d'%num)
    if num==1:
        name = input('请输入要添加的用户名')
        names.append(name)
        print('添加成功,当前的名字一共有%s'%names)
    elif num==2:
        pass
    elif num==3:
        pass
    elif num==4:
        find_name = input('请输入查询名字')
        if find_name in names:
            print('查看你要的人')
        else:
            print('查无此人')
    elif num==5:
        break
    else:
        print('输入错误请重新输入')
