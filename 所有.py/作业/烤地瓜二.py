class kao_di_gua:
    def __init__(self):
        self.sheng_shu = 0
        self.sheng_shu_str = '生地瓜'
        self.add_tiao_liaos = []

    def kao(self,times):
        self.sheng_shu += times  
        if self.sheng_shu > 8:
            self.sheng_shu_str = '烤糊了' 
        elif self.sheng_shu > 5:
            self.sheng_shu_str = '烤熟了'
            self.add_tiao_liaos.append('苹果酱')
        elif self.sheng_shu > 3:
            self.sheng_shu_str = '半生不熟'
        else:
            self.add_tiao_liaos.append('橄榄油')
            self.sheng_shu_str = '生地瓜'
kdg = kao_di_gua()
kdg.kao(3)
print(kdg.sheng_shu_str)
kdg.kao(3)
print(kdg.sheng_shu_str)
print(kdg.add_tiao_liaos)
