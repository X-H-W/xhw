class restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    def restaurrant_name(self):
        print('欢迎光临')
        print('里面请')
        print('请问您需要什么')
    def cuisine_type(self):
        print('正在营业')
ke = restaurant('百年老字号','值得信赖')
print(ke.name,ke.type)
ke.restaurrant_name()
ke.cuisine_type()

class user():
    def __init__(self,first_name,last_name):
        self.first = first_name
        self.last = last_name
    def describe_user(self):
        print('用户:姓%s,名%s'%(self.first,self.last))
    def greet_user(self):
        self.sex = int(input('欢迎光临，一共几位'))
        if self.sex <= 3:
             print('请在大厅入座')
        elif self.sex >= 4 and self.sex <= 6:
             print('可以在大厅入座，或者去一楼包间')
        elif self.sex >= 7:
             print('请跟我去二楼')
        else:
             print('请')
people = user('薛','宏伟')
print(people.first,people.last)
people.describe_user()
people.greet_user()
