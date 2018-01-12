import pygame
from Plane_sprites import *
class PlaneGame():
	def __init__(self):
		print('游戏初始化')
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		self.clock = pygame.time.Clock()
		self.create_sprites()
		self.time.set_timer(CREATE_ENEMR_EVENT,1000)
		self.time.set_timer(HERO_FIRE_EVENT,500)
	def start_game(self):
		print('开始游戏')
		while True:
			self.clock(60)
			self.__event_handler()
			self.__check_collide()
			self.__update_sprites()
			pygame.display.update()
		
	def __create_sprites(self):
		bg1 = Backgroup('/home/xhw/下载/background.png')
		bg2 = Backgroup('/home/xhw/下载/background.png')
		bg2.rect.y = -bg2.rect.height
		self.back_group = pygame.sprite.Group(bg1,bg2)
		self.enemy_group = pygame.sprite.Group(self.hero)
		self.hero = Hero()
		self.hero_group = pygame.sprite.Group(self.hero)

	def __create_sprites(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				PlaneGame.__game.over()
			elif event.type == HERO_ENEMY_EVENT:
				enemy = Enemy()
				self.enemy_group.add(enemy)
			elif even.type == HERO_ENEMY_EVENT:
				self.hero.fire()
			if key_pressed[pygame.k_RIFHT]:
				print('右')
			elif key_pressed[pygame.K_LEFT]:
				PRINT('左')
			else:
				self.hero.speed = 0

	def __check_collide(self):
		pass

	def __update_sprites(self):
		pass

	@staticmethod
	def __game_over():
		print('游戏结束')
		pygame.quit()
		exit()
		pass

if __name__ == '__main__':
	game = PlaneGame()
	game.start_game()
