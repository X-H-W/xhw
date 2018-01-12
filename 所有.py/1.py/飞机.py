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
	
	def strart_game(self):
		print('开始游戏')
		while True:
			self.clock,tick(60)
			self.__event_handler()
			self.__check_collide()
			self.__update_sprites()
			pygame.displaty.update()

	def __create_sprites(self):
		pass

	def __create_sprites(self):
		pass

	def __check_collide(self):
		pass

	@staticmethod
	def __game_over():
		print('游戏结束')
		pygame.quit()
		exit()

if __name__ == '__main__':
	game = PlaneGame()
	game.start_game()
