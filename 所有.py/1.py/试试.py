import pygame
pygame.init()
screen = pygame.display.set_mode((480,700))
bg = pygame.image.load('/home/xhw/下载/background.png')
screen.blit(bg,(0,0))
yx = pygame.image.load('/home/xhw/下载/life.png')
rect = pygame.Rect(200,600,46,57)
screen.blit(yx,rect)
pygame.display.update()
clock = pygame.time.Clock()

while True:
	clock.tick(60)
	if rect.y == 0:
		rect.y == 600
	else:
		rect.y = rect.y -2
	screen.blit(bg,(0,0))
	screen.blit(yx,rect)
	pygame.display.update()
	pass
while True:
	clock.tick(60)
	if rect.y == 0:
		rect.y == 600
	else:
		rect.y = rect.y - 1
	screen.blit(bg,(0,0))
	screen.blit(yx,rect)
	pygame.display.update()
pygame.quit()
