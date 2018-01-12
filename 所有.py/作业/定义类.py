# 定义类
class dog:   # 类名
    # 方法
    def walk(self):
        print('走')
    def drink(self):
        print('喝水')
    def tian(self):
        print('舔')
# 创建一个叫冰糖的对象   sugar是名字
sugar = dog()
sugar.name = '冰糖'
print('那只叫%s狗狗'%sugar.name)
sugar.walk()
sugar.drink()
sugar.tian()

# 再创建一个小狗
diudiu = dog()
sugar.name = '小狗'
print('又出现一只叫%s'%sugar.name)
diudiu.walk()
diudiu.drink()
diudiu.tian()

# 在创建一个小狗  狗名：小黑
xiaohei = dog()
sugar.name = '小黑'
print('有出现一个%s'%sugar.name)
xiaohei.walk()
xiaohei.drink()
xiaohei.tian()
