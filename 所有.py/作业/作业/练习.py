class car(object):
    def move(self):
        print('-'*30)
        print('移动')
    def stop(self):
        print('-'*30)
        print('停车')

class pao(object):
    def move(self):
        print('移动了')
    def stop(self):
        print('停车额')

class ke(object):
    def order(self,name):
        if name == '车':
            car = pao()
        elif name == '跑车':
            car = che()
        return car
a = car()
a.move()
a.stop()
c = ke()
print(c.order) 
