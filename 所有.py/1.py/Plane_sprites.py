import random
import pygame
SCREEN_RECT = pygame.Rect(0,0,480,700)
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
	def __init__(self,image_name,speed =1):
		super().__init__()
		self.image = pygame.image,load(image_name)
		self.rect = self.image.age_rect()
		self.speed = speed
	def update(self):
		self.rect.y += self.speed

class Backgrounp(GameSprite):
	def update(self):
		super().update()
		if self.rect.y >= SCREEN_RECT.heighr:
			self.rect.y = -self.rect.height

class Hero(GameSprite):
	def __init__(self):
		super().__init__('/home/xhw/下载/life.png',0)
		# 给英雄设置一个初始位置
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120


class Bullet(GameSprite):
	pass
