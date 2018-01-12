import pygame
# 开始
pygame.init()
# display(窗口) 类
# set_mode() 方法 初始化我们的显示窗口
# update() 方法 刷新我们的屏幕
screen = pygame.display.set_mode((480,700))
# image.load
# 第一步 加载图片
bg = pygame.image.load('/home/xhw/下载/background.png')
# 第二步 绘制图片
screen.blit(bg,(0,0))
# 第三步 更新图片
pygame.display.update()

hero_fly = pygame.image.load('/home/xhw/下载/enemy3_n1.png')
screen.blit(hero_fly,(170,0))
pygame.display.update()

hero_fly = pygame.image.load('/home/xhw/下载/bullet1.png')
screen.blit(hero_fly,(255,400))
pygame.display.update()

hero_fly = pygame.image.load('/home/xhw/下载/bullet1.png')
screen.blit(hero_fly,(255,500))
pygame.display.update()

hero_fly = pygame.image.load('/home/xhw/下载/life.png')
screen.blit(hero_fly,(235,650))
pygame.display.update()

# 游戏时钟
clock = pygame.time.Clock()
while True:
    # 设置频率
    clock.tick(120)  
    pass
pygame.quit()
