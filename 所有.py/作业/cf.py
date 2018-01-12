class cf:
    def __init__(self,newname):
        
        self.name = newname
    def ren(self):
        print('%s'%self.name)
    def qiang(self):
        print('枪有:ak47、m4a1')
    def shou(self):
        print('手枪:沙鹰、新usp、cop')
    def dao(self):
        print('刀:普通小刀、屠龙、尼泊尔')
aa = cf('人物:奥莫')
aa.ren()
aa.qiang()
aa.shou()
aa.dao()
