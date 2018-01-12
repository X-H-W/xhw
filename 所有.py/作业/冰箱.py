class Play_lwh:
    # 写一个构造函数 init 
    def __init__(self,newName,animal):
        self.animal = animal
        self.name = newName
    # 买大象
    def buyAnimal(self):
        #self.animal = '大象'
        print('%s'%self.name,'准备一只%s'%self.animal)
    # 打开冰箱
    def open_bin(self):
        print('打开冰箱')
    # 装进冰箱
    def zhuang(self):
        print('把%s装进冰箱'%self.animal)
    # 关闭冰箱
    def close_bin(self):
        print('关闭冰箱')
game = Play_lwh('九','鼠')
game.buyAnimal()
game.open_bin()
game.zhuang()
game.close_bin()
print('-'*20)
jiu = Play_lwh('翠花','猫')
jiu.buyAnimal()
jiu.open_bin()
jiu.zhuang()
jiu.close_bin()
