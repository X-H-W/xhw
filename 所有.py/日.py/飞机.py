# import pygame
# pygame.init()
# gygame.quit()
# from pygame import *
# init()
# quit()
# 1.导入pygame模板 2.开始 3.结束 4.初始化模块 5.添加循环 6.给一个背景 7.添加图片 load加载  绘制窗口 刷新窗口 8.添加飞机

import pygame
pygame.init()
# 屏幕 display 设置大小 set_mode
# 自定义 = 包.屏幕.大小 (窗口大小)  
screen = pygame.display.set_mode((480,700))
# 自定义 = 包.模板(image).方法 (load)
bg = pygame.image.load('/home/xhw/下载/background.png')
# 绘制 模块.位置(bg(0,0))
screen.blit(bg,(0,0))

hero_me = pygame.image.load('/home/xhw/下载/life.png')
# 飞机初始位置
hero_rect = pygame.Rect(200,600,46,57)
screen.blit(hero_me,hero_rect)
# 敌人飞机
clock = pygame.time.Clock()
while True:
    # 设置频率
    clock.tick(60)
    if hero_rect.y == 0:
        hero_rect.y = 600
    else:
    # 设置y的值
        hero_rect.y = hero_rect.y - 2
    screen.blit(bg,(0,0))
    screen.blit(hero_me,hero_rect)
    pygame.display.update()
pygame.quit()

