class catzu:
    def catzu(self):
        print('我是猫族长')
        print('我什么也会')
class hua(catzu):
   # def __init__(self):
    #    chi = '吃'
    def fu(self):
        print('我是父亲')
    def fly(self):
        print('会飞')
    def zhuo(self):
        print('会捉老鼠')
class zi(catzu):
   # def __init__(self):
    #    run = '跑'
    def mu(self):
        print('我是母亲')
    def swim(self):
        print('我会游泳')
    def haha(self):
        print('我会叫')
class hz(hua,zi):
    def xin(self):
        print('我是刚出生的猫')
    def ming(self):
        print('我叫小黑')
    def haha(self):
        print('我会变身')
    def sheng(self):
        print('变身:猫妖')
    def ya(self):
        print('---呀!变态---')

mao = hz()
mao.catzu()
mao.fu()
mao.fly()
mao.zhuo()
mao.mu()
mao.swim()
mao.xin()
mao.ming()
mao.haha()
mao.sheng()
mao.ya()
