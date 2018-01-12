class oo():
    def ooo(self):
        print('-----族长-----')
   
class a(oo):

    def __init__(self):
        self.head = '头'
        self.eye = '眼睛'

    def fan(selt):
        print('HELLO')

class b(oo):
    def __init__(self):
        self.eye = '眼睛'
   #     super().__init__()
    def fang(self):
    #    super().fang()
        print('hello')

class c(a,b):
    #def __init__(self):
     #   self.leg = '腿'
    def fa(self): 
        print('啦啦')  
z = c()
z.fan()
