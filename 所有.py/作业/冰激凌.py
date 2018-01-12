class resturant:
    def __init__(self,newname,dao):
        self.name = newname
        self.wei = dao 
    def newname(self):
        print('欢迎光临')
        print('您好,您需要什么冰激凌')
    def dao(self):
        print('正在营业')

class icecreamstand(resturant):
    def ice(self):
        print('草莓冰激凌') 
    def ICE(self):
        self.flavors = ['巧克力','橙']
 
       
Ice = icecreamstand('巧克力味','原味')
Ice.newname()
Ice.ice()
Ice.ICE()
