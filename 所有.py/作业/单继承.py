'''
class cat(object):
    def __init__(self,name,color='灰'):
        self.name = name
        self.color = '灰'

    def run(self):
        print('%s的在跑'%self.name)

class boss(cat):
    def newname(self,newname):
        self.name = newname

     
    def eat(self):
        print('%s在吃'%self.name)

bs = boss('小黑')
print('%s在吃'%bs.name)
print('%s的在跑'%bs.color)
bs.eat()
bs.newname('黑')
bs.run()
'''
class cat(object):
    def __init__(self,name,color= '灰色'):
        self.name = name
        self.color = color
    def run(self):
        print('%s--在跑'%self.name)
        print('%s--在跳'%self.color)
bs = cat('魔','神')
bs.run()
