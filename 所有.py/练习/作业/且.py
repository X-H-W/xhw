def app(a,b):
    a1 = a
    a2 = b
    sum = a+b
    return sum
def ap(a):
    a1 = a
    a2 = app(2,3)
    return{'qq':a1,'wx':a2}
av=ap(6)
print('用户输入的内容%s，最终的和为%s'%(av['qq'],av['wx']))
