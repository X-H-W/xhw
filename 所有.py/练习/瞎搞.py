#姓名:   年龄:   学号:    
mm = []#盒子
def addstudent():#添加
    name = input('输入你的名字')
    age = input('输入你的年龄')
    num = input('输入你的学号')
    pp = {'姓名':name,'年龄':age,'学号':num}#创建字典
    mm.append(pp)
    print('*'*30)
    print('现在的学生有%s'%mm)
def delete():#删除
    name = input('输入你要删除的名字')
    count = 0
    for dic in mm:
        if dic['姓名'] == name:
            del mm[count]
        else:
            #print('没有此人')
            count+=1
    print('现在剩余还有%s'%mm)
def xiu_gai():#修改
    name = input('输入你要修改的名字')
    count = 0
    for dic in mm:
        if dic['姓名'] == name:
           mm[count]['姓名'] = input('请输入姓名')
           mm[count]['年龄'] = input('请输入年龄')
           mm[count]['学号'] = input('请输入学号')
        else:
            count+=1
    print('现在还有%s'%mm)
def cha_xun():#查询
    for dic in mm:
        print('姓名:%s\t年龄:%s\t学号:%s\t'%(dic['姓名'],dic['年龄'],dic['学号']))
def tui_chu():#退出
    pass
addstudent()
addstudent()
delete()
xiu_gai()
cha_xun()
