# 定义一个父类
class Cat(object):
    def __init__(self,name,color='白色'):
        self.name = name
        self.color = color 
    def run(self):
        print('%s--在跑'%self.name)

# 定义一个子类
class Bosi(Cat):
    def setNewName(self,newName):
        self.name = newName
    def eat(self):
        print('%s--在吃'%self.name)

bs = Cat('波斯')
print('bs的名字为:%s'%bs.name)
print('bs的颜色为:%s'%bs.color)
mao = Bosi('波斯')
mao.eat()
mao.setNewName('波斯')
mao.run()
