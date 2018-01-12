class sweetpotato:
    def __init__(self):
        self.cookedlever = 0 
        self.cookedstr = '生的'
        self.cookedstr = '烤'
        self.condliments = []
    def cook(self,time):
        self.cookedlever += time
        if self.cookedlever>8:
             print(self.cookedstr)
             self.cookedstr = '烤没了'
        elif self.conkedlever>5:
            self.cookedstr = '烤熟了'
        elif self.conkedlever>3:
            self.cookedstr = '半生不熟'
        else:
            self.cookedstr = '生的'

class xin:
    def __init__(self):
        self.co
potato = sweetpotato()
print('--有一个地瓜，还没有没烤的地瓜--')
print(potato.cookedlever)
print(potato.cookedstr)
print(potato.condliments)
print('*'*50)
potato = sweetpotato()

