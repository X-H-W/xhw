import pygame
from Plane_sprites import *

class PlaneGame(object):
	'''飞机大战主游戏类'''
	def __init__(self):  # 初始化游戏
		# 窗口
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		# 游戏时钟
		self.clock = pygame.time.Clock()
		# 背景 英雄 敌机 
		self.__create_sprites()
	def start_game(self):  
		'''开始游戏'''
		print('开始游戏')

while True:
	# 设置帧率
	self.clock.tick(60)
	# 事件监听
	self.__even_handler()
	# 碰撞检测
	self.__check_collide()
	# 更新精灵
	self.__update_sprites()
	# 屏幕显示
	pygame.display.update()
	def __even__handler(self):
		'''监听事件'''
		for event in pygame.event.get():
			if event.type == pygame.QUIT() 
				PlaneGame.__game_over()
	@staticmethod
	def __game__over():
		pygame.quit()
		exit()

	def __check_collide(self):
		'''碰撞检测'''
		pass

	def __update_sprites(self):
		'''更新精灵和精灵组'''	
		for group in [self_group,self.dd_group,sel.yy_group]
		group.update()
		group.draw(self.screen)
		pass

	def __create_sprites(self):
		'''创建精灵用的'''
		# 背景组
		bg1 = Backgrounp
		self.bg_group = pygame.sprite.Group()
		# 敌机组
		self.dd_group = pygame.sprite.Group()
		# 英雄组
		self.yy_group = pygame.sorite.Group()
		pass


if __name__ == '__main__':
	# 创建游戏对象
		game = PlaneGame()
	# 开始游戏
		game.start_game()
