import pygame
# 打开
pygame.init()
# 弄一个游戏边框  screen是变  display是屏幕 set_mode大小
screen = pygame.display.set_mode((480,700))
# 放入图片 包+模块+方法(路径)  .
bg = pygame.image.load('/home/xhw/下载/background.png')
# 绘制 变.blit 图片 
screen.blit(bg,(0,0))

# 飞机的初始位置
hero_me = pygame.image.load('/home/xhw/下载/life.png')
hero_rect = pygame.Rect(200,600,102,126)
screen.blit(hero_me,hero_rect)
pygame.display.update()

# 游戏时钟
while True:
    pass








# 关闭
pygame.quit()
