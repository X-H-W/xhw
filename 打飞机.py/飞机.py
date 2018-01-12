import pygame
pygame.init()
screen = pygame.display.set_mode((480,700))
bg = pygame.image.load('/home/xhw/下载/background.png')
screen.blit(bg,(0,0))
hero_me = pygame.image.load('/home/xhw/下载/life.png')
hero_rect = pygame.Rect(200,600,46,57)
screen.blit(hero_me,hero_rect)
pygame.display.update()
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    if hero_rect.y == 0:
        hero_rect.y = 600
    else:
        hero_rect.y = hero_rect.y - 2
    screen.blit(bg,(0,0))
    screen.blit(hero_me,hero_rect)
    pygame.display.update()
    pass
while True:
    clock.tick(60)
    if hero_rect.y == 0:
        hero_rect.y = 600
    else:
        hero_rect.y = hero_rect.y - 1
    screen.blit(bg,(0,0))
    screen.blit(hero_me,hero_rect)
    pygame.display.update()
pygame.quit()
