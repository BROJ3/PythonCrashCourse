import pygame

class Ship():

	def __init__ (self,ai_settings,screen):
		self.screen=screen
		self.ai_settings=ai_settings

		self.image = pygame.image.load('try_yourself/horizontal_bullets/images/krab.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#start new ship at the center of the left side of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.left = self.screen_rect.left

		#store a decimal value for shp's center
		self.center = float(self.rect.centerx)

		#movement flag
		self.moving_up =False
		self.moving_down = False

	def update(self):

		#update ship's position based on movement flag
		if self.moving_up:
			print(self.rect)
			self.rect[1] -= self.ai_settings.ship_speed_factor
		if self.moving_down:
			print(self.rect)
			self.rect[1] += self.ai_settings.ship_speed_factor

		self.rect.centerx = self.center

	def blitime(self):

		self.screen.blit(self.image,self.rect)