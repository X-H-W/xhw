class cf:
    def __init__(self,newname):
        self.name = newname

    def ren(self):
        print('%s'%self.name)
    def qiang(self):
        print('步枪:ak47:远程距离射击')
    def shou(self):
        print('手枪:cop:中距离射击')
    def dao(self):
        print('刀:小刀:近距离攻击')
oo = cf('奥莫')
oo.ren()
oo.qiang()
oo.shou()
oo.dao()
