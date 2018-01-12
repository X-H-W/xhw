a = {'o':'学号'}
def test1():
    a['o']= '学号'
    print(a)
def test2():
    print(a)
test1()
test2()
 
def home1(home,homes=[]):
    homes.append(home)
    return homes
def home2():
    print(home1('66',[1,3,5,7]))

home2()
