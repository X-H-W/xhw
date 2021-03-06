# 使用pygame 我们要先到导入这个包
import pygame
from Plane_sprites import *

class PlaneGame(object):
    '''飞机大战主游戏'''
    def __init__(self):
        print('游戏初始化')
        # 1.创建游戏窗口 pygame.display.set._mode 创建游戏窗口 需要寛和长
        # size 取宽高  x取x轴  y取y轴
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏时钟 pygame.time.Clock() 会给我们放回一个时钟对象
        self.clock = pygame.time.Clock()
        # 3.调用私有方法 在里面创建精灵和精灵组
        self.__create_sprites()
        # 4.设置定时器事件 - 每秒创建一家敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        #
        pygame.time.set_timer(HERO_FIRE_EVENT)

    def start_game(self):
        print('游戏开始')
        while True:
            # 1.设置帧率
            self.clock.tick(60)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新精灵组
            self.__update_sprites()
            # 5.更新屏幕显示
            pygame.display.update()

    def __create_sprites(self):
        '''创建精灵和精灵组'''
        # 1.背景精灵组
        bg1 = Backgroup('/home/xhw/下载/background.png')
        bg2 = Backgroup('/home/xhw/下载/background.png')
        #self.back_group = pygame.sprite.Grounp(bg1,bg2)
        bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1,bg2)
        # 2.敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 3.英雄精灵组
        hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
       # pass

    def __event_handler(self):
        '''时间监听的方法'''
        for event in pygame.event.get():  #  获取监听事件的类别
            # 当列表里面有pygame.QUIT这个值的时候
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()            
            #elif evemy == pygame.KEYDOWN and event.key == pygame.k
            #      print('右移动')
            # 类一种方案 返回所有按键的元组
            key_pressef = pygame.key.get_gressed()
            if key_pressed[pygame.K.RIGHT]:
                self.hero.speed = 2
                print('有右移动')
            elif key_pressed[pygame.K_LEFT]:
               print('向左移动')
               self.hero.speed = -2
            else:
                self.hero.speed = 0
    def __check_collide(self):
        '''碰撞检测的方法'''
        pass

    def __update_sprites(self):
        '''跟新精灵组'''
        for group in [self.back_group,self.enemy_group,self.hero_group]:
            # 更新精灵组里面所有精灵的位置
            group.update()
            # 绘制到屏幕上
            group.draw(self.screen)
        #pass

    @staticmethod
    def __game_over():
        '''游戏结束'''
        print('游戏结束')
        pygame.quit()
        exit()
        pass
# 一般情况下 比如有一个场景 测试
if __name__ == '__main__':
    # 创建游戏对
    game = PlaneGame()
    # 调用游戏开始的方法
    game.start_game()
